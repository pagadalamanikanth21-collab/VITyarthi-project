🎓 Student Management System

A simple console-based Student Management System developed in Python as part of the VITyarthi project. The application helps manage student records, store academic marks, calculate grades, analyze class performance, and maintain persistent data using a JSON file.

📌 Project Overview

The Student Management System provides a straightforward way to manage student academic information through a menu-driven command-line interface.

Each student record contains:

Roll number

Student name

Marks in five subjects

Total marks

Percentage

Grade

The application stores student records in a students.json file, allowing data to persist between program executions. {"fallbackMarkdown":"(GitHub
)","reference":{"matched_text":"","prefix":null,"start_idx":1159,"end_idx":1176,"safe_urls":["https://github.com/pagadalamanikanth21-collab/VITyarthi-project/blob/main/import%20json.py"],"refs":[],"alt":"(GitHub
)","prompt_text":null,"type":"grouped_webpages","status":"done","error":null,"style":null,"items":[{"title":"VITyarthi-project/import json.py at main · pagadalamanikanth21-collab/VITyarthi-project · GitHub","url":"https://github.com/pagadalamanikanth21-collab/VITyarthi-project/blob/main/import%20json.py","attribution":"GitHub","pub_date":null,"snippet":null,"thumbnail_url":"https://images.openai.com/static-rsc-1/W-p58tLUZ3tZdvjPghPRxrcxLeqS86e5872Y6amAmilJ14KX5cGTtY2s_lCDYp5Tjw7LQl2gBTeWW1mqv1v4koOJXfK9WExKQw9hmomMxc81Pd-sykytfyc0PcJuoKHmCjWFicd0XSsdYEFtPqmF12Jpmj0KdayvRvH277HOM64dP2RNUuORdOvItaw8zi4jaPULYi95usGJCm1gzNni7RAcdXF10epmBMZKFu4kMIM","attribution_segments":null,"supporting_websites":[],"refs":[{"turn_index":1,"ref_type":"view","ref_index":0}],"hue":null,"attributions":null}],"fallback_items":null},"showLoginRequiredCard":false}

✨ Features

➕ Add Student — Add a new student with their roll number, name, and subject marks.

👥 View All Students — Display all registered students along with their marks, total, percentage, and grade.

🔍 Search Student — Find a student using their roll number.

📊 Class Average — Calculate the average percentage of all students.

🏆 Find Class Topper — Identify the student with the highest percentage.

🗑️ Delete Student — Remove an existing student record.

📈 Sort Students by Marks — Generate a ranking list based on percentage.

💾 JSON Data Storage — Automatically save and load student records using students.json.

✅ Input Validation — Prevent invalid marks, empty names, duplicate roll numbers, and invalid menu choices.

📚 Subjects

The system currently manages marks for five subjects:

Subject	Maximum Marks
Python	100
Maths	100
Physics	100
English	100
Computer	100
Total	500
🧮 Grading System

Grades are calculated automatically according to the student's percentage:

Percentage	Grade
90–100%	A+
80–89%	A
70–79%	B
60–69%	C
40–59%	D
Below 40%	F
🛠️ Technologies Used

Python 3

JSON — Persistent storage of student records

OS module — File existence and file handling operations

Git & GitHub — Version control and project hosting

The application uses Python's built-in json and os modules and does not require external Python packages. {"fallbackMarkdown":"(GitHub
)","reference":{"matched_text":"","prefix":null,"start_idx":2733,"end_idx":2750,"safe_urls":["https://github.com/pagadalamanikanth21-collab/VITyarthi-project/blob/main/import%20json.py"],"refs":[],"alt":"(GitHub
)","prompt_text":null,"type":"grouped_webpages","status":"done","error":null,"style":null,"items":[{"title":"VITyarthi-project/import json.py at main · pagadalamanikanth21-collab/VITyarthi-project · GitHub","url":"https://github.com/pagadalamanikanth21-collab/VITyarthi-project/blob/main/import%20json.py","attribution":"GitHub","pub_date":null,"snippet":null,"thumbnail_url":"https://images.openai.com/static-rsc-1/W-p58tLUZ3tZdvjPghPRxrcxLeqS86e5872Y6amAmilJ14KX5cGTtY2s_lCDYp5Tjw7LQl2gBTeWW1mqv1v4koOJXfK9WExKQw9hmomMxc81Pd-sykytfyc0PcJuoKHmCjWFicd0XSsdYEFtPqmF12Jpmj0KdayvRvH277HOM64dP2RNUuORdOvItaw8zi4jaPULYi95usGJCm1gzNni7RAcdXF10epmBMZKFu4kMIM","attribution_segments":null,"supporting_websites":[],"refs":[{"turn_index":1,"ref_type":"view","ref_index":0}],"hue":null,"attributions":null}],"fallback_items":null},"showLoginRequiredCard":false}

📁 Project Structure
VITyarthi-project/
│
├── import json.py
├── Student_Management_System_Report.pdf
└── README.md

File Description
File	Description
import json.py	Main Python program containing the Student Management System
students.json	Automatically created file used to store student records
Student_Management_System_Report.pdf	Project report/documentation
README.md	Project documentation

The repository currently contains the Python source file and project report. {"fallbackMarkdown":"(GitHub
)","reference":{"matched_text":"","prefix":null,"start_idx":3294,"end_idx":3311,"safe_urls":["https://github.com/pagadalamanikanth21-collab/VITyarthi-project"],"refs":[],"alt":"(GitHub
)","prompt_text":null,"type":"grouped_webpages","status":"done","error":null,"style":null,"items":[{"title":"GitHub - pagadalamanikanth21-collab/VITyarthi-project · GitHub","url":"https://github.com/pagadalamanikanth21-collab/VITyarthi-project","attribution":"GitHub","pub_date":null,"snippet":null,"thumbnail_url":"https://images.openai.com/static-rsc-1/Lr_9pwEsgQIPe0W3ObD7qaK-5kRcaObluoeLAVxx7oWIGp4CZmkwTOXk_kOJ9rPi7qT-4q5PUqV3xVNxL-ouzGzUxa34LErFPTWPZWKCbRI_EDCXcQzBo5MmtVE0ULb6UbKC9rsNb1kk4u4v4v0iDt2-u2zySUC2sWlwwRmhCX_5uwHh_ChWlVodhprif-ktsHSnSEckdyY7sbJaRuR56qhFr1uWGE3aqO0NGw2KtNg","attribution_segments":null,"supporting_websites":[],"refs":[{"turn_index":0,"ref_type":"view","ref_index":0}],"hue":null,"attributions":null}],"fallback_items":null},"showLoginRequiredCard":false}

⚙️ Requirements

Before running the project, make sure you have:

Python 3.x installed

Git installed (optional, if cloning the repository)

You can verify Python installation with:

python --version


or:

python3 --version

🚀 Installation & Setup
1. Clone the repository
git clone https://github.com/pagadalamanikanth21-collab/VITyarthi-project.git

2. Navigate to the project directory
cd VITyarthi-project

3. Run the application

Because the source file is named import json.py, run:

python "import json.py"


On systems where Python 3 is invoked using python3:

python3 "import json.py"

🖥️ How to Use

After starting the application, a menu will be displayed:

===================================
 STUDENT MANAGEMENT SYSTEM
===================================
1. Add Student
2. View All Students
3. Search Student
4. Calculate Class Average
5. Find Class Topper
6. Delete Student
7. Sort Students by Marks
8. Exit
===================================

Add a Student

Select option 1 and enter:

Roll number

Student name

Python marks

Maths marks

Physics marks

English marks

Computer marks

Marks must be between 0 and 100.

View Students

Select option 2 to display all stored student records, including:

Roll number

Name

Subject-wise marks

Total marks

Percentage

Grade

Search for a Student

Select option 3 and enter the student's roll number to retrieve their academic details.

Calculate Class Average

Select option 4 to calculate the average percentage of all registered students.

Find Class Topper

Select option 5 to display the student with the highest percentage.

Delete a Student

Select option 6 and enter the roll number of the student you want to remove.

Sort Students

Select option 7 to display students in descending order according to their percentage.

Exit

Select option 8 to close the application.

💾 Data Storage

Student information is stored locally in:

students.json


The program automatically loads existing records when it starts and saves changes whenever a student is added or deleted. {"fallbackMarkdown":"(GitHub
)","reference":{"matched_text":"","prefix":null,"start_idx":5553,"end_idx":5570,"safe_urls":["https://github.com/pagadalamanikanth21-collab/VITyarthi-project/blob/main/import%20json.py"],"refs":[],"alt":"(GitHub
)","prompt_text":null,"type":"grouped_webpages","status":"done","error":null,"style":null,"items":[{"title":"VITyarthi-project/import json.py at main · pagadalamanikanth21-collab/VITyarthi-project · GitHub","url":"https://github.com/pagadalamanikanth21-collab/VITyarthi-project/blob/main/import%20json.py","attribution":"GitHub","pub_date":null,"snippet":null,"thumbnail_url":"https://images.openai.com/static-rsc-1/W-p58tLUZ3tZdvjPghPRxrcxLeqS86e5872Y6amAmilJ14KX5cGTtY2s_lCDYp5Tjw7LQl2gBTeWW1mqv1v4koOJXfK9WExKQw9hmomMxc81Pd-sykytfyc0PcJuoKHmCjWFicd0XSsdYEFtPqmF12Jpmj0KdayvRvH277HOM64dP2RNUuORdOvItaw8zi4jaPULYi95usGJCm1gzNni7RAcdXF10epmBMZKFu4kMIM","attribution_segments":null,"supporting_websites":[],"refs":[{"turn_index":1,"ref_type":"view","ref_index":0}],"hue":null,"attributions":null}],"fallback_items":null},"showLoginRequiredCard":false}

Example data structure:

{
    "101": {
        "name": "Student Name",
        "marks": [
            85,
            90,
            78,
            88,
            92
        ]
    }
}

🔒 Input Validation

The application includes validation for:

Empty roll numbers

Duplicate roll numbers

Empty student names

Marks outside the 0–100 range

Non-numeric marks

Invalid menu selections

Searching for students that do not exist

🎯 Project Objectives

The main objectives of this project are to:

Demonstrate Python programming fundamentals.

Implement functions and modular program logic.

Work with dictionaries and lists.

Perform calculations and data processing.

Implement file handling using JSON.

Practice input validation and exception handling.

Build a practical menu-driven application.

🔮 Future Improvements

Possible improvements include:

✏️ Edit/update student records

🔐 User authentication

📊 Graphical representation of marks

📄 Export reports to PDF or CSV

🗄️ Database integration using SQLite/MySQL

🖥️ Graphical User Interface (GUI)

📱 Web-based student management portal

📧 Automated student report generation

📄 Project Report

The repository includes the project report:

Student_Management_System_Report.pdf

👨‍💻 Project

VITyarthi Student Management System

Developed as part of the VITyarthi academic project.

📜 License

This project is intended for educational and academic purposes.
