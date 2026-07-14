"""
Program Name: Python Study Planner
Author: Liam Malone
Purpose: A command-line study planner that will let users add, view, complete, and delete school tasks.
Date: June 25 2026
"""
def display_study_planner_title():
    """Display the title of the Python Study Planner."""
    print()
    print("Python Study Planner")
   


def display_study_planner_menu():
    """Display the main menu choices for the user."""
    print()
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task complete")
    print("4. Delete a task")
    print("5. View progress")
    print("6. Quit")


def add_study_task(study_tasks):
    """Add a new study task to the task list."""
    task_name = input("Enter the task name: ")
    task_subject = input("Enter the subject: ")

    new_task = {
        "name": task_name,
        "subject": task_subject,
        "complete": False
    }

    study_tasks.append(new_task)
    print("Task added successfully.")


def view_study_tasks(study_tasks):
    """Display all study tasks in the task list."""
    if len(study_tasks) == 0:
        print("There are no tasks yet.")
    else:
        print()
        print("Current Tasks:")

        task_number = 1

        for task in study_tasks:
            if task["complete"]:
                task_status = "Complete"
            else:
                task_status = "Not Complete"

            print(f"{task_number}. {task['name']} - {task['subject']} - {task_status}")
            task_number += 1


def get_task_index_from_user(study_tasks, action_name):
    """Get a valid task number from the user and return the task index."""
    if len(study_tasks) == 0:
        print("There are no tasks to choose from.")
        return None

    view_study_tasks(study_tasks)

    task_choice = input(f"Enter the task number to {action_name}: ")

    if not task_choice.isdigit():
        print("Please enter a number.")
        return None

    task_number = int(task_choice)

    if task_number < 1 or task_number > len(study_tasks):
        print("That task number does not exist.")
        return None

    return task_number - 1


def mark_study_task_complete(study_tasks):
    """Mark one study task as complete."""
    task_index = get_task_index_from_user(study_tasks, "mark complete")

    if task_index is not None:
        study_tasks[task_index]["complete"] = True
        print("Task marked as complete.")


def delete_study_task(study_tasks):
    """Delete one study task from the task list."""
    task_index = get_task_index_from_user(study_tasks, "delete")

    if task_index is not None:
        removed_task = study_tasks.pop(task_index)
        print(f"Deleted task: {removed_task['name']}")


def view_study_progress(study_tasks):
    """Display how many study tasks are complete."""
    total_tasks = len(study_tasks)
    completed_tasks = 0

    for task in study_tasks:
        if task["complete"]:
            completed_tasks += 1

    print()
    print("Study Progress")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Total tasks: {total_tasks}")

    if total_tasks > 0:
        print(f"You have completed {completed_tasks} out of {total_tasks} tasks.")
    else:
        print("Add a task to start tracking your progress.")


def run_python_study_planner():
    """Run the main Python Study Planner program."""
    study_tasks = []
    menu_choices = ("1", "2", "3", "4", "5", "6")
    program_is_running = True

    display_study_planner_title()

    while program_is_running:
        display_study_planner_menu()
        user_choice = input("Choose an option: ")

        if user_choice == "1":
            add_study_task(study_tasks)
        elif user_choice == "2":
            view_study_tasks(study_tasks)
        elif user_choice == "3":
            mark_study_task_complete(study_tasks)
        elif user_choice == "4":
            delete_study_task(study_tasks)
        elif user_choice == "5":
            view_study_progress(study_tasks)
        elif user_choice == "6":
            print("Thank you for using Python Study Planner.")
            program_is_running = False
        elif user_choice not in menu_choices:
            print("Invalid choice. Please choose a number from 1 to 6.")


run_python_study_planner()