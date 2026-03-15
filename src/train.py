import pandas as pd
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

from src.data_loader import load_data
from src.preprocessing import preprocess_text

def train():
    print("Loading data...")
    df = load_data()
    
    print("Preprocessing...")
    df['clean_text'] = df['text'].apply(preprocess_text)
    
    X = df['clean_text']
    y = df['language']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Pipeline: TF-IDF (Char n-grams) -> Naive Bayes
    pipeline = Pipeline([
        ('vectorizer', TfidfVectorizer(analyzer='char', ngram_range=(2, 3))),
        ('classifier', MultinomialNB())
    ])
    
    print("Training model...")
    pipeline.fit(X_train, y_train)
    
    print("Evaluating...")
    y_pred = pipeline.predict(X_test)
    print(classification_report(y_test, y_pred))
    
    # Save Model
    if not os.path.exists("models"):
        os.makedirs("models")
        
    joblib.dump(pipeline, "models/language_detector.pkl")
    print("Model saved to models/language_detector.pkl")
    
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8,6))
    sns.heatmap(cm, annot=True, fmt='d', xticklabels=pipeline.classes_, yticklabels=pipeline.classes_)
    plt.title("Confusion Matrix")
    plt.savefig("models/confusion_matrix.png")
    plt.close()

if __name__ == "__main__":
    train()
