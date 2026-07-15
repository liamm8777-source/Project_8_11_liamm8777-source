"""
Program Name: Python Study Planner Tests
Author: Liam Malone
Purpose: Test the regular and priority study task classes.
Date: July 15, 2026
"""


# project two code added
import unittest

from study_task import PriorityStudyTask, StudyTask


class StudyTaskTests(unittest.TestCase):
   

    def test_regular_task_starts_incomplete(self):
        
        study_task = StudyTask(
            "Finish homework",
            "Python"
        )

        self.assertFalse(
            study_task.study_task_complete
        )

    def test_regular_task_can_be_completed(self):
        
        study_task = StudyTask(
            "Finish homework",
            "Python"
        )

        study_task.mark_study_task_complete()

        self.assertTrue(
            study_task.study_task_complete
        )

    def test_regular_task_description(self):
       
        study_task = StudyTask(
            "Read Chapter 11",
            "Python"
        )

        expected_description = (
            "Read Chapter 11 - Python - Not Complete"
        )

        self.assertEqual(
            study_task.get_study_task_description(),
            expected_description
        )

    def test_priority_task_uses_inheritance(self):
        
        priority_task = PriorityStudyTask(
            "Finish final project",
            "Python",
            "High"
        )

        self.assertIsInstance(
            priority_task,
            StudyTask
        )

        self.assertEqual(
            priority_task.priority_level,
            "High"
        )

    def test_priority_task_description(self):
        
        priority_task = PriorityStudyTask(
            "Study for exam",
            "Python",
            "High"
        )

        expected_description = (
            "Study for exam - Python - "
            "Not Complete - Priority: High"
        )

        self.assertEqual(
            priority_task.get_study_task_description(),
            expected_description
        )


if __name__ == "__main__":
    unittest.main()