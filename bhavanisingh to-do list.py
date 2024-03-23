# Function to display the current to-do list
def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to add a task to the to-do list
def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to your to-do list.")

# Function to delete a task from the to-do list
def delete_task(todo_list, task_number):
    if 1 <= task_number <= len(todo_list):
        deleted_task = todo_list.pop(task_number - 1)
        print(f"Task '{deleted_task}' deleted from your to-do list.")
    else:
        print("Invalid task number. Please try again.")

# Main function to run the to-do list application
def main():
    todo_list = []

    while True:
        print("\nOptions:")
        print("1. Display to-do list")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            task = input("Enter the task to add: ")
            add_task(todo_list, task)
        elif choice == "3":
            task_number = int(input("Enter the task number to delete: "))
            delete_task(todo_list, task_number)
        elif choice == "4":
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
