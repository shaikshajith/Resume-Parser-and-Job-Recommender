import nltk
import spacy
from nltk.corpus import stopwords
import en_core_web_sm

# Download stopwords (runs only once)
nltk.download('stopwords')

# Load English stopwords
stop_words = set(stopwords.words('english'))

# Load SpaCy model
nlp = en_core_web_sm.load()
