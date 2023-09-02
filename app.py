import streamlit as st
import pandas as pd
import pickle

# Load the saved model
model = pickle.load(open('model_2.pkl', 'rb'))

# Streamlit UI
st.set_page_config(page_title="Credit Card Default Prediction")
st.title("Credit Card Defaulter Prediction")

# Gender selection
gender = st.radio("Gender:", ("Male", "Female"))

# Education selection
education = st.radio("Education:", ("Graduate School", "University", "High School", "Others"))

# Marital Status selection
marriage = st.radio("Marital Status:", ("Married", "Single", "Others"))

# Age input
age = st.number_input("Age:", min_value=18, max_value=100)

# Limit Balance input
limit_bal = st.number_input("Limit Balance (in NT dollars):", min_value=0)

# Map repayment status categories to numerical values
repay_status_mapping = {
    "On-Time Payment": 0,
    "payment delay for one month": 1,
    "payment delay for two months": 2,
    "payment delay for three months": 3,
    "payment delay for four months": 4,
    "payment delay for five months": 5,
    "payment delay for six months": 6,
    "payment delay for seven months": 7,
    "payment delay for eight months": 8,
    "payment delay for nine months and above": 9
}

# Payment Status section
with st.expander("Payment Status"):
    repay_status = []
    for i, month in enumerate(["April", "May", "June", "July", "August", "September"]):
        selected_category = st.selectbox(f"{month}:", list(repay_status_mapping.keys()), key=f"repay_status_{i}")
        numerical_value = repay_status_mapping[selected_category]
        repay_status.append(numerical_value)

# Bill Amounts section
with st.expander("Bill Amounts"):
    bill_amounts = []
    for i, month in enumerate(["April", "May", "June", "July", "August", "September"]):
        value = st.number_input(f"{month}:", min_value=0, key=f"bill_amount_{i}")
        bill_amounts.append(value)

# Previous Payments section
with st.expander("Previous Payments"):
    previous_payments = []
    for i, month in enumerate(["April", "May", "June", "July", "August", "September"]):
        value = st.number_input(f"{month}:", min_value=0, key=f"previous_payments_{i}")
        previous_payments.append(value)

# Get the column order from the training data
column_order = [
    'LIMIT_BAL', 'AGE', 'PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5',
    'PAY_6', 'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4',
    'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3',
    'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6', 'SEX_1', 'SEX_2', 'EDUCATION_1',
    'EDUCATION_2', 'EDUCATION_3', 'EDUCATION_4', 'MARRIAGE_1', 'MARRIAGE_2',
    'MARRIAGE_3'
]

# Prediction button
if st.button("Predict"):
    # Preprocess the input data
    input_data = {
        "AGE": age,
        "LIMIT_BAL": limit_bal,
        "PAY_6": repay_status[0],
        "PAY_5": repay_status[1],
        "PAY_4": repay_status[2],
        "PAY_3": repay_status[3],
        "PAY_2": repay_status[4],
        "PAY_1": repay_status[5],
        "BILL_AMT6": bill_amounts[0],
        "BILL_AMT5": bill_amounts[1],
        "BILL_AMT4": bill_amounts[2],
        "BILL_AMT3": bill_amounts[3],
        "BILL_AMT2": bill_amounts[4],
        "BILL_AMT1": bill_amounts[5],
        "PAY_AMT6": previous_payments[0],
        "PAY_AMT5": previous_payments[1],
        "PAY_AMT4": previous_payments[2],
        "PAY_AMT3": previous_payments[3],
        "PAY_AMT2": previous_payments[4],
        "PAY_AMT1": previous_payments[5],
        "SEX_1": 1 if gender == "Male" else 0,
        "SEX_2": 1 if gender == "Female" else 0,
        "EDUCATION_1": 1 if education == "Graduate School" else 0,
        "EDUCATION_2": 1 if education == "University" else 0,
        "EDUCATION_3": 1 if education == "High School" else 0,
        "EDUCATION_4": 1 if education == "Others" else 0,
        "MARRIAGE_1": 1 if marriage == "Married" else 0,
        "MARRIAGE_2": 1 if marriage == "Single" else 0,
        "MARRIAGE_3": 1 if marriage == "Others" else 0
    }
    input_df = pd.DataFrame([input_data], columns=column_order)

    # Make a prediction
    prediction = model.predict(input_df)


    # Display the prediction result
    prediction_text = "The user won't be a defaulter next month" if prediction == 0 else "The user will be a defaulter next month"
    prediction_background = "lightgreen" if prediction == 0 else "lightcoral"

    st.subheader("Prediction:")
    st.write(f'<div style="background-color:{prediction_background}; padding: 10px; border-radius: 5px;">'
         f'<p style="font-weight:bold;">{prediction_text}</p>'
         f'</div>', unsafe_allow_html=True)
    
    
# Add your name
st.write("<div style='text-align:right; color:#666; font-size:15px;'>Created by Dnyanesh Yeole</div>", unsafe_allow_html=True)

