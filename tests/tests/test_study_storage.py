"""
Program Name: Python Study Planner Tests
Author: Liam Malone
Purpose: Test saving and loading study tasks with JSON.
Date: July 15, 2026
"""


# project two code added
import tempfile
import unittest
from pathlib import Path

from study_storage import (
    load_study_tasks,
    save_study_tasks
)

from study_task import PriorityStudyTask, StudyTask


class StudyStorageTests(unittest.TestCase):
   

    def test_regular_task_can_be_saved_and_loaded(self):
        
        with tempfile.TemporaryDirectory() as folder:
            test_file = Path(folder) / "test_tasks.json"

            original_tasks = [
                StudyTask(
                    "Read Chapter 10",
                    "Python"
                )
            ]

            save_result = save_study_tasks(
                original_tasks,
                test_file
            )

            loaded_tasks = load_study_tasks(
                test_file
            )

            self.assertTrue(save_result)

            self.assertEqual(
                len(loaded_tasks),
                1
            )

            self.assertEqual(
                loaded_tasks[0].study_task_name,
                "Read Chapter 10"
            )

            self.assertEqual(
                loaded_tasks[0].study_task_subject,
                "Python"
            )

    def test_priority_task_can_be_saved_and_loaded(self):
        
        with tempfile.TemporaryDirectory() as folder:
            test_file = Path(folder) / "test_tasks.json"

            original_tasks = [
                PriorityStudyTask(
                    "Finish final project",
                    "Python",
                    "High"
                )
            ]

            save_study_tasks(
                original_tasks,
                test_file
            )

            loaded_tasks = load_study_tasks(
                test_file
            )

            self.assertEqual(
                len(loaded_tasks),
                1
            )

            self.assertIsInstance(
                loaded_tasks[0],
                PriorityStudyTask
            )

            self.assertEqual(
                loaded_tasks[0].priority_level,
                "High"
            )

    def test_missing_file_returns_empty_list(self):
       
        with tempfile.TemporaryDirectory() as folder:
            missing_file = (
                Path(folder) / "missing_tasks.json"
            )

            loaded_tasks = load_study_tasks(
                missing_file
            )

            self.assertEqual(
                loaded_tasks,
                []
            )


if __name__ == "__main__":
    unittest.main()