from storage.interests_storage import InterestStorage

class InterestController:
    def __init__(self, file_path):
        self.storage = InterestStorage(file_path)

    def get_all_interests(self):
        return self.storage.load_interests()
