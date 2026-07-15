"""
Program Name: Python Study Planner
Author: Liam Malone
Purpose: Define the regular and priority study task classes.
Resources Used: Original Project One Python Study Planner and
Date: July 14, 2026
"""


# project two code added
class StudyTask:
    

    def __init__(
        self,
        study_task_name,
        study_task_subject,
        study_task_complete=False
    ):
        
        self.study_task_name = study_task_name
        self.study_task_subject = study_task_subject
        self.study_task_complete = study_task_complete

    def mark_study_task_complete(self):
        
        self.study_task_complete = True

    def get_study_task_description(self):
        
        if self.study_task_complete:
            completion_status = "Complete"
        else:
            completion_status = "Not Complete"

        return (
            f"{self.study_task_name} - "
            f"{self.study_task_subject} - "
            f"{completion_status}"
        )

    # project two code added
    def convert_study_task_to_dictionary(self):
        
        return {
            "task_type": "regular",
            "name": self.study_task_name,
            "subject": self.study_task_subject,
            "complete": self.study_task_complete
        }


# project two code added
class PriorityStudyTask(StudyTask):
    

    def __init__(
        self,
        study_task_name,
        study_task_subject,
        priority_level,
        study_task_complete=False
    ):
        
        super().__init__(
            study_task_name,
            study_task_subject,
            study_task_complete
        )

        self.priority_level = priority_level

    def get_study_task_description(self):
       
        regular_description = (
            super().get_study_task_description()
        )

        return (
            f"{regular_description} - "
            f"Priority: {self.priority_level}"
        )

    # project two code added
    def convert_study_task_to_dictionary(self):
        
        task_dictionary = (
            super().convert_study_task_to_dictionary()
        )

        task_dictionary["task_type"] = "priority"
        task_dictionary["priority"] = self.priority_level

        return task_dictionary


# project two code added
def create_study_task_from_dictionary(task_dictionary):
    
    if task_dictionary.get("task_type") == "priority":
        return PriorityStudyTask(
            task_dictionary["name"],
            task_dictionary["subject"],
            task_dictionary.get("priority", "Medium"),
            task_dictionary.get("complete", False)
        )

    return StudyTask(
        task_dictionary["name"],
        task_dictionary["subject"],
        task_dictionary.get("complete", False)
    )