"""
Program Name: Python Study Planner
Author: Liam Malone
Purpose: Save and load study tasks using a JSON file.
Resources Used: Original Project One Python Study Planner and
Date: July 15, 2026
"""


# project two code added
import json
from pathlib import Path

from study_task import create_study_task_from_dictionary


# project two code added
STUDY_TASK_FILE = Path("study_tasks.json")


# project two code added
def save_study_tasks(
    study_tasks,
    file_path=STUDY_TASK_FILE
):
    """Save all study tasks to a JSON file."""
    study_task_dictionaries = []

    for study_task in study_tasks:
        study_task_dictionaries.append(
            study_task.convert_study_task_to_dictionary()
        )

    try:
        file_path = Path(file_path)

        file_path.write_text(
            json.dumps(
                study_task_dictionaries,
                indent=4
            ),
            encoding="utf-8"
        )

        return True

    except OSError:
        print("The study tasks could not be saved.")
        return False



def load_study_tasks(file_path=STUDY_TASK_FILE):
    
    file_path = Path(file_path)

    if not file_path.exists():
        return []

    try:
        saved_task_information = json.loads(
            file_path.read_text(
                encoding="utf-8"
            )
        )

        loaded_study_tasks = []

        for task_dictionary in saved_task_information:
            loaded_study_tasks.append(
                create_study_task_from_dictionary(
                    task_dictionary
                )
            )

        return loaded_study_tasks

    except (
        OSError,
        json.JSONDecodeError,
        KeyError,
        TypeError
    ):
        print(
            "The saved task file could not be loaded. "
            "A new task list will be used."
        )

        return []