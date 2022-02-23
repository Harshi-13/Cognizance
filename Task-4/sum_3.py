# Question-3
# Write a python program to make a 2-dimensional list that contains represents a table of records,
# for instance, student details like Roll no, Student Name, Marks; And complete the following 2 sub-tasks.
# i) Add some records in the list and print the list in tabular form,

# Entering own names and values
student_details = {1: [1, 'Harshita',90],
2: [2,'Jayashri',80],
3: [3, 'Satish',70] }
print("(i)")
print ("{:<8} {:<15} {:<10} ".format('Roll No','Name','Marks'))
for ctr, student_record in student_details.items():
    rollno, name, marks = student_record
    print ("{:<8} {:<15} {:<10} ".format(rollno, name, marks))

# ii) From created list, extract and print second record/row that contains
print("(ii)")
print("{:<8} {:<15} {:<10} ".format(student_details[2][0],student_details[2][1],student_details[2][2]))