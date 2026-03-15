<<<<<<< HEAD
# Real-Time Language Detection

Detects the language of text using Naive Bayes and TF-IDF character n-grams.

## Components
- **Model**: Scikit-Learn Pipeline (TF-IDF + MultinomialNB).
- **API**: FastAPI (`src/api.py`).
- **Frontend**: Simple HTML/JS (`frontend/index.html`).

## Setup
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Train the model:
   ```bash
   python src/train.py
   ```

## Usage
1. Start the API:
   ```bash
   uvicorn src.api:app --reload
   ```
2. Open `frontend/index.html` in your browser.
=======
# Language-Detection
ml project
>>>>>>> b1833e83a9ccaa94dee7d5701e6e983b82df0d6a
