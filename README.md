# Phishing Email Detection System

## Overview

The Phishing Email Detection System is a Machine Learning-based cybersecurity project designed to identify phishing emails and distinguish them from legitimate emails.

The system uses Natural Language Processing (NLP) and Logistic Regression to analyze email content and classify emails as either:

* Phishing Email
* Safe Email

## Features

* Email classification using Machine Learning
* TF-IDF text vectorization
* Logistic Regression model
* URL detection and counting
* Suspicious keyword detection
* Confidence score prediction
* Graphical User Interface (Tkinter)
* Automatic scan report generation
* Confusion matrix and accuracy evaluation

## Technologies Used

* Python
* Scikit-Learn
* Pandas
* NumPy
* Joblib
* Tkinter
* Regular Expressions (Regex)

## Project Structure

Phishing-Email-Detection/

├── dataset/

├── model/

├── app.py

├── train.py

├── requirements.txt

├── README.md

└── reports/

## How It Works

1. User enters email content.
2. System extracts text features using TF-IDF.
3. URLs and suspicious keywords are detected.
4. Logistic Regression model predicts whether the email is phishing or safe.
5. Confidence score is displayed.
6. Scan report is automatically generated.

## Future Enhancements

* Real-world phishing email dataset
* Email file (.eml) analysis
* Web-based dashboard
* Deep Learning integration
* Real-time email monitoring

## Author

Developed as a Cybersecurity Internship Project.
