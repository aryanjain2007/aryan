import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from subjects_reference import cs_subject_reference, me_subject_reference, ee_subject_reference

# Grade point dictionary mapping letter grades to numeric grade points
vit_grade_point_dict = {
    "s": 10, "a": 9, "b": 8,
    "c": 7, "d": 6, "e": 5,
    "f": 0, "n": 0
}

L = []  # Global list to store SGPA values calculated in the current session

# Dictionary to hold subject references for each course
subject_refs = {
    "Computer Science": cs_subject_reference,
    "Mechanical Engineering": me_subject_reference,
    "Electrical Engineering": ee_subject_reference
}

# Main Application class handling the GUI and logic
class SGPA_CGPA_App:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 SGPA & CGPA Calculator")  # Window title
        self.root.geometry("600x450")  # Window size
        self.root.configure(bg="#f0f4f7")  # Background color
        self.root.resizable(True, True)  # Disable window resizing

        # Title label at the top of the window
        title = tk.Label(root, text="VIT CGPA Genie",
                         font=("Helvetica", 18, "bold"),
                         bg="#f0f4f7", fg="#2c3e50")
        title.pack(pady=30)  # Add vertical padding

        # Define button styles for consistent appearance
        button_style = {"font": ("Helvetica", 12), "width": 30, "height": 2, "bd": 0}

        # Button to open SGPA calculation window
        sgpa_btn = tk.Button(root, text="📘 Calculate SGPA",
                             bg="#3498db", fg="white",
                             command=self.sgpa_window, **button_style)
        sgpa_btn.pack(pady=10)

        # Button to open CGPA calculation window
        cgpa_btn = tk.Button(root, text="📊 Calculate CGPA",
                             bg="#27ae60", fg="white",
                             command=self.cgpa_window, **button_style)
        cgpa_btn.pack(pady=10)

        # Exit button to close the application
        exit_btn = tk.Button(root, text="❌ Exit",
                             bg="#e74c3c", fg="white",
                             command=self.root.quit, **button_style)
        exit_btn.pack(pady=10)

    def sgpa_window(self):
        """
        Opens a new window for SGPA calculation.
        Lets user select course, view subjects, input credits and grades,
        and calculate SGPA.
        """
        sgpa_win = tk.Toplevel(self.root)
        sgpa_win.title("SGPA Calculator")
        sgpa_win.geometry("750x800")
        sgpa_win.configure(bg="#ffffff")

        # Label prompting user to select their course
        tk.Label(sgpa_win, text="🎓 Select Your Course",
                 font=("Arial", 13, "bold"),
                 bg="#ffffff", fg="#2c3e50").pack(pady=10)

        # Dropdown menu to select course (CS, ME, EE)
        course_var = tk.StringVar(sgpa_win)
        course_menu = ttk.Combobox(sgpa_win, textvariable=course_var,
                                   state="readonly", width=40)
        course_menu['values'] = list(subject_refs.keys())
        course_menu.pack(pady=5)

        # Frame to display subject-credit reference table
        reference_frame = tk.Frame(sgpa_win, bg="#ffffff")
        reference_frame.pack(pady=10)

        def display_reference(course_dict):
            """
            Displays subject codes and their default credits
            in a text widget with a scrollbar.
            """
            # Clear previous reference table widgets
            for widget in reference_frame.winfo_children():
                widget.destroy()

            # Title for the reference table
            tk.Label(reference_frame, text="📚 Subject Reference Table",
                     font=("Arial", 12, "bold"),
                     bg="#ffffff", fg="#34495e").pack()

            # Text widget to show the table content
            text_area = tk.Text(reference_frame, height=12, width=60,
                                bg="#ecf0f1", fg="#2c3e50",
                                font=("Courier", 10))
            text_area.pack(side="left", fill="both", padx=(10, 0), pady=5)

            # Vertical scrollbar linked to the text widget
            scrollbar = tk.Scrollbar(reference_frame, command=text_area.yview)
            scrollbar.pack(side="right", fill="y")
            text_area.config(yscrollcommand=scrollbar.set)

            # Insert table headers
            text_area.insert(tk.END, f"{'Subject Code':<25}{'Credit':<10}\n")
            text_area.insert(tk.END, "-" * 35 + "\n")

            # Insert each subject and credit row
            for code, credit in course_dict.items():
                text_area.insert(tk.END, f"{code:<25}{credit:<10}\n")

            text_area.config(state="disabled")  # Make read-only

        def next_step():
            """
            Called after course selection.
            Displays subject reference table and allows
            user to input credits and grades for each subject.
            """
            course = course_var.get()
            if not course:
                messagebox.showerror("Error", "Please select a course.")
                return

            subjects = subject_refs[course]
            display_reference(subjects)

            # List to hold entries for credit and grade inputs
            subject_entries = []

            def add_subject_fields():
                """
                Adds input fields for one subject's credit and grade.
                """
                frame = tk.Frame(sgpa_win, bg="#ffffff")
                frame.pack(pady=6)

                # Credit input label and entry box
                tk.Label(frame, text="Credit:", bg="#ffffff", fg="#2c3e50").pack(side="left", padx=5)
                credit_entry = tk.Entry(frame, width=5)
                credit_entry.pack(side="left")

                # Grade input label and entry box
                tk.Label(frame, text="Grade (S/A/B/...):", bg="#ffffff", fg="#2c3e50").pack(side="left", padx=5)
                grade_entry = tk.Entry(frame, width=5)
                grade_entry.pack(side="left")

                # Append this subject's inputs to the list
                subject_entries.append({'credit': credit_entry, 'grade': grade_entry})

            def compute_sgpa():
                """
                Calculate SGPA based on entered credits and grades.
                Validates inputs and shows result or error.
                """
                try:
                    total_weighted = 0
                    total_credits = 0
                    for entry in subject_entries:
                        credit = float(entry['credit'].get())  # Convert credit to float
                        grade = entry['grade'].get().lower()   # Get grade as lowercase
                        if grade not in vit_grade_point_dict:
                            raise ValueError("Invalid grade entered")
                        gp = vit_grade_point_dict[grade]        # Lookup grade point
                        total_weighted += credit * gp
                        total_credits += credit

                    if total_credits == 0:
                        messagebox.showerror("Error", "Total credits cannot be zero.")
                        return

                    sgpa = round(total_weighted / total_credits, 2)
                    L.append(sgpa)  # Store the SGPA in global list

                    messagebox.showinfo("SGPA Result", f"✅ Your SGPA is: {sgpa}")
                except Exception as e:
                    messagebox.showerror("Error", f"❌ {e}")

            # Button to add subject input fields dynamically
            tk.Button(sgpa_win, text="➕ Add Subject",
                      command=add_subject_fields,
                      bg="#2980b9", fg="white",
                      font=("Arial", 10, "bold")).pack(pady=10)

            # Button to calculate SGPA from entered data
            tk.Button(sgpa_win, text="📘 Calculate SGPA",
                      command=compute_sgpa,
                      bg="#27ae60", fg="white",
                      font=("Arial", 10, "bold")).pack(pady=10)

        # Button to confirm course selection and proceed
        tk.Button(sgpa_win, text="📋 Show Subject Reference",
                  command=next_step,
                  bg="#8e44ad", fg="white",
                  font=("Arial", 10, "bold")).pack(pady=15)

    def cgpa_window(self):
        """
        Opens a window or dialog to calculate CGPA.
        If SGPAs are present in current session, computes average.
        Otherwise, prompts user to input previous SGPA list manually.
        """
        if L:  # If SGPA list has values
            avg = round(sum(L) / len(L), 2)  # Calculate average CGPA
            messagebox.showinfo("CGPA Result", f"📊 Your CGPA (this session): {avg}")
        else:
            try:
                # Ask user to input list of previous semester SGPAs as a string
                user_input = simpledialog.askstring("Input", "Enter SGPA list like [8.5, 9.0, 8.0]:")
                sgpa_list = eval(user_input)  # Convert string to list

                # Validate that input is a list of numbers
                if not isinstance(sgpa_list, list) or not all(isinstance(x, (int, float)) for x in sgpa_list):
                    raise ValueError

                cgpa = round(sum(sgpa_list) / len(sgpa_list), 2)
                messagebox.showinfo("CGPA Result", f"📊 Your CGPA (manual input): {cgpa}")
            except:
                messagebox.showerror("Error", "❌ Invalid input format.")

# Entry point: run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SGPA_CGPA_App(root)
   
