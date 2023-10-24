def display_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value[0]} students, {value[1]}")

def add_entry(dictionary, name, students, school_type):
    dictionary[name] = (students, school_type)
    print(f"Added entry: {name}: {students} students, {school_type}")

def delete_entry(dictionary, name):
    if name in dictionary:
        del dictionary[name]
        print(f"Deleted entry: {name}")
    else:
        print(f"Entry '{name}' not found in the dictionary.")

def view_sorted_keys(dictionary):
    sorted_keys = sorted(dictionary.keys())
    for key in sorted_keys:
        print(f"{key}: {dictionary[key][0]} students, {dictionary[key][1]}")

def calculate_total_students(dictionary):
    total_students = sum(students for students, school_type in dictionary.values() if school_type == "school")
    print(f"Total number of students in schools: {total_students}")

def main():
    institution_data = {
        "School A": (123, "school"),
        "School B": (234, "college"),
        "School C": (345, "school"),
        "School D": (456, "college"),
        "School E": (567, "school"),
        "School F": (678, "techikum"),
    }

    while True:
        print("\nMenu:")
        print("1. Display dictionary values")
        print("2. Add an entry")
        print("3. Delete an entry")
        print("4. View dictionary contents by sorted keys")
        print("5. Calculate total number of students in schools")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_dictionary(institution_data)
        elif choice == "2":
            name = input("Enter the name of the institution: ")
            students = int(input("Enter the number of students: "))
            school_type = input("Enter the type of institution (school/college/technikum): ")
            add_entry(institution_data, name, students, school_type)
        elif choice == "3":
            name = input("Enter the name of the institution to delete: ")
            delete_entry(institution_data, name)
        elif choice == "4":
            view_sorted_keys(institution_data)
        elif choice == "5":
            calculate_total_students(institution_data)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
