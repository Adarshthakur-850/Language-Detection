import pandas as pd
import numpy as np

def load_data():
    # Synthetic dataset for demonstration
    data = []
    
    # English
    data.extend([("Hello world", "English"), ("This is a test", "English"), 
                 ("Machine learning is great", "English"), ("How are you?", "English"),
                 ("The quick brown fox", "English"), ("Good morning", "English")])
    
    # Spanish
    data.extend([("Hola mundo", "Spanish"), ("Esto es una prueba", "Spanish"), 
                 ("El aprendizaje automático es genial", "Spanish"), ("¿Cómo estás?", "Spanish"),
                 ("El zorro marrón rápido", "Spanish"), ("Buenos días", "Spanish")])
    
    # French
    data.extend([("Bonjour le monde", "French"), ("Ceci est un test", "French"), 
                 ("L'apprentissage automatique est génial", "French"), ("Comment ça va?", "French"),
                 ("Le renard brun rapide", "French"), ("Bonjour", "French")])
                 
    # German
    data.extend([("Hallo Welt", "German"), ("Das ist ein Test", "German"), 
                 ("Maschinelles Lernen ist großartig", "German"), ("Wie geht es dir?", "German"),
                 ("Der schnelle braune Fuchs", "German"), ("Guten Morgen", "German")])
                 
    # Hindi (Transliterated/Script mix for robustness logic test, usually script based is easy)
    data.extend([("Namaste duniya", "Hindi"), ("Yeh ek pariksha hai", "Hindi"),
                 ("Mera naam kya hai", "Hindi"), ("Aap kaise hain", "Hindi"),
                 ("नमस्ते दुनिया", "Hindi"), ("सुप्रभात", "Hindi")])

    df = pd.DataFrame(data, columns=['text', 'language'])
    return df
