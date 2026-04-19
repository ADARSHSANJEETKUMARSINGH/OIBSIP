# 📧 Email Spam Detection ML App

This project is a Machine Learning-based web application that classifies SMS/email messages as **Spam** or **Not Spam**.
It combines **TF-IDF feature extraction**, a **high-precision ML model**, and a **FastAPI-based backend with frontend UI** to deliver real-time predictions.



## 🧠 Problem Statement

Spam messages are not only annoying but can also be dangerous, often containing scams or phishing attempts.
The goal of this project is to build a reliable system that can automatically detect spam messages while **minimizing false positives**.



## ⚡ Features

* Classifies messages as **Spam** or **Not Spam**
* High-precision ML model (reduces false alerts)
* Real-time prediction via web interface
* FastAPI backend with integrated frontend
* Lightweight keyword enhancement for modern spam detection
* Clean and modular project structure



## 🛠 Tech Stack

* **Language:** Python
* **Machine Learning:** scikit-learn
* **Model:** Multinomial Naive Bayes
* **Vectorizer:** TF-IDF
* **Backend:** FastAPI
* **Frontend:** HTML, JavaScript
* **Libraries:** Pandas, NumPy



## 🧪 Model Performance

| Metric    | Value |
| --------- | ----- |
| Accuracy  | 97%   |
| Precision | 98%   |
| Recall    | 81%   |

The model is optimized for **high precision**, ensuring that legitimate messages are rarely misclassified as spam.



## 🚀 Project Architecture

Frontend (HTML + JS)
⬇
FastAPI Backend
⬇
TF-IDF Vectorizer
⬇
Naive Bayes Model
⬇
Prediction Output



## 🧩 Hybrid Enhancement (Important)

To improve detection of modern promotional spam messages (e.g., “gift card”, “exclusive deal”),
a lightweight **keyword-based enhancement layer** is added on top of the ML model.

> This helps detect spam patterns not present in the original dataset.



## 📁 Project Structure

```
email spam detection with ml/
│
├── data/
│   └── spam.csv
│
├── notebooks/
│   └── spam_detection.ipynb
│
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── index.html
│
├── requirements.txt
└── README.md
```



## 🧪 Jupyter Notebook Workflow

The notebook (`notebooks/spam_detection.ipynb`) includes:

### 1. Data Understanding & Cleaning

* Loaded dataset
* Removed unnecessary columns
* Handled duplicates and missing values

### 2. Text Preprocessing

* Lowercasing
* Removing punctuation and numbers
* Stopword removal

### 3. Feature Engineering

* Converted text into numerical features using TF-IDF

### 4. Model Training & Evaluation

* Trained Multinomial Naive Bayes and Logistic Regression
* Compared accuracy, precision, recall
* Selected best-performing model

### 5. Model Export

* Saved model and vectorizer using pickle



## ▶️ How to Run Locally

### 1. Clone repository

```bash
git clone <your-repo-link>
cd email-spam-detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run backend

```bash
uvicorn backend.app:app --reload
```

### 4. Open in browser

```
http://127.0.0.1:8000
```



## 🧪 Example Predictions

| Message                       | Prediction |
| ----------------------------- | ---------- |
| "Win free tickets now!!!"     | Spam       |
| "Let’s meet tomorrow"         | Not Spam   |
| "Exclusive deal just for you" | Spam       |
| "Call me when you’re free"    | Not Spam   |



## ⚠️ Limitations

* Model is trained on SMS dataset, so some modern spam formats may not be fully captured
* Performance depends on dataset vocabulary
* Keyword enhancement is rule-based and limited in scope



## 📌 Future Improvements

* Use deep learning models (LSTM / BERT)
* Expand dataset with modern spam examples
* Add user authentication system
* Deploy on cloud (Render / AWS / GCP)



## 📧 Author

**Adarsh Sanjeet Kumar Singh**
