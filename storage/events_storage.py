import csv

class Event:
    def __init__(self, event_id, member_id, event_name, organization, role, start_date, description):
        self.event_id = event_id
        self.member_id = member_id
        self.event_name = event_name
        self.organization = organization
        self.role = role
        self.start_date = start_date
        self.description = description


class EventStorage:
    def __init__(self, file_path, encoding="utf-8"):
        self.file_path = file_path
        self.encoding = encoding

    def load_events(self):
        events = []
        try:
            with open(self.file_path, "r", encoding=self.encoding) as f:
                reader = csv.DictReader(f, delimiter=";")

                for row in reader:
                    event = Event(
                        row.get("event_id", ""),
                        row.get("member_id", ""),
                        row.get("event_name", ""),
                        row.get("organization", ""),
                        row.get("role", ""),
                        row.get("start_date", ""),
                        row.get("description", "")
                    )
                    events.append(event)

            print("[INFO] Événements chargés avec succès.")

        except FileNotFoundError:
            print("[ERROR] Le fichier events.csv est introuvable.")

        except Exception as e:
            print(f"[ERROR] Erreur lors du chargement des événements : {e}")

        return events
