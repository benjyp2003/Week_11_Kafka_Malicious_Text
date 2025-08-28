import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


class Cleaner:
    def __init__(self,data:str):
        self.data = data
        self.clean_data = data

    def removing_all_marks(self):
        translator = str.maketrans('', '', string.punctuation)
        clean_text = self.clean_data.translate(translator)
        self.clean_data = clean_text

    def removing_long_spaces(self):
        cleaned_text = ' '.join(self.clean_data.split())
        self.clean_data = cleaned_text

    def convert_to_lowercase(self):
        lowercase_string = self.clean_data.lower()
        self.clean_data = lowercase_string

    def removing_stop_words(self):
        stop_words = set(stopwords.words('english'))
        filtered_sentence = [w for w in self.clean_data.split() if not w in stop_words]
        self.clean_data = ' '.join(filtered_sentence)


    def lemtization(self):
        ps = PorterStemmer()
        lemtied_data = [ps.stem(word) for word in self.clean_data.split()]
        self.clean_data = ' '.join(lemtied_data)
        #self.clean_data = ""

    def manager_cleaner(self):
        self.removing_all_marks()
        self.removing_long_spaces()
        self.convert_to_lowercase()
        self.removing_stop_words()
        self.lemtization()

if __name__ == "__main__":
    cleaner = Cleaner("""This#$ is a"" sample/   sentenTCce, @@#@$  showing off   REYE    the stop words filtration.""")
    print(cleaner.clean_data)
    cleaner.removing_all_marks()
    print(cleaner.clean_data)
    cleaner.removing_long_spaces()
    print(cleaner.clean_data)
    cleaner.convert_to_lowercase()
    print(cleaner.clean_data)
    cleaner.removing_stop_words()
    print(cleaner.clean_data)
    cleaner.lemtization()
    print(cleaner.clean_data)


