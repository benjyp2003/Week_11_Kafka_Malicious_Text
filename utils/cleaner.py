import string
import re
import nltk
from nltk.corpus import stopwords


class Cleaner:
    def __init__(self,data:str):
        self.data = data
        self.clean_data = data

    def removing_punctuation_marks(self):
        translator = str.maketrans('', '', string.punctuation)
        clean_text = self.clean_data.translate(translator)
        self.clean_data = clean_text

    def removing_special_marks(self):
        clean_string = ' '.join(e for e in self.clean_data.split() if e.isalnum())
        self.clean_data = clean_string

        #self.clean_data = ""

    def removing_long_spacees_end_marks(self):
        self.clean_data = ""
    #
    # def removing_stop_words(self):
    #     nltk.download('stopwords')
    #     stop_words = set(stopwords.words('english'))


        #print(stopwords.words('english'))
        # self.clean_data = ""

    def convert_to_lowercase(self):
        self.clean_data = ""

    def lemtization(self):
        self.clean_data = ""

if __name__ == "__main__":
    cleaner = Cleaner("""This#$ is a sample sentence, showing off the stop words filtration.""")
    print(cleaner.clean_data)
    cleaner.removing_punctuation_marks()
    #print(cleaner.clean_data)
    cleaner.removing_special_marks()

    print(cleaner.clean_data)


