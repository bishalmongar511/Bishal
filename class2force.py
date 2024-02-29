print("Newton's second law of motion")
print("--------------------------------")

# determiming the missing value
print("1. Mass (m)")
print("2. Acceleration (a)")
print("3. Force (F)")
missing_value_choice = input("Enter the option number for the missing value: ")

# promote the user to enter the other two values
if missing_value_choice == "1":
    a = float(input("Enter acceleration (a):"))
    F = float(input("Enter force (F):"))
    m = F/a  
    print(f"mass (m) = {m}")
elif missing_value_choice == "2":
    m = float(input("Enter mass(a):"))
    F = float(input("Enter force (F): "))
    a = F/m 
    print(f"acceleration (a) = {a}")
elif missing_value_choice == "3":
    m = float(input("Enter mass (a)"))
    F = float(input("Enter acceleration (a): "))
    F = m*a 
    print(f"invalid force(f) = {f} ")
else:
    print("Invalid option selection for the missing value")
