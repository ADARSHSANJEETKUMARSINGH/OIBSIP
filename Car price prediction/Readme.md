# 🚗 Car Price Prediction using Machine Learning

## 📌 Project Overview

This project aims to predict the **selling price of used cars** based on various features such as present price, kilometers driven, fuel type, transmission, and more.

The goal is to build a regression model that can estimate car prices accurately using historical data.



## 🎯 Problem Statement

Predict the **Selling Price** of a car using its features.



## 📊 Dataset Description

The dataset contains the following features:

* **Car_Name** – Name of the car
* **Year** – Manufacturing year
* **Selling_Price** – Target variable (price to predict)
* **Present_Price** – Current ex-showroom price
* **Driven_kms** – Total kilometers driven
* **Fuel_Type** – Petrol/Diesel/CNG
* **Selling_type** – Dealer/Individual
* **Transmission** – Manual/Automatic
* **Owner** – Number of previous owners



## ⚙️ Steps Performed

### 1. Data Loading & Inspection

* Loaded dataset using pandas
* Checked structure using `.head()`, `.info()`, `.shape()`



### 2. Exploratory Data Analysis (EDA)

* Checked duplicate values and removed them
* Analyzed statistical summary using `.describe()`
* Visualized distributions of numerical features
* Identified skewness and outliers



### 3. Data Cleaning

* Removed duplicate rows
* Verified data consistency



### 4. Feature Engineering

* Created a new feature:
  **Car_Age = Current Year - Year**
* Dropped unnecessary columns:

  * `Year`
  * `Car_Name` (high cardinality, not useful directly)



### 5. Encoding

* Converted categorical variables into numerical using **One-Hot Encoding**
* Used `drop_first=True` to avoid multicollinearity



### 6. Train-Test Split

* Split dataset into:

  * 80% training data
  * 20% testing data



### 7. Model Training

* Trained **Linear Regression** model

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```



### 8. Model Evaluation

* **R² Score:** 0.75
* **Mean Absolute Error (MAE):** 1.47

Interpretation:

* Model explains ~75% of variance
* Average prediction error ≈ ₹1.47 lakh



### 9. Model Comparison

* Tried Random Forest Regressor
* Linear Regression performed better for this dataset



### 10. Prediction Analysis

* Compared actual vs predicted values
* Analyzed prediction errors



## 📈 Results

* Linear Regression provided the best performance
* Model captures major pricing trends effectively



## 🚀 Future Improvements

* Apply feature scaling
* Perform hyperparameter tuning
* Try advanced models like:

  * Random Forest (tuned)
  * XGBoost
* Handle outliers more effectively
* Use larger dataset for better performance



## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn



## 📌 Conclusion

This project demonstrates a complete machine learning workflow:

* Data understanding
* Cleaning
* Feature engineering
* Model training
* Evaluation

The model can reasonably predict car prices and serves as a strong foundation for further improvements.



## 👨‍💻 Author

Adarsh Sanjeet Kumar Singh
