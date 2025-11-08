# models/skill.py

class Skill:
    """Représente une compétence possédée par un membre."""

    def __init__(self, student_id, category, name):
        self.student_id = student_id
        self.category = category
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.category})"
