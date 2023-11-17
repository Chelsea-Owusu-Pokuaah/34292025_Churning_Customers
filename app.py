import streamlit as st
import pickle as pk
import pandas as pd
import os


st.set_page_config(page_title="Customer Churning",
                   page_icon="😃", layout="wide")


st.subheader("Customer Churning site")
st.title("Predict whether a customer will churn or not")
st.write("Predict whether you will lose customer before you do!")

def map_yes_no(value):
    return 1 if value == "Yes" else 0

def map_one_zeros(value):
    return "Yes" if value == 1 else "No"


def predict(inputs):
    if input is not None:
        with open("mlp_scaler.pkl", "rb") as scaler_file:
            scaler = pk.load(scaler_file)
        inputs_scaled = scaler.fit_transform(inputs)

        try:
            with open("mlp_model.pkl", "rb") as model_file:
                model = pk.load(model_file)
                prediction = model.predict(inputs_scaled)
                prediction = map_one_zeros((prediction > 0.5).astype(int))
                st.success(f"Predicted Churn: {prediction}")
                return prediction
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
            return None
    else:
        st.warning("Please fill in all fields.")
        return None
    


def map_internet_service(value):
    return 1
with st.container():
    st.write("---")
    left_column, middle_column, middle2_column, right_column = st.columns(4)
# Collecting inputs for tenure, and ChargePerMonth
    with left_column:
        tenure = st.slider("Tenure", min_value=0, max_value=100)
        monthly_charges = st.slider("Monthly Charges", min_value=0, max_value=100)
        total_charges = st.slider("Total Charges", min_value=0, max_value=100)

    with middle_column:
        # Collecting inputs for gender, SeniorCitizzen, partner, and dependents
        senior_citizen = map_yes_no(st.radio("Senior citizen", ["Yes", "No"]))
        gender = map_yes_no(st.radio("Select Gender", ["Male", "Female"]))
        partner = map_yes_no(st.radio("Do you have a Partner", ["Yes", "No"]))
    
    with middle2_column:
        multiple_lines = map_yes_no(st.radio("Multiple Lines", ["Yes", "No"]))
        fiber_optic = map_yes_no(st.radio("Fibre Optic", ["Yes", "No"]))
        online_security = map_yes_no(st.radio("Online Security", ["Yes", "No"]))
        online_backup = map_yes_no(st.radio("Online Backup", ["Yes", "No"]))
        device_protection = map_yes_no(st.radio("Device protection", ["Yes", "No"]))


    
    with right_column:
        # Collecting inputs for other columns
        month_to_month_contract = map_yes_no(st.radio("Month to Month contracts", ["Yes", "No"]))
        two_year_contract = map_yes_no(st.radio("Two year contract", ["Yes", "No"]))
        paperless_billing = map_yes_no(st.radio("Paperless billing", ["Yes", "No"]))
        electronic_check_payment = map_yes_no(st.radio("Electronic check payment", ["Yes", "No"]))

if st.button("Enter"):
        inputs = None
            # creating a dictionary of the inputs
        user_inputs = {
                'senior_citizen': [senior_citizen],
                'tenure': [tenure],
                'gender': [gender],
                'partner': [partner],
                'multiple_lines': [multiple_lines],
                'fibre_optic': [fiber_optic],
                'online_backup': [online_backup],
                'device_protection': [device_protection],
                'internet_service_fibre': [fiber_optic],
                'monthly_charges': [monthly_charges],
                'total_charges':[total_charges],
                'month_to_month': [month_to_month_contract],
                'two_year': [two_year_contract],
                'paperless_billing': [paperless_billing],
                'electronic_check_payment': [electronic_check_payment],
            }
            # creating a dataframe from the inputs
        inputs = pd.DataFrame(user_inputs)

            # Call the predict_system function
        predict(inputs)
