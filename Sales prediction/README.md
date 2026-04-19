# 📊 Sales Prediction using Machine Learning

## 🚀 Project Overview

This project aims to predict product sales based on advertising expenditure across different platforms such as TV, Radio, and Newspaper.

Using **Linear Regression**, we analyze how advertising budgets influence sales and build a model to make accurate predictions.

---

## 📁 Project Structure

```
sales_prediction/
│
├── advertising.csv
└── sales_prediction.ipynb
```

---

## 🧠 Problem Statement

Businesses need to estimate future sales based on advertising spend.
This project helps in predicting **Sales** using:

* TV Advertising Budget
* Radio Advertising Budget
* Newspaper Advertising Budget

---

## ⚙️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## 🔍 Workflow

1. **Data Loading**
2. **Data Understanding**
3. **Data Cleaning**
4. **Exploratory Data Analysis (EDA)**
5. **Feature Selection**
6. **Model Training (Linear Regression)**
7. **Model Evaluation**
8. **Prediction & Insights**

---

## 📊 Model Performance

* **MAE:** ~1.46
* **MSE:** ~3.17
* **R² Score:** ~0.90

👉 The model explains ~90% of the variance in sales, indicating strong performance.

---

## 💡 Key Insights

* 📈 **TV Advertising:** Strong impact on sales
* 📻 **Radio Advertising:** Moderate impact
* 📰 **Newspaper Advertising:** Minimal impact

---

## ▶️ How to Run This Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/sales-prediction.git
cd sales-prediction
```

---

### 2️⃣ Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

### 3️⃣ Run the Notebook

```bash
jupyter notebook
```

Then open:

```
sales_prediction.ipynb
```

---

## 📌 Example Prediction

The model predicts sales based on advertising input:

```python
model.predict([[TV, Radio, Newspaper]])
```

---

## 🎯 Conclusion

This project demonstrates how machine learning can help businesses:

* Optimize advertising budgets
* Understand key sales drivers
* Make data-driven decisions

---

## 🙌 Author

Adarsh
(ML Enthusiast | Aspiring Data Scientist)
