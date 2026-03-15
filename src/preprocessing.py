import re
import string

def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Remove extra spaces
    text = " ".join(text.split())
    
    return text
