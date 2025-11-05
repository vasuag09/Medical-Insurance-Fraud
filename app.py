import joblib
import pandas as pd
import streamlit as st
model = joblib.load("model/fraud_model.pkl")
preprocessor = joblib.load("model/preprocessor.pkl")

st.title("🩺 Health Insurance Fraud Detection (Colab Inline Demo)")

claim_amount = st.number_input("Claim Amount ($)", value=5000.0)
patient_age = st.number_input("Patient Age", value=35)
patient_income = st.number_input("Patient Income ($)", value=40000.0)
claim_type = st.selectbox("Claim Type", ["Inpatient", "Outpatient", "Emergency"])
submission_method = st.selectbox("Submission Method", ["Online", "Paper", "Phone"])
claim_status = st.selectbox("Claim Status", ["Submitted", "Pending", "Approved", "Denied"])

if st.button("🔍 Predict Fraud Risk"):
    input_df = pd.DataFrame({
        "ClaimAmount": [claim_amount],
        "PatientAge": [patient_age],
        "PatientIncome": [patient_income],
        "ClaimType": [claim_type],
        "ClaimSubmissionMethod": [submission_method],
        "ClaimStatus": [claim_status],
            "PatientGender": ["Male"],  # default placeholder
    "PatientMaritalStatus": ["Single"],  # placeholder
    "PatientEmploymentStatus": ["Employed"],  # placeholder
    "ProviderSpecialty": ["General"],  # placeholder
    "Cluster": [0]  # numeric cluster label
    })
    X_processed = preprocessor.transform(input_df)
    prediction = model.predict(X_processed)[0]
    prob = model.predict_proba(X_processed)[0][1]
    st.write(f"**Fraud Probability:** {prob:.2%}")
    st.success("Legitimate" if prediction == 0 else "🚨 Fraudulent Claim Detected")
