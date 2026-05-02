# 🤖 Customer Feedback Sentiment & Emotion Analysis Dashboard

## 📌 Overview
This project is an AI-powered dashboard that analyzes **customer feedback** and classifies it into:

- 😊 Positive / 😡 Negative / 😐 Neutral (Sentiment)
- 😀 Happy / 😢 Sad / 😠 Angry (Emotion)

It provides insights similar to how companies analyze customer reviews and feedback at scale.

---

## 🎯 Problem Statement
Businesses receive large volumes of customer feedback across platforms. Manually analyzing this data is inefficient.

This project automates:
- Sentiment detection  
- Emotion recognition  
- Insight generation via an interactive dashboard  

---

## 💼 Industry Use Cases
- Customer feedback analysis (e-commerce, apps)
- Product improvement insights
- Support quality monitoring
- Brand perception tracking

---

## 🧠 Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- NLTK (NLP preprocessing)  
- Streamlit (Dashboard)  
- Plotly (Visualization)  

---

## ⚙️ Features

### 🔹 NLP Pipeline
- Text cleaning & preprocessing  
- Stopword removal  
- TF-IDF vectorization  

### 🔹 Machine Learning
- Multinomial Naive Bayes  
- Dual model system:
  - Sentiment classifier  
  - Emotion classifier  

### 🔹 Dashboard
- Real-time prediction  
- Dual output (Sentiment + Emotion)  
- Interactive charts  
- Dark-themed UI  
- Dataset preview  

---

## 🏗️ Architecture

```
Data → Cleaning → Preprocessing → TF-IDF → ML Models → Prediction → Dashboard
```

---

## 📁 Folder Structure

```
Feedback-Sentiment-Pro/
│
├── data/                # Dataset
├── src/                 # Preprocessing & training code
├── app/                 # Streamlit dashboard
├── models/              # Saved models
├── images/              # Screenshots
├── requirements.txt
└── README.md
```

---

## ⚡ Installation

```bash
git clone https://github.com/yourusername/customer-feedback-sentiment-dashboard.git
cd customer-feedback-sentiment-dashboard

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

---

## ▶️ How to Run

### Train Model
```bash
python src/train.py
```

### Run Dashboard
```bash
streamlit run app/dashboard.py
```

---

## 📊 Output

- Sentiment prediction (Positive / Negative / Neutral)  
- Emotion prediction (Happy / Sad / Angry)  
- Interactive dashboard with charts  


---

## 🎓 Learning Outcomes
- NLP preprocessing techniques  
- Text classification using ML  
- Multi-model system design  
- Dashboard development with Streamlit  
- End-to-end project building  

---

## 🙏 Acknowledgement
Special thanks to my mentor and Indian Institute of Placement for their guidance and support.

---

## 👩‍💻 Author
Yashika Aggarwal
---

## ⭐ Support
If you found this project useful, consider giving it a star ⭐
