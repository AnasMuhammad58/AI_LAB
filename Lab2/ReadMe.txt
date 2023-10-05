# Initialize an empty list to store the dictionaries
student_records = []

def display_records(records):
    print("\nList of student records:")
    for idx, student in enumerate(records, start=1):
        print(f"Record {idx}:")
        for key, value in student.items():
            print(f"{key}: {value}")
        print()

def add_record():
    registration_number = input("Registration Number: ")
    name = input("Name: ")
    email = input("Email: ")
    gender = input("Gender: ")

    student_dict = {
        'Registration Number': registration_number,
        'Name': name,
        'Email': email,
        'Gender': gender
    }

    student_records.append(student_dict)
    print("Record added successfully!")

def update_record():
    display_records(student_records)
    record_to_update = int(input("Enter the record number you want to update: ")) - 1

    if 0 <= record_to_update < len(student_records):
        print("Enter new details for the student:")
        registration_number = input("Registration Number: ")
        name = input("Name: ")
        email = input("Email: ")
        gender = input("Gender: ")

        student_records[record_to_update] = {
            'Registration Number': registration_number,
            'Name': name,
            'Email': email,
            'Gender': gender
        }
        print("Record updated successfully!")
    else:
        print("Invalid record number.")

def delete_record():
    display_records(student_records)
    record_to_delete = int(input("Enter the record number you want to delete: ")) - 1

    if 0 <= record_to_delete < len(student_records):
        deleted_record = student_records.pop(record_to_delete)
        print(f"Record deleted successfully:\n{deleted_record}")
    else:
        print("Invalid record number.")

while True:
    print("\nOptions:")
    print("1. Add a new record")
    print("2. Update a record")
    print("3. Delete a record")
    print("4. Display all records")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        add_record()
    elif choice == '2':
        update_record()
    elif choice == '3':
        delete_record()
    elif choice == '4':
        display_records(student_records)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
