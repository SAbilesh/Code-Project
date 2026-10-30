import csv
students=[
    {"RollNo":"101", "Name":"Anitha", "Department":"CSE","Mark":"86"},
    {"RollNo":"102","Name":"Bala","Department":"CSE","Mark":"91"},
    {"RollNo":"103","Name":"Chitra","Department":"ECE","Mark":"78"},
]
#Tuple example:fixed course details
course=("Python",4)
print("Course Name:",course)
with open("students.txt","w") as file:
    for student in students:
        file.write(str(student)+"\n")
with open("student.csv","w",newline="") as file:
    fieldnames=["RollNo","Name","Department","Mark"]
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)
    print("\n---Records from CSV---")
with open("student.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row["RollNo"],row["Name"],row["Department"],row["Mark"])
