import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
df = pd.read_csv("dataset/emails.csv")

X = df["text"]
y = df["label"]

# Convert text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy * 100)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)
import os
import joblib

# Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save model and vectorizer
joblib.dump(model, "model/phishing_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Model saved successfully!")