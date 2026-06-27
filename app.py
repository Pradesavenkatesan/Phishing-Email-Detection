import tkinter as tk
from tkinter import messagebox
import joblib
import re
from datetime import datetime

# Load model and vectorizer
model = joblib.load("model/phishing_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

SUSPICIOUS_KEYWORDS = [
    "urgent",
    "verify",
    "password",
    "login",
    "bank",
    "reward",
    "prize",
    "account",
    "suspended",
    "click",
    "winner",
    "claim",
    "security",
    "limited time",
    "update"
]

def count_urls(text):
    urls = re.findall(r'https?://\S+|www\.\S+', text)
    return len(urls)

def find_keywords(text):
    found = []

    text = text.lower()

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in text:
            found.append(keyword)

    return found

def generate_report(email, url_count, keywords, prediction_text, confidence):
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""
========================================
PHISHING EMAIL SCAN REPORT
========================================

Date: {timestamp}

Email:
{email}

URLs Found: {url_count}

Suspicious Keywords:
{", ".join(keywords) if keywords else "None"}

Prediction:
{prediction_text}

Confidence:
{confidence:.2f}%

========================================
"""

    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)

def check_email():
    email = email_text.get("1.0", tk.END).strip()

    if not email:
        messagebox.showwarning("Warning", "Please enter an email.")
        return

    url_count = count_urls(email)
    keywords = find_keywords(email)

    email_vector = vectorizer.transform([email])

    prediction = model.predict(email_vector)
    probability = model.predict_proba(email_vector)

    result_text = f"URLs Found: {url_count}\n\n"

    if keywords:
        result_text += "Suspicious Keywords:\n"
        result_text += ", ".join(keywords)
        result_text += "\n\n"
    else:
        result_text += "Suspicious Keywords: None\n\n"

    if prediction[0] == 1:
        confidence = probability[0][1] * 100
        prediction_text = "PHISHING EMAIL"

        result_text += (
            f"⚠️ PHISHING EMAIL DETECTED\n"
            f"Confidence: {confidence:.2f}%"
        )
    else:
        confidence = probability[0][0] * 100
        prediction_text = "SAFE EMAIL"

        result_text += (
            f"✅ SAFE EMAIL\n"
            f"Confidence: {confidence:.2f}%"
        )

    generate_report(
        email,
        url_count,
        keywords,
        prediction_text,
        confidence
    )

    result_label.config(text=result_text)

root = tk.Tk()
root.title("Phishing Email Detector")
root.geometry("700x500")

title = tk.Label(
    root,
    text="Phishing Email Detector",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

email_text = tk.Text(root, height=10, width=75)
email_text.pack(pady=10)

check_button = tk.Button(
    root,
    text="Check Email",
    command=check_email,
    font=("Arial", 12)
)
check_button.pack(pady=10)

result_label = tk.Label(
    root,
    text="Result will appear here",
    font=("Arial", 12),
    justify="left",
    wraplength=650
)
result_label.pack(pady=20)

root.mainloop()