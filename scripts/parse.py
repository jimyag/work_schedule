from typing import List


def free_time_student(index: int, name: List[str], students: dict):
    for student_name, student in students.items():
        if student[index]:
            name.append(student_name)
    if len(name) == 0:
        name.append("此处无人")


def get_free_time_names(students: dict, free_time_names: List[List[str]]):
    for index in range(20):
        name = []
        free_time_student(index, name, students)
        free_time_names.append(name)
