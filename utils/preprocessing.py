import string
from config.settings import nlp

def preprocess_text(text):
    text = text.lower()
    doc = nlp(text)
    clean_tokens = [token.text for token in doc if not token.is_stop and token.text not in string.punctuation]
    return " ".join(clean_tokens)
