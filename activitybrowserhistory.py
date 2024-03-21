from queue import Queue
patient_queue = Queue()


while True:
    print("\n---- Patient Registration and Appointment Scheduling System ----")
    print("1. Register Patient")
    print("2. Remove Patient after Meeting Doctor")
    print("3. Display Patient Queue")
    print("4. Exit")

    choice = input("Enter your choice: ")

    
    if choice == '1':
        patient_name = input("Enter patient name: ")
        patient_queue.put(patient_name)
        print(f"Patient {patient_name} registered successfully.")

    
    elif choice == '2':
        if patient_queue.empty():
            print("No patients in the queue.")
        else:
            removed_patient = patient_queue.get()
            print(f"Patient {removed_patient} removed after meeting the doctor.")

    
    elif choice == '3':
       
        if patient_queue.empty():
          print("No patients in the queue.")
        else:
          print("Current Patient Queue:")
          for patient in patient_queue.queue:
              print(patient)


    # Exit the program
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break

    # Handle invalid choices
    else:
        print("Invalid choice. Please enter a valid option.")
