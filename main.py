"""
Program Name: Python Study Planner
Author: Liam Malone
Purpose: A command-line study planner that lets users add, view, complete,
delete, save, and load school tasks.
Resources Used: Original Project One Python Study Planner and
Date: June 25, 2026
Updated: July 15, 2026
"""


# project two code added
from planner_manager import StudyPlannerManager
from study_storage import load_study_tasks, save_study_tasks
from study_task import PriorityStudyTask, StudyTask


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


# project two code added
def add_study_task(study_planner):
    """Add a regular or priority task to the planner."""
    study_task_name = input("Enter the task name: ")
    study_task_subject = input("Enter the subject: ")

    priority_answer = input(
        "Is this a priority task? (y/n): "
    ).lower()

    if priority_answer == "y":
        priority_level = input(
            "Enter the priority level "
            "(Low, Medium, or High): "
        ).title()

        if priority_level not in ("Low", "Medium", "High"):
            print(
                "Invalid priority level. "
                "Medium will be used."
            )
            priority_level = "Medium"

        new_study_task = PriorityStudyTask(
            study_task_name,
            study_task_subject,
            priority_level
        )
    else:
        new_study_task = StudyTask(
            study_task_name,
            study_task_subject
        )

    study_planner.add_study_task(new_study_task)

    save_study_tasks(
        study_planner.get_all_study_tasks()
    )

    print("Task added successfully.")


# project two code added
def view_study_tasks(study_planner):
    """Display all study tasks in the planner."""
    study_tasks = study_planner.get_all_study_tasks()

    if len(study_tasks) == 0:
        print("There are no tasks yet.")
    else:
        print()
        print("Current Tasks:")

        task_number = 1

        for study_task in study_tasks:
            print(
                f"{task_number}. "
                f"{study_task.get_study_task_description()}"
            )

            task_number += 1


# project two code added
def get_task_index_from_user(
    study_planner,
    action_name
):
    """Get a valid task number and return its index."""
    if study_planner.get_study_task_count() == 0:
        print("There are no tasks to choose from.")
        return None

    view_study_tasks(study_planner)

    task_choice = input(
        f"Enter the task number to {action_name}: "
    )

    try:
        task_number = int(task_choice)
    except ValueError:
        print("Please enter a number.")
        return None

    if (
        task_number < 1
        or task_number
        > study_planner.get_study_task_count()
    ):
        print("That task number does not exist.")
        return None

    return task_number - 1


# project two code added
def mark_study_task_complete(study_planner):
    """Mark one study task as complete."""
    study_task_index = get_task_index_from_user(
        study_planner,
        "mark complete"
    )

    if study_task_index is not None:
        study_planner.complete_study_task(
            study_task_index
        )

        save_study_tasks(
            study_planner.get_all_study_tasks()
        )

        print("Task marked as complete.")


# project two code added
def delete_study_task(study_planner):
    """Delete one study task from the planner."""
    study_task_index = get_task_index_from_user(
        study_planner,
        "delete"
    )

    if study_task_index is not None:
        removed_study_task = (
            study_planner.delete_study_task(
                study_task_index
            )
        )

        save_study_tasks(
            study_planner.get_all_study_tasks()
        )

        print(
            "Deleted task: "
            f"{removed_study_task.study_task_name}"
        )


# project two code added
def view_study_progress(study_planner):
    
    total_study_tasks = (
        study_planner.get_study_task_count()
    )

    completed_study_tasks = (
        study_planner
        .get_completed_study_task_count()
    )

    print()
    print("Study Progress")
    print(
        f"Completed tasks: {completed_study_tasks}"
    )
    print(f"Total tasks: {total_study_tasks}")

    if total_study_tasks > 0:
        print(
            f"You have completed "
            f"{completed_study_tasks} out of "
            f"{total_study_tasks} tasks."
        )
    else:
        print(
            "Add a task to start tracking "
            "your progress."
        )


# project two code added
def run_python_study_planner():
    """Load saved tasks and run the study planner."""
    loaded_study_tasks = load_study_tasks()

    study_planner = StudyPlannerManager(
        loaded_study_tasks
    )

    menu_choices = ("1", "2", "3", "4", "5", "6")
    program_is_running = True

    display_study_planner_title()

    while program_is_running:
        display_study_planner_menu()
        user_choice = input("Choose an option: ")

        if user_choice == "1":
            add_study_task(study_planner)

        elif user_choice == "2":
            view_study_tasks(study_planner)

        elif user_choice == "3":
            mark_study_task_complete(
                study_planner
            )

        elif user_choice == "4":
            delete_study_task(study_planner)

        elif user_choice == "5":
            view_study_progress(study_planner)

        elif user_choice == "6":
            save_study_tasks(
                study_planner.get_all_study_tasks()
            )

            print(
                "Thank you for using "
                "Python Study Planner."
            )

            program_is_running = False

        elif user_choice not in menu_choices:
            print(
                "Invalid choice. "
                "Please choose a number from 1 to 6."
            )


# project two code added
if __name__ == "__main__":
    run_python_study_planner()