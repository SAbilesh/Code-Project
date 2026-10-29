#Student Marks,Percentage and Grade
name=input("Enter Student Name: ")
n=int(input("Enter Number of Subjects: "))
total=0
for i in range(1,n+1):
    marks=float(input(f"Enter Marks for Subject {i}: "))
    total+=marks
percentage=total/n
if percentage>=90:
    grade="A+"
    performance="Outstanding"
elif percentage>=80:
    grade="A"
    performance="Excellent"
elif percentage>=70:
    grade="B"
    performance="Very Good"
elif percentage>=60:
    grade="C"
    performance="Good"
elif percentage>=50:
    grade="D"
    performance="Average"
else:
    grade="F"
    performance="Needs Improvement"
print("\n---Academic Performance---")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Performance:", performance)
