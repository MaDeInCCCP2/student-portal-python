# models/student.py
class Student:
    def __init__(self, id=None, first_name="", last_name="", email=""):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"