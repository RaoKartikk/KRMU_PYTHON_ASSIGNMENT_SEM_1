import csv
import os

#Name Kartik         
#Roll no 2501730166
# Assignment 2 

def get_manual_input():
    marks = {}
    print("\n--- Manual Data Entry ---")
    print("Type 'done' to finish.")
    
    while True:
        name = input("Enter Student Name: ").strip()
        
        if name.lower() == 'done':
            break
        
        try:
            score = float(input(f"Enter marks for {name}: "))
            marks[name] = score
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    return marks

def load_csv_data(filename):
    marks = {}
    
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return marks

    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader, None)
            
            for row in reader:
                if len(row) >= 2:
                    name = row[0].strip()
                    try:
                        score = float(row[1].strip())
                        marks[name] = score
                    except ValueError:
                        continue
        
        print(f"Loaded {len(marks)} students from {filename}.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    return marks

def append_student_record(filename):
    name = input("Enter new student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        score = float(input("Enter marks: ").strip())
    except ValueError:
        print("Invalid marks.")
        return

    file_exists = os.path.exists(filename)
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow(['Name', 'Marks'])
            
        writer.writerow([name, score])
        
    print(f"Added {name} to {filename}.")

def calculate_average(marks_dict):
    scores = list(marks_dict.values())
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def find_max_score(student_scores):
    if not student_scores:
        return
        
    max_score = -1
    max_student = ""

    for name, score in student_scores.items():
        if score > max_score:
            max_score = score
            max_student = name
            
    print(f"HIGHEST SCORE: {max_score} by {max_student}")

def find_min_score(student_scores):
    if not student_scores:
        return
        
    min_score = 101
    min_student = ""

    for name, score in student_scores.items():
        if score < min_score:
            min_score = score
            min_student = name
            
    print(f"LOWEST SCORE:  {min_score} by {min_student}")

def assign_grades(student_scores):
    grades = {}
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for name, score in student_scores.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        
        grades[name] = grade
        distribution[grade] += 1
        
    return grades, distribution

def print_summary(student_scores, grades):
    passed = [name for name, score in student_scores.items() if score >= 40]
    failed = [name for name, score in student_scores.items() if score < 40]
    
    print("\n--- Class Statistics ---")
    avg = calculate_average(student_scores)
    print(f"Average Score: {avg:.2f}")
    
    find_max_score(student_scores)
    find_min_score(student_scores)
    
    _, final_dist = assign_grades(student_scores)
    print(f"Grade Counts:  {final_dist}")
    
    print(f"Passed: {len(passed)} students")
    print(f"Failed: {len(failed)} students")
    
    print("\n" + "="*40)
    print(f"{'Name':<20} | {'Marks':<10} | {'Grade':<5}")
    print("-" * 40)
    
    for name, score in student_scores.items():
        grade = grades[name]
        print(f"{name:<20} | {score:<10.1f} | {grade:<5}")
    print("="*40)

def main():
    print("\n=== GRADEBOOK ANALYZER ===")
    
    while True:
        print("\n1. Manual Entry")
        print("2. Load from CSV")
        print("3. Add Student to CSV")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        student_scores = {}

        if choice == '1':
            student_scores = get_manual_input()
            
        elif choice == '2':
            filename = input("Enter CSV filename: ")
            student_scores = load_csv_data(filename)
            
        elif choice == '3':
            filename = input("Enter CSV filename: ")
            append_student_record(filename)
            student_scores = load_csv_data(filename)
            
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Try again.")
            continue

        if student_scores:
            final_grades, _ = assign_grades(student_scores)
            print_summary(student_scores, final_grades)
        else:
            if choice in ['1', '2', '3']:
                print("No data loaded.")

if __name__ == "__main__":
    main()
