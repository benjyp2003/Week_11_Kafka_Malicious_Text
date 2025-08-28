from utils.cleaner import Cleaner

class Update:
    def __init__(self,data:list):
        self.data = data


    def clean_and_update_text(self):
        for message in self.data:
            message['original_text'] = message['text']
            del message['text']
            cleaner = Cleaner(message['original_text'])
            cleaner.manager_cleaner()
            message["clean_text"] = cleaner.clean_data

        return self.data







