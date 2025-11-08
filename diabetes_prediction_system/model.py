import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data
data = pd.read_csv('data/diabetes.csv')
X = data.drop('Outcome', axis=1)
y = data["Outcome"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save
with open("diabetes_model.pkl", "wb") as f:
    pickle.dump(model, f)