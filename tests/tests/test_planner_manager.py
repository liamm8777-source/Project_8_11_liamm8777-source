"""
Program Name: Python Study Planner Tests
Author: Liam Malone
Purpose: Test the StudyPlannerManager class.
Date: July 15, 2026
"""


# project two code added
import unittest

from planner_manager import StudyPlannerManager
from study_task import StudyTask


class StudyPlannerManagerTests(unittest.TestCase):
    
    def setUp(self):
       
        self.study_planner = StudyPlannerManager()

        self.study_task = StudyTask(
            "Complete homework",
            "Python"
        )

    def test_study_task_can_be_added(self):
       
        self.study_planner.add_study_task(
            self.study_task
        )

        self.assertEqual(
            self.study_planner.get_study_task_count(),
            1
        )

    def test_study_task_can_be_completed(self):
        
        self.study_planner.add_study_task(
            self.study_task
        )

        self.study_planner.complete_study_task(0)

        self.assertTrue(
            self.study_task.study_task_complete
        )

        self.assertEqual(
            self.study_planner
            .get_completed_study_task_count(),
            1
        )

    def test_study_task_can_be_deleted(self):
       
        self.study_planner.add_study_task(
            self.study_task
        )

        removed_study_task = (
            self.study_planner.delete_study_task(0)
        )

        self.assertEqual(
            removed_study_task.study_task_name,
            "Complete homework"
        )

        self.assertEqual(
            self.study_planner.get_study_task_count(),
            0
        )


if __name__ == "__main__":
    unittest.main()