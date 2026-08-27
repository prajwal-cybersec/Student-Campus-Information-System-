# =========================================================
# SMART CAMPUS INFORMATION SYSTEM
# =========================================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# GLOBAL LIST
# =========================================================

students = []

# =========================================================
# MODULE 1 : ADD STUDENT
# =========================================================

def add_student():

    print("\n===== ADD STUDENT =====")

    student_id = input("Enter Student ID: ")

    if not student_id.isalnum():

        print("Invalid Student ID!")
        return

    name = input("Enter Student Name: ")

    age = int(input("Enter Age: "))

    score = float(
        input("Enter Exam Score (0-100): ")
    )

    total_fee = float(
        input("Enter Total Fee: ")
    )

    paid_fee = float(
        input("Enter Paid Fee: ")
    )

    remaining_fee = total_fee - paid_fee

    # Grade Calculation

    if score >= 90:

        grade = "A"
        remark = "Excellent"

    elif score >= 75:

        grade = "B"
        remark = "Very Good"

    elif score >= 60:

        grade = "C"
        remark = "Good"

    elif score >= 40:

        grade = "D"
        remark = "Average"

    else:

        grade = "F"
        remark = "Fail"

    # Store Student Data

    student = {

        "id": student_id,
        "name": name,
        "age": age,
        "score": score,
        "grade": grade,
        "remark": remark,
        "total_fee": total_fee,
        "paid_fee": paid_fee,
        "remaining_fee": remaining_fee,
        "courses": []
    }

    students.append(student)

    print("\nStudent Added Successfully!")

# =========================================================
# MODULE 2 : DISPLAY STUDENT
# =========================================================

def display_students():

    print("\n===== DISPLAY STUDENT =====")

    sid = input("Enter Student ID: ")

    found = False

    for student in students:

        if student["id"] == sid:

            found = True

            print("\n================================")
            print("        STUDENT DETAILS")
            print("================================")

            print("Student ID    :", student["id"])
            print("Name          :", student["name"])
            print("Age           :", student["age"])
            print("Score         :", student["score"])
            print("Grade         :", student["grade"])
            print("Remark        :", student["remark"])

            print("\n========== FEE DETAILS ==========")

            print("Total Fee     :",
                  student["total_fee"])

            print("Paid Fee      :",
                  student["paid_fee"])

            print("Remaining Fee :",
                  student["remaining_fee"])

            print("\n=========== COURSES ===========")

            if len(student["courses"]) == 0:

                print("No Courses Enrolled")

            else:

                for course in student["courses"]:

                    print(
                        "-",
                        course["course_name"],
                        "| Credits:",
                        course["credits"]
                    )

    if not found:

        print("\nStudent Not Found!")

# =========================================================
# MODULE 3 : COURSE ENROLLMENT
# =========================================================

def enroll_course():

    print("\n===== COURSE ENROLLMENT =====")

    sid = input("Enter Student ID: ")

    found = False

    for student in students:

        if student["id"] == sid:

            found = True

            max_courses = 5

            while True:

                if len(student["courses"]) >= max_courses:

                    print(
                        "Maximum Course Limit Reached!"
                    )

                    break

                course_name = input(
                    "Enter Course Name (or done): "
                )

                if course_name.lower() == "done":

                    break

                credits = int(
                    input("Enter Course Credits: ")
                )

                course = {

                    "course_name": course_name,
                    "credits": credits
                }

                student["courses"].append(course)

                print("Course Added Successfully!")

    if not found:

        print("Student Not Found!")

# =========================================================
# MODULE 4 : SEARCH STUDENT
# =========================================================

def search_student():

    print("\n===== SEARCH STUDENT =====")

    sid = input(
        "Enter Student ID to Search: "
    )

    found = False

    for student in students:

        if student["id"] == sid:

            found = True

            print("\nStudent Found!")

            print("Name  :",
                  student["name"])

            print("Grade :",
                  student["grade"])

    if not found:

        print("Student Not Found!")

# =========================================================
# MODULE 5 : SORT STUDENTS
# =========================================================

def sort_students():

    print("\n===== SORT STUDENTS =====")

    if len(students) == 0:

        print("No Students Available.")
        return

    sorted_students = sorted(
        students,
        key=lambda x: x["name"]
    )

    print("\n===== SORTED STUDENTS =====")

    for student in sorted_students:

        print(
            student["name"],
            "-",
            student["id"]
        )

# =========================================================
# MODULE 6 : UPDATE FEES
# =========================================================

def update_fee():

    print("\n===== UPDATE FEES =====")

    sid = input("Enter Student ID: ")

    found = False

    for student in students:

        if student["id"] == sid:

            found = True

            print("\nStudent Name :",
                  student["name"])

            extra_payment = float(
                input("Enter Amount Paid: ")
            )

            student["paid_fee"] += extra_payment

            student["remaining_fee"] = (

                student["total_fee"]
                - student["paid_fee"]
            )

            print("\nFee Updated Successfully!")

            print("Total Fee     :",
                  student["total_fee"])

            print("Paid Fee      :",
                  student["paid_fee"])

            print("Remaining Fee :",
                  student["remaining_fee"])

    if not found:

        print("Student Not Found!")

# =========================================================
# MODULE 7 : SAVE RECORDS TO FILE
# =========================================================

def save_to_file():

    with open(
        "student_records.txt",
        "w"
    ) as file:

        for student in students:

            file.write(

                f"{student['id']},"
                f"{student['name']},"
                f"{student['age']},"
                f"{student['score']},"
                f"{student['grade']},"
                f"{student['total_fee']},"
                f"{student['paid_fee']},"
                f"{student['remaining_fee']},"
                f"{student['courses']}\n"
            )

    print("\nRecords Saved Successfully!")

# =========================================================
# MODULE 8 : READ RECORDS FROM FILE
# =========================================================

def read_from_file():

    print("\n===== FILE RECORDS =====")

    try:

        with open(
            "student_records.txt",
            "r"
        ) as file:

            data = file.readlines()

            for line in data:

                print(line.strip())

    except FileNotFoundError:

        print("File Not Found!")

# =========================================================
# MODULE 9 : DIRECTORY SCANNING
# =========================================================

class EmptyFolderError(Exception):

    pass

def scan_directory():

    print("\n===== DIRECTORY SCANNING =====")

    path = input(
        "Enter Directory Path: "
    )

    try:

        if not os.path.exists(path):

            raise FileNotFoundError(
                "Invalid Directory Path!"
            )

        for root, dirs, files in os.walk(path):

            level = root.replace(
                path,
                ""
            ).count(os.sep)

            indent = " " * 4 * level

            print(
                f"{indent}"
                f"{os.path.basename(root)}/"
            )

            sub_indent = " " * 4 * (
                level + 1
            )

            for f in files:

                print(f"{sub_indent}{f}")

            if not files and not dirs:

                raise EmptyFolderError(

                    f"Empty Folder Found: {root}"
                )

    except FileNotFoundError as e:

        print("Error :", e)

    except EmptyFolderError as e:

        print("Custom Error :", e)

    except Exception as e:

        print("Unexpected Error :", e)

# =========================================================
# MODULE 10 : PERFORMANCE ANALYSIS
# =========================================================

def performance_analysis():

    print("\n===== PERFORMANCE ANALYSIS =====")

    if len(students) == 0:

        print("No Student Data Available.")
        return

    names = []
    scores = []

    for student in students:

        names.append(student["name"])
        scores.append(student["score"])

    df = pd.DataFrame({

        "Name": names,
        "Score": scores
    })

    print("\n===== STUDENT DATA =====")

    print(df)

    arr = np.array(scores)

    print("\n===== ANALYSIS =====")

    print("Mean Score :", np.mean(arr))
    print("Highest    :", np.max(arr))
    print("Lowest     :", np.min(arr))
    print("Median     :", np.median(arr))
    print("Std Dev    :", np.std(arr))

    plt.bar(names, scores)

    plt.title(
        "Student Performance Analysis"
    )

    plt.xlabel("Student Name")

    plt.ylabel("Score")

    plt.show()

# =========================================================
# MAIN MENU
# =========================================================

def main():

    while True:

        print("\n===================================")

        print(
            " SMART CAMPUS INFORMATION SYSTEM"
        )

        print("===================================")

        print("1. Add Student")
        print("2. Display Student")
        print("3. Course Enrollment")
        print("4. Search Student")
        print("5. Sort Students")
        print("6. Update Fees")
        print("7. Save Records to File")
        print("8. Read Records from File")
        print("9. Directory Scanning")
        print("10. Performance Analysis")
        print("11. Exit")

        choice = input(
            "\nEnter Your Choice: "
        )

        if choice == "1":

            add_student()

        elif choice == "2":

            display_students()

        elif choice == "3":

            enroll_course()

        elif choice == "4":

            search_student()

        elif choice == "5":

            sort_students()

        elif choice == "6":

            update_fee()

        elif choice == "7":

            save_to_file()

        elif choice == "8":

            read_from_file()

        elif choice == "9":

            scan_directory()

        elif choice == "10":

            performance_analysis()

        elif choice == "11":

            print("\nExiting Program...")

            break

        else:

            print("\nInvalid Choice!")

# =========================================================
# PROGRAM STARTS HERE
# =========================================================

main()
