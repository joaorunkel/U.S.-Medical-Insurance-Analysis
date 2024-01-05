# Insurance Cost Prediction and Analysis

This project is a portfolio project that demonstrates fundamental skills in data science, machine learning, and artificial intelligence, acquired through Codecademy's courses. It should not be used as an insurance counselor.

## Overview

The code provides insights into U.S. medical insurance costs using Python, specifically utilizing the pandas library for data analysis and scikit-learn for machine learning. The project includes a linear regression model to predict insurance costs and a simple Tkinter-based user interface for interacting with the model.

## Project Context

This project is part of Codecademy's Data Science, Machine Learning, and AI fundamentals. All code was independently developed without the use of code generator text. The only part where AI-like chatGPT was employed is in the UI, as it was an additional feature. At the time of project development, there was a limited knowledge of user interface development in Python, and the goal was to showcase the application of Python for data analysis and machine learning.

## Prerequisites

- Python 3.x
- Libraries: pandas, scikit-learn, tkinter
- "insurance.csv" document

## Features

1. **Charges Insights:**
   - Average charges analysis.
   - Average charges per region.
   - Average charges for smokers and non-smokers.
   - Average charges based on gender.
   - Average charges for parents.

2. **Age Insights:**
   - Average age of smokers.
   - Average age of parents.
   - Average age per region.

3. **Gender Insights:**
   - Count of individuals for each gender.
   - Count of smokers for each gender.
   - Gender-based cost difference.

4. **Important Conclusions:**
   - Impacts of region, smoking and gender on insurance costs.

5. **Linear Regression Model:**
   - Utilizes scikit-learn's Linear Regression for cost prediction.
   - One-hot encoding of categorical variables.

6. **Insurance cost predictor and BMI Calculator:**
   - Insurance costs predictor with age, gender, BMI and number of children inputs with a Tkinter-based GUI.
   - A simple BMI calculator with a Tkinter-based GUI.

## Usage

1. Ensure you have Python, required libraries installed and "insurance.csv" document.
2. Run the `us_medical_insurance_cost.py` script.
3. Use the provided Tkinter interface to input information and predict insurance costs.
