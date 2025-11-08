# storage/csv_storage.py
import csv
from models.member import Member

FIELDNAMES = [
    "student_id", "family_name", "first_name", "email", "phone",
    "address", "join_date", "subscription_status", "skills", "interests"
]

class CSVStorage:
    def __init__(self, file_path, encoding='utf-8'):
        self.file_path = file_path
        self.encoding = encoding

    def load_members(self):
        members = []
        try:
            with open(self.file_path, "r", encoding=self.encoding) as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    member = Member(
                        row.get("student_id", "").strip(),
                        row.get("family_name", "").strip(),
                        row.get("first_name", "").strip(),
                        row.get("email", "").strip(),
                        row.get("phone", "").strip(),
                        row.get("address", "").strip(),
                        row.get("join_date", "").strip(),
                        row.get("subscription_status", "").strip(),
                        row.get("skills", "").strip(),
                        row.get("interests", "").strip()
                    )
                    members.append(member)
            print("[INFO] Fichier chargé avec succès.")
        except FileNotFoundError:
            print("[INFO] Fichier introuvable, il sera créé plus tard.")
        except Exception as e:
            print(f"[ERROR] Erreur lors du chargement du fichier : {e}")
        return members

    def save_members(self, members):
        """Réécrit tout le CSV proprement."""
        if not members:
            print("[INFO] Aucun membre à sauvegarder.")
            return
        
        with open(self.file_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter=';')
            writer.writeheader()
            for m in members:
                writer.writerow(m.to_dict())

        print("[INFO] Données mises à jour dans le fichier.")
