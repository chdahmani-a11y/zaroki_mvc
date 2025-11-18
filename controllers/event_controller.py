from storage.events_storage import EventStorage
from storage.interests_storage import InterestStorage

class EventController:
    def __init__(self):
        self.event_storage = EventStorage("data/events.csv")
        self.interest_storage = InterestStorage("data/interests.csv")

    def get_events_by_member(self, member_id):
        events = self.event_storage.load_events()
        return [e for e in events if e.member_id == member_id]

    def get_interests_by_member(self, member_id):
        interests = self.interest_storage.load_interests()
        return [i for i in interests if i.member_id == member_id]

    def get_all_events(self):
        return self.event_storage.load_events()

    def get_all_interests(self):
        return self.interest_storage.load_interests()
