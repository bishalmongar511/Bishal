num_students = int(input("Enter the number of the studens: "))
 
i = 1
while i <= num_students:
    total_grade = 0
    num_subjects = int(input("Enter the number of subject for student{i}: "))

    for j in range(1, num_subjects +1): 
        grade = float(input(f"Enter subject {j} grade for student {i}: "))
        total_grade += grade


avrage_grade = total_grade/ num_subjects
print(f"Avrage grade for student {i}: {avrage_grade:.2f}")
i += 1 




