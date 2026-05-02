import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from preprocess import clean_text, preprocess_text

os.makedirs("models", exist_ok=True)

df = pd.read_csv("data/feedback_data.csv")

df['clean'] = df['text'].apply(clean_text)
df['processed'] = df['clean'].apply(preprocess_text)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['processed'])

# Train TWO models
sentiment_model = MultinomialNB()
emotion_model = MultinomialNB()

sentiment_model.fit(X, df['sentiment'])
emotion_model.fit(X, df['emotion'])

# Save models
pickle.dump(sentiment_model, open("models/sentiment.pkl", "wb"))
pickle.dump(emotion_model, open("models/emotion.pkl", "wb"))
pickle.dump(vectorizer, open("models/vectorizer.pkl", "wb"))

print("✅ Sentiment + Emotion models saved!")