import os
import csv
from storage.csv_storage import CSVStorage
from models.member import Member
from storage.skill_storage import SkillStorage

FIELDNAMES = ["student_id","family_name","first_name","email","phone","address","join_date","subscription_status","skills","interests"]

class MemberController:
    def __init__(self, file_path, view): 
        self.file_path = file_path
        self.storage = CSVStorage(file_path)  
        self.view = view 

    
        self.skill_storage = SkillStorage("data/skills.csv")
        self.skills = self.skill_storage.load_skills()

    def search_by_skill(self, skill_name):
        skill_name = skill_name.strip().lower()
        members = self.storage.load_members()
        matches = []

        for member in members:
        
            member_skills = [
                s.name.lower().strip() 
                for s in self.skills 
                if s.student_id == member.student_id
            ]

            if skill_name in member_skills:
                matches.append(member)

        return matches
