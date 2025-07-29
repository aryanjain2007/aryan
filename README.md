VIT CGPA Genie is a user-friendly Python application designed to calculate SGPA (Semester Grade Point Average) and CGPA (Cumulative Grade Point Average) specifically for VIT students. It uses the Tkinter library to provide an interactive graphical interface, removing the need for manual GPA calculations or command-line input.

The app is structured to support three major engineering branches:

Computer Science

Mechanical Engineering

Electrical Engineering

Students can:

View predefined subject-credit mappings for their branch

Dynamically enter subject credits and grades for a semester

Calculate SGPA based on VIT’s grading system

Compute CGPA using session-based or manually entered SGPA values

🔧 How the Code Works (Brief Overview)
The code is organized into a modular and readable structure. Here's a breakdown:

1. Grade Point Mapping
vit_grade_point_dict = {
    "s": 10, "a": 9, "b": 8, "c": 7, "d": 6, "e": 5, "f": 0, "n": 0
}
This dictionary maps VIT's letter grades to numeric grade points. It's used throughout the SGPA computation logic.

2. Subject Reference Handling
The app imports subject-credit dictionaries from subjects_reference.py, which contains mappings like:

cs_subject_reference = {"CSE1001": 3, "CSE1002": 4, ...}
This lets the app display default credit structures for different courses.

3. GUI Layout with Tkinter
The SGPA_CGPA_App class handles the entire interface. It:

Initializes the main window

Sets button styles and positions

Handles window resizing and aesthetics

Three main buttons:

📘 Calculate SGPA

📊 Calculate CGPA

❌ Exit

4. SGPA Calculation Flow
A new window opens when "Calculate SGPA" is clicked.

User selects their course from a dropdown.

The subject-credit reference is displayed.

Users add subjects dynamically with “➕ Add Subject” button.

Each subject includes:

Credit input

Grade input

Clicking “📘 Calculate SGPA” triggers:

Grade validation

Credit-weighted average computation

SGPA display in a popup

SGPA is saved in a global list L[] for session CGPA

5. CGPA Calculation Flow
If SGPA values exist in L[], it calculates and displays the average CGPA.

If no SGPAs are stored yet, it prompts the user to input a list like [9.0, 8.5, 9.2].

The average is validated and shown.

📁 Code Files
main.py: Contains the full GUI and logic implementation

subjects_reference.py: A separate file with dictionaries of subject codes and their default credits

💡 Highlights
Clean and responsive UI using Tkinter

Modular design for easy maintenance

Works without internet or external dependencies

Fully functional for VIT grading system

Designed for beginners to understand GUI development in Python

⚠️ Assumptions and Limitations
Only VIT’s 10-point grading system is supported

Requires valid letter grades (S, A, B, C, D, E, F, N)

No file saving or data persistence (session-based only)

powerpoint presentation: https://prezi.com/view/8TXeHoynS8pwSnFFHcLA/










