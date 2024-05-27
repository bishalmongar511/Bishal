student_list = []
student_dict = {}

name = input("Enter your name: ")
Age = input("Enter your age: ")
Grade = input("Enter your grade: ")

student_list.append(name)
student_dict[name] = {"Age": Age, "Grade": Grade}

print("Studet information added sucessfully! ")
print(student_dict.items())

search_name = input("Enter the name to search:")
if search_name in student_list:
    print(f"student found: {student_dict[search_name]}")

else:
    print("Student not found!")

remove_name = input("Enter the name to remove: ")
if remove_name in student_list:
    student_list.remove(remove_name)
    del student_dict[name]
    print("Student name removed sucessfully!")
    

else:
    print("Student name not found!")