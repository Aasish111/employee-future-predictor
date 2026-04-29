# 🚀 Employee Future Predictor

A Machine Learning project that predicts employee attrition and estimates the financial impact on organizations. It also forecasts future salary based on employee retention.

---

## 📌 Overview

Employee attrition is a major concern for companies due to the high cost of hiring and training replacements. This project uses Machine Learning to:

* Predict whether an employee will leave or stay
* Estimate financial loss if the employee leaves
* Predict future salary if the employee stays

---

## 🎯 Features

✔ Attrition Prediction using classification model
✔ Financial Loss Estimation for employee exit
✔ Salary Prediction after annual hike
✔ End-to-end ML pipeline
✔ Interactive web app using Streamlit

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, scikit-learn, joblib
* **Visualization/UI:** Streamlit
* **Dataset:** IBM HR Analytics Dataset

---

## 📂 Project Structure

```
employee-future-predictor/
│── app.py                  # Streamlit web app
│── train.py               # Model training script
│── requirements.txt       # Dependencies
│── data.csv               # Sample dataset (replace with IBM dataset)
│── attrition_model.pkl    # Saved classification model
│── salary_model.pkl       # Saved regression model
│── README.md              # Project documentation
```

---

## ⚙️ How It Works

### 1. Data Preprocessing

* Handling missing values
* Encoding categorical variables
* Feature selection

### 2. Model Training

* **Classification Model:** Predicts employee attrition
* **Regression Model:** Predicts salary

### 3. Prediction Logic

* If employee is likely to leave → estimate financial loss
* If employee stays → predict salary after hike

---

## ▶️ Run Locally

### Step 1: Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/employee-future-predictor.git
cd employee-future-predictor
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Train Models

```bash
python train.py
```

### Step 4: Run Application

```bash
streamlit run app.py
```

---

## 📊 Sample Output

* 🟥 "Employee likely to leave → Estimated loss: ₹XXXXX"
* 🟩 "Employee will stay → Predicted salary: ₹XXXXX"

---

## 🚀 Future Improvements

* Advanced feature engineering
* Hyperparameter tuning
* Model explainability (SHAP/LIME)
* Real-time HR dashboard
* Deployment on cloud (Streamlit Cloud / AWS)

---

## 📈 Use Cases

* HR Analytics
* Workforce Planning
* Cost Optimization
* Employee Retention Strategies

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---
