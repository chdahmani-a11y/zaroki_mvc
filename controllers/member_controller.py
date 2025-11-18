# controllers/member_controller.py
import os
import csv
from storage.csv_storage import CSVStorage
from storage.skill_storage import SkillStorage
from models.member import Member

FIELDNAMES = [
    "student_id","family_name","first_name","email","phone",
    "address","join_date","subscription_status","skills","interests"
]

class MemberController:
    def __init__(self, file_path, view):
        self.file_path = file_path
        self.storage = CSVStorage(file_path)
        self.view = view
        self.skill_storage = SkillStorage("data/skills.csv")
        self.skills = self.skill_storage.load_skills()

    def load_members(self):
        return self.storage.load_members()

    def search_by_skill(self, skill_name):
        skill_name = skill_name.strip().lower()
        members = self.storage.load_members()
        matches = []
        for member in members:
            # member.skills might be a string "Python,SQL" or empty
            member_skills = []
            if getattr(member, "skills", None):
                member_skills = [s.strip().lower() for s in member.skills.split(",") if s.strip()]
            # also check skills table (separate file) where skill.student_id == member.student_id
            member_skills += [s.name.lower() for s in self.skills if s.student_id == member.student_id]
            if skill_name and skill_name in member_skills:
                matches.append(member)
        return matches

    def get_member_by_id(self, student_id):
        for m in self.storage.load_members():
            if str(m.student_id) == str(student_id):
                return m
        return None

    def update_member(self, student_id, new_data: dict):
        members = self.storage.load_members()
        updated = False
        for i, m in enumerate(members):
            if str(m.student_id) == str(student_id):
                # update attributes (keep other fields if missing)
                for k, v in new_data.items():
                    if hasattr(m, k):
                        setattr(m, k, v)
                members[i] = m
                updated = True
                break
        if updated:
            self.storage.save_members(members)
        return updated

    def delete_member(self, student_id):
        members = self.storage.load_members()
        new_list = [m for m in members if str(m.student_id) != str(student_id)]
        if len(new_list) == len(members):
            return False
        self.storage.save_members(new_list)
        return True

    def add_member(self, data):
        # keep header if needed
        write_header = not os.path.exists(self.file_path) or os.path.getsize(self.file_path) == 0
        with open(self.file_path, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter=';')
            if write_header:
                writer.writeheader()
            writer.writerow(data)
