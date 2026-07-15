"""
Program Name: Python Study Planner
Author: Liam Malone
Purpose: Manage the collection of study tasks in the planner.
Resources Used: Original Project One Python Study Planner and
Python Crash Course Chapter 9.
Date: July 14, 2026
"""


# project two code added
class StudyPlannerManager:
  

    def __init__(self, starting_study_tasks=None):
        
        if starting_study_tasks is None:
            self.study_tasks = []
        else:
            self.study_tasks = starting_study_tasks

    def add_study_task(self, new_study_task):
        
        self.study_tasks.append(new_study_task)

    def get_all_study_tasks(self):
        
        return self.study_tasks

    def get_study_task_count(self):
       
        return len(self.study_tasks)

    def complete_study_task(self, study_task_index):
        
        self.study_tasks[
            study_task_index
        ].mark_study_task_complete()

    def delete_study_task(self, study_task_index):
        
        return self.study_tasks.pop(study_task_index)

    def get_completed_study_task_count(self):
        
        completed_study_tasks = 0

        for study_task in self.study_tasks:
            if study_task.study_task_complete:
                completed_study_tasks += 1

        return completed_study_tasks