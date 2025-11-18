# storage/interests_storage.py
import csv

class Interest:
    def __init__(self, interest_id, member_id, interest_category, interest_name):
        self.interest_id = interest_id
        self.member_id = member_id
        self.interest_category = interest_category
        self.interest_name = interest_name


class InterestStorage:
    def __init__(self, file_path, encoding="utf-8"):
        self.file_path = file_path
        self.encoding = encoding

    def load_interests(self):
        interests = []
        try:
            with open(self.file_path, "r", encoding=self.encoding) as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    interests.append(Interest(**row))
        except Exception as e:
            print("[ERROR] Cannot load interests:", e)

        return interests
