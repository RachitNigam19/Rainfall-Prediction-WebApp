# 🌧️ Rainfall-Prediction-WebApp
This repository contains a machine learning-powered web application that predicts rainfall based on meteorological data. Built with Flask for a responsive web interface and scikit-learn for predictive modeling, this project demonstrates expertise in data science, web development, and application deployment.
📖 Overview
The Rainfall Prediction WebApp uses a trained machine learning model to forecast rainfall based on features like temperature, humidity, or other weather metrics. The Flask-based web interface allows users to input data and view predictions through a clean, responsive UI. The project includes a preprocessed dataset (Rainfall.csv) and a serialized model (rainfall_model.pkl), with deployment support via a procfile for platforms like Heroku.
🎯 Features

Predicts rainfall using a machine learning model trained on weather data.
Responsive web interface built with Flask, HTML, and CSS.
Supports user input for weather features (e.g., temperature, humidity).
Preprocessed dataset and model for efficient predictions.
Deployment-ready setup with a procfile for platforms like Heroku.

🛠️ Tech Stack

Python: Core programming language.
Flask: Lightweight framework for building the web application.
Scikit-learn: For training and serving the rainfall prediction model.
Pandas/NumPy: For data manipulation and processing.
HTML/CSS: For front-end UI (in templates and static folders).
Gunicorn: WSGI server for deployment (via procfile).
Git: Version control with .gitignore for clean repository management.

🚀 Getting Started
Prerequisites

Python 3.8+
Git
Heroku CLI (optional, for deployment)

Installation

Clone the repository:git clone https://github.com/RachitNigam19/Rainfall-Prediction-WebApp.git
cd Rainfall-Prediction-WebApp


Install dependencies:pip install -r requirements.txt


Ensure the serialized model (rainfall_model.pkl) and dataset (Rainfall.csv) are in the root directory.

Usage

Run the Flask application locally:python app.py


Access the app at http://localhost:5000.


Input weather data (e.g., temperature, humidity) via the web UI to get rainfall predictions.
Explore the rainfall.py script for model training or preprocessing details.

Deployment (Optional)

Deploy to Heroku:heroku create
git push heroku main
heroku open


Ensure the procfile is configured (e.g., web: gunicorn app:app).

📂 Project Structure
Rainfall-Prediction-WebApp/
├── static/                      # CSS and static assets for the web UI
├── templates/                   # HTML templates for the web interface
├── app.py                       # Main Flask application
├── rainfall.py                  # Model training and preprocessing script
├── Rainfall.csv                 # Dataset for training and predictions
├── rainfall_model.pkl           # Serialized machine learning model
├── procfile                     # Deployment configuration for Heroku
├── requirements.txt             # Project dependencies
├── .gitignore                   # Files/folders to ignore in Git
├── rainfallenv/                 # Virtual environment (excluded from Git)

🔍 How It Works

Dataset: The Rainfall.csv file contains a dataset of meteorological features (e.g., temperature, humidity) for training the model.
Model: The rainfall_model.pkl file stores a trained scikit-learn model (e.g., regression or classification) for predicting rainfall.
Preprocessing: The rainfall.py script likely handles data preprocessing and model training.
Web UI: The app.py script uses Flask to serve a web interface, with HTML templates in templates and styling in static.
Deployment: The procfile enables deployment on platforms like Heroku using Gunicorn.

🌟 Why This Project?

Demonstrates expertise in machine learning for weather prediction.
Showcases skills in building responsive web applications with Flask.
Highlights proficiency in data preprocessing and model serialization.
Reflects deployment knowledge with Heroku and Gunicorn.
Provides a practical example of an ML-driven web application for environmental analytics.

📫 Contact

GitHub: RachitNigam19
LinkedIn: Rachit Nigam
Email: rachitn46@gmail.com

Feel free to explore, contribute, or reach out for collaboration!
