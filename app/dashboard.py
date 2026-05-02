import streamlit as st
import pickle
import pandas as pd
import sys
import os

# Fix path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.preprocess import clean_text, preprocess_text

# Load models
sentiment_model = pickle.load(open("models/sentiment.pkl", "rb"))
emotion_model = pickle.load(open("models/emotion.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

# Page config
st.set_page_config(page_title="Feedback AI", layout="wide")

# DARK THEME STYLE
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #1f2937;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 AI Feedback Intelligence Dashboard")

# INPUT
user_input = st.text_area("Enter customer feedback:")

if st.button("Analyze"):
    text = clean_text(user_input)
    text = preprocess_text(text)
    vec = vectorizer.transform([text])

    sentiment = sentiment_model.predict(vec)[0]
    emotion = emotion_model.predict(vec)[0]

    col1, col2 = st.columns(2)

    col1.markdown(f"<div class='card'>Sentiment: <b>{sentiment}</b></div>", unsafe_allow_html=True)
    col2.markdown(f"<div class='card'>Emotion: <b>{emotion}</b></div>", unsafe_allow_html=True)

# LOAD DATA
df = pd.read_csv("data/feedback_data.csv")

st.markdown("---")

col1, col2 = st.columns(2)

col1.subheader("📊 Sentiment Distribution")
col1.bar_chart(df['sentiment'].value_counts())

col2.subheader("🎭 Emotion Distribution")
col2.bar_chart(df['emotion'].value_counts())

st.markdown("---")

st.subheader("📂 Raw Data")
st.dataframe(df)