# models/member.py

class Member:
    def __init__(self, student_id, family_name, first_name, email, phone, address, join_date, subscription_status, skills="", interests=""):
        self.student_id = student_id
        self.family_name = family_name
        self.first_name = first_name
        self.email = email
        self.phone = phone
        self.address = address
        self.join_date = join_date
        self.subscription_status = subscription_status
        self.skills = skills
        self.interests = interests

    def __str__(self):
        return f"{self.student_id} - {self.family_name} {self.first_name} ({self.subscription_status})"

    def to_dict(self):
        """Retourne les données dans le bon ordre pour l'écriture CSV."""
        return {
            "student_id": self.student_id,
            "family_name": self.family_name,
            "first_name": self.first_name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "join_date": self.join_date,
            "subscription_status": self.subscription_status,
            "skills": self.skills,
            "interests": self.interests
        }
