🚕 Ola Dashboard & ML Prediction System – Bangalore Location

The Ola Dashboard & Ride Prediction System is a complete end-to-end data analytics and machine-learning solution designed to provide deep insights into ride-hailing operations within Bangalore. The project combines Excel (CSV) datasets, MySQL, Power BI, Machine Learning, Streamlit, and Flask to transform raw operational data into an interactive analytics dashboard and a smart prediction tool.

📌 Overview

This project goes beyond traditional BI dashboards by integrating data preprocessing, statistical analysis, business intelligence, and machine learning predictions.

The solution includes:

✔️ A detailed Power BI dashboard

For analyzing ride performance, revenue, cancellations, ratings, and demand zones.

✔️ A Machine Learning Prediction System

Using a Random Forest Regressor, the model predicts:

Ride Distance

Booking Value (Fare Amount)

based on:

Pickup location

Drop location

Vehicle type

A Streamlit frontend and Flask backend API provide a user-friendly interface for entering inputs and viewing predictions in real time.

⚙️ Tech Stack
📄 Excel (CSV Dataset)

Raw ride data — trips, fares, ratings, pickup/drop locations, vehicle types, etc.

🗄️ MySQL

Data import

Cleaning

Preprocessing

Query-based insights

📊 Power BI

Visualization

KPI dashboards

Interactive filters

Insight reporting

🤖 Machine Learning

Random Forest Regressor

Advanced preprocessing

Feature engineering for location-to-location prediction

Model evaluation & tuning

🌐 Streamlit (Frontend)

Clean UI for prediction

Input fields for pickup, drop, vehicle type

Real-time ML result display

🧩 Flask (Backend)

API endpoint for prediction

ML model and pipeline hosting

Integration with Streamlit

🔑 Features
📈 Overall Performance

Total rides

Total revenue

Active users

Average ride duration

🚗 Vehicle Type Analysis

Insights on ride distribution across:
Sedan, Prime SUV, Prime Plus, Mini, Auto, Bike, E-Bike.

💰 Revenue Insights

Revenue by vehicle category

Time-based trends

High-demand zones

❌ Cancellation Trends

Customer-initiated vs driver-initiated

Peak cancellation time slots

⭐ Customer Ratings

Ratings by ride type

Driver performance metrics

🔮 ML-Powered Ride Prediction System (Newly Added)

Predict ride distance

Predict booking value (fare)

Works using pickup, drop location, and vehicle type

Helps simulate price estimates before booking

🖼️ Dashboard Preview

(Insert dashboard image here)

🚀 Improvements in the Updated Version
✔️ Cleaned & Preprocessed Dataset

Outlier removal

Missing value treatment

Location mapping

Feature encoding

Normalization where required

✔️ Built Random Forest Regressor for Predictions

Trained using optimized hyperparameters

Achieves high accuracy for distance & price prediction

✔️ Developed a Full ML Web Application

Streamlit UI for user input

Flask backend serving prediction API

Real-time results with clean UX

This transforms the project from a static dashboard into a fully interactive analytics + ML prediction platform.

📊 Business Impact

Identify high-demand areas and optimize driver placement.

Reduce cancellations by analyzing behavior trends.

Improve revenue forecasting using the ML prediction system.

Enhance customer satisfaction using rating insights.

Provide approximate fare/distance predictions before booking.

🛠️ How to Use
1. Import Data into MySQL

Load the CSV files and run cleaning SQL scripts.

2. Visualize in Power BI

Connect MySQL → Build/refresh dashboard → Interact with filters.

3. Run the ML Prediction App

🚀Train the Flask Model (use the below command):

python train_model.py

🚀Run Streamlit frontend (use the below command):

streamlit run ola_app.py

Enter pickup, drop, vehicle type → get predictions instantly
<img width="958" height="863" alt="Screenshot 2025-11-25 123804" src="https://github.com/user-attachments/assets/e370659d-456a-4ca1-95d1-0fe63c9a7a3e" />
