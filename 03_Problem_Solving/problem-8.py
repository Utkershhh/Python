n1 = int(input("Enter marks of subject1: "))
n2 = int(input("Enter marks of subject2: "))
n3 = int(input("Enter marks of subject3: "))
n4 = int(input("Enter marks of subject4: "))
n6 = int(input("Enter marks of subject5: "))
n5 = int(input("Enter marks of subject6: "))

marks = [n1, n2, n3, n4, n5, n6]
marks.sort()
marks_avg = (n1+n2+n3+n4+n5)/5
print(marks)
print("Average marks of the student = ", marks_avg)