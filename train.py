import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import joblib

# Replace with IBM dataset CSV
df = pd.read_csv("data.csv")

# Basic preprocessing
df = df.dropna()

# Example encoding
df = pd.get_dummies(df)

# Target
y = df['Attrition_Yes']
X = df.drop(columns=['Attrition_Yes'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

joblib.dump(clf, "attrition_model.pkl")

# Salary hike regression (dummy target example)
if 'MonthlyIncome' in df.columns:
    y_reg = df['MonthlyIncome']
    reg = RandomForestRegressor()
    reg.fit(X, y_reg)
    joblib.dump(reg, "salary_model.pkl")

print("Models trained and saved.")
