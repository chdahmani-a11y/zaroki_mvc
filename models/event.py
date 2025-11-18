class Event:
    def __init__(self, event_id, member_id, event_name, organization, role, start_date, description):
        self.event_id = event_id
        self.member_id = member_id
        self.event_name = event_name
        self.organization = organization
        self.role = role
        self.start_date = start_date
        self.description = description
