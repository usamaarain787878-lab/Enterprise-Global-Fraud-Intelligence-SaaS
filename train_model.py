import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Dummy dataset create kar rahe hain demonstration ke liye
np.random.seed(42)
X = np.random.rand(1000, 5) # 5 features (jaise transaction amount, time, etc.)
y = np.random.choice([0, 1], size=1000, p=[0.95, 0.05]) # 0 = Normal, 1 = Fraud

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Models folder banakar save karna
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/fraud_model.pkl")

print("Model successfully train aur save ho gaya hai!")