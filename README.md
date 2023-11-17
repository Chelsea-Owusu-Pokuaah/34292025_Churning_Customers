### Churn Prediction Project README

This document provides an overview of the Churn Prediction Project, including instructions for setup, usage, and customization.

# Project Name

Predicting Churning in a Telecommunication company

## Description

This assignment trained a multi layer perceptron on data from cutomers of a telecommunication company. The model predicts whther a customer will churn or not.

## Features

- User interface for enterning new data and making predictions
- Predictive system predicts whether a customer will churn or not based on selected features

## Installation

  - Install required packages by running:
     ```python
     !pip install tensorflow
     !pip install scikeras
     ```
   - Mount Google Drive:
     ```python
     from google.colab import drive
     drive.mount('/content/drive')
     ```
   - Install packages in requirements.txt

## Setup

   - Open the Colab Notebook provided

## Streamlit App:

   - The Streamlit app is available for predicting customer churn.
   - Run the Streamlit app using "streamlit run app.py"

## Usage

1. Data Preparation:
   - Load and preprocess the dataset as explained in the notebook.

2. Model Inference:
   - Train the Random Forest model and evaluate its performance.

3. Streamlit App:
   - Use the Streamlit app to predict customer churn interactively.
   - Customize the input sliders and radio buttons to input customer details.

## References

    OpenAI. (2023). ChatGPT [Large language model]. https://chat.openai.com

## Link to video
   https://youtu.be/jATnZpbk3OU?si=adgmuwyCsd7YmvIw



