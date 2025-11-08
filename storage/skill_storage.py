# storage/skill_storage.py
import csv
from models.skill import Skill

class SkillStorage:
    """Charge les compétences depuis un fichier CSV."""

    def __init__(self, file_path, encoding="utf-8"):
        self.file_path = file_path
        self.encoding = encoding

    def load_skills(self):
        skills = []
        try:
            with open(self.file_path, 'r', encoding=self.encoding) as file:
                reader = csv.DictReader(file, delimiter=';')
                
                for row in reader:
                    skill = Skill(
                        student_id=row.get("student_id", "").strip(),
                        category=row.get("skill_category", "").strip(),
                        name=row.get("skill_name", "").strip()
                    )
                    skills.append(skill)

            print("[INFO] Compétences chargées avec succès.")
        
        except FileNotFoundError:
            print("[ERROR] Le fichier des compétences est introuvable.")
        
        except Exception as e:
            print(f"[ERROR] Problème lors du chargement des compétences: {e}")

        return skills
