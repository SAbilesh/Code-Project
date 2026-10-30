# Menu-Driven Student Information System
student = {}

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    student[roll] = {"Name": name, "Department": dept}
    print("Student Added Successfully")

def view_student():
    if not student:
        print("No Student Records Found")
        return
    
    print("\n--- Student Records ---")
    for roll, data in student.items():
        print("Roll No:", roll)
        print("Name:", data["Name"])
        print("Department:", data["Department"])
        print("-" * 20)

def search_student():
    roll = input("Enter Roll No to search: ")
    if roll in student:
        print(f"Roll No: {roll}, Name: {student[roll]['Name']}, Department: {student[roll]['Department']}")
    else:
        print("Student not found")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    if roll in student:
        del student[roll]
        print("Student Deleted Successfully")
    else:
        print("Student not found")

# Main Program Loop
while True:
    print("\n1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid Choice")