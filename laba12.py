import json

def load_json_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

def save_json_file(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)

def display_json_content(file_name):
    data = load_json_file(file_name)
    print(json.dumps(data, indent=2))

def add_entry(file_name):
    school_type = input("Enter school type (school, college, technikum): ")
    num_pupils = int(input("Enter number of pupils: "))

    entry = {
        "type": school_type,
        "students": num_pupils
        # Додайте інші поля, якщо потрібно
    }

    data = load_json_file(file_name)
    data.append(entry)
    save_json_file(file_name, data)
    print("Entry added successfully.")

def delete_entry(file_name, entry_index):
    data = load_json_file(file_name)
    if 0 <= entry_index < len(data):
        del data[entry_index]
        save_json_file(file_name, data)
        print("Entry deleted successfully.")
    else:
        print("Invalid entry index.")

def search_by_field(file_name, field_name, field_value):
    data = load_json_file(file_name)
    results = [entry for entry in data if entry.get(field_name) == field_value]
    print("Search results:")
    print(json.dumps(results, indent=2))

def calculate_total_students(file_name):
    data = load_json_file(file_name)
    total_students = sum(entry.get("students", 0) for entry in data if entry.get("type") == "school")
    print(f"Total number of students in schools: {total_students}")

# Головна функція для діалогового режиму
def main():
    file_name = "data.json"  # Замініть на власний файл

    while True:
        print("\nMenu:")
        print("1. Display JSON content")
        print("2. Add new entry")
        print("3. Delete entry")
        print("4. Search by field")
        print("5. Calculate total number of students in schools")
        print("6. Save result to another JSON file")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            display_json_content(file_name)
        elif choice == "2":
            add_entry(file_name)
        elif choice == "3":
            entry_index = int(input("Enter the index of the entry to delete: "))
            delete_entry(file_name, entry_index)
        elif choice == "4":
            field_name = input("Enter the field name to search: ")
            field_value = input("Enter the field value to search: ")
            search_by_field(file_name, field_name, field_value)
        elif choice == "5":
            calculate_total_students(file_name)
        elif choice == "6":
            result_file_name = input("Enter the name of the result file: ")
            calculate_total_students(file_name)  # Виконати завдання
            save_json_file(result_file_name, load_json_file(file_name))
            print(f"Result saved to {result_file_name}")
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
