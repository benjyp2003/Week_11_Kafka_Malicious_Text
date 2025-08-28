from utils.cleaner import Cleaner
class Update:
    def __init__(self,data:list):
        self.data = data



    def clean_and_update_text(self):
        #print(self.data)
        for message in self.data:
            message['original_text'] = message['text']
            del message['text']
            cleaner = Cleaner(message['original_text'])
            cleaner.manager_cleaner()
            message["clean_text"] = cleaner.clean_data

        return self.data
        #     print("old data::::")
        #     print(message['original_text'])
        #
        #     print("clean data")
        #     print(message["clean_text"])
        # print(self.data)






