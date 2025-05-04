# 🚘 Automobile Price Prediction using Machine Learning

![GitHub repo size](https://img.shields.io/github/repo-size/pratham14-coder/Automobile_Price_Prediction_model)
![GitHub stars](https://img.shields.io/github/stars/pratham14-coder/Automobile_Price_Prediction_model?style=social)
![GitHub forks](https://img.shields.io/github/forks/pratham14-coder/Automobile_Price_Prediction_model?style=social)


> 🔍 A machine learning model to predict car prices based on various features — built during my **Data Science Internship at [Rubixe](https://rubixe.com/)**.

---

## 🧠 Overview

This project focuses on building a **regression-based ML model** that can predict automobile prices using real-world data. The model leverages various car attributes such as engine size, horsepower, fuel type, and more.

🎯 **Objective**: Help customers, dealers, and platforms like used car marketplaces to **estimate car prices more accurately**.

---

## ⚙️ Technologies & Tools

| Category       | Tools & Libraries                          |
|----------------|---------------------------------------------|
| Language       | Python 3.x                                  |
| Data Handling  | Pandas, NumPy                               |
| Visualization  | Matplotlib, Seaborn                         |
| Modeling       | Scikit-learn (Linear Regression, RF, SVR)   |
| Tuning & Eval  | GridSearchCV, R², MAE, MSE, RMSE            |
| IDE            | Jupyter Notebook                            |

---

## 📦 Dataset

- Source: [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/automobile)
- Records: 205 cars
- Features include:
  - Make, Fuel Type, Body Style
  - Horsepower, Engine Size, Mileage
  - Number of Doors, Curb Weight
  - Target: **Price**

---

## 🧹 Data Preprocessing Highlights

- ✅ Missing values handled
- 🔄 Categorical to numeric: Label & One-Hot Encoding
- 📊 Feature scaling: StandardScaler
- 🧠 Correlation analysis for feature selection

---

## 🏗️ Model Building

Trained multiple regression algorithms:

- 🔹 Linear Regression
- 🌲 Random Forest Regressor
- 🧮 Support Vector Regressor
- 🌳 Decision Tree Regressor

Best performance from: **Random Forest**  
(📌 R² Score: *XX.XX*, RMSE: *XXX.XX*)

---

## 📊 Evaluation Metrics

| Metric      | Description                           |
|-------------|---------------------------------------|
| R² Score    | How well the model explains variance |
| MAE         | Average error between predictions    |
| MSE         | Mean of squared errors               |
| RMSE        | Square root of MSE                   |

---

## 🚀 Results & Insights

- ✅ High accuracy in predicting car prices
- 💡 Discovered most influential features:
  - Engine size
  - Horsepower
  - Curb weight
- 📈 Visualized feature importance & residuals

---

## ▶️ How to Run

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/automobile-price-prediction.git

# 2. Navigate into the directory
cd automobile-price-prediction

# 3. Install required packages
pip install -r requirements.txt

# 4. Open the notebook
jupyter notebook Automobile_Price_Prediction.ipynb
```
