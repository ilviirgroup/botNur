from datetime import datetime
import nltk, re, string, collections
from nltk.corpus import stopwords
from nltk.util import ngrams # function for making ngrams
nltk.download('stopwords')
from nltk.tokenize import word_tokenize

from nltk.stem import PorterStemmer

porter = PorterStemmer()


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello','hi','sup',):
        return "Hey! How`s it going"
    if user_message in ('time','time?'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    return tokenizer_porter(input_text)


def toNgrams(tx):
    sent = nltk.sent_tokenize(tx)

    return sent

def tokenizer(text):
    return text.split()

def tokenizer_porter(text):
    return [porter.stem(word) for word in text.split()]
