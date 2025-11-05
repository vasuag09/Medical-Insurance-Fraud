# 🩺 Health Insurance Fraud Detection App

An **industry-level Machine Learning web application** that predicts whether a **health insurance claim** is **fraudulent** or **legitimate** based on claim and patient data.  
Built with a complete ML pipeline — from preprocessing to explainability — and deployed on **Streamlit Cloud** for interactive use.

---

## 🚀 Live Demo  
🔗 [**Try the App Here →**](https://vasuag09-medical-insurance-fraud-app-jlnqby.streamlit.app/)

---

## 🧠 Project Overview  

Insurance fraud is a major challenge for healthcare systems.  
This project leverages **Machine Learning** to automatically detect potentially fraudulent claims based on structured claim information, patient details, and provider data.

The model predicts the likelihood of fraud using both **numerical** and **categorical** inputs, while providing **interpretable results** using SHAP feature explanations.

---

## ⚙️ Tech Stack  

**Languages & Frameworks**
- Python (3.9+)
- Streamlit  
- Scikit-learn  
- Pandas, NumPy  
- Matplotlib, SHAP  

**Modeling & Explainability**
- Decision Tree Classifier (optimized via depth tuning)  
- SMOTE for class balancing  
- ROC-AUC evaluation  
- SHAP for interpretability  

**Deployment**
- Streamlit Cloud  

---

## 📊 Key Features  

✅ **Interactive Streamlit UI**  
Enter claim details (amount, type, submission method, etc.) to receive instant fraud predictions.  

✅ **End-to-End ML Pipeline**  
Includes preprocessing (encoding, scaling), model training, and inference with a serialized `.pkl` pipeline.  

✅ **Explainable AI**  
Visualizes feature impact on fraud predictions using **SHAP Summary and Force plots**.  

✅ **Production-Ready Design**  
Column validation, robust error handling, and consistent schema alignment for deployment stability.  

✅ **High Accuracy Model**  
Achieved **99% ROC-AUC** using a Decision Tree with max_depth optimization and balanced data.

---

## 🧩 Project Workflow  

### 1️⃣ Data Preprocessing  
- Cleaned and encoded categorical variables  
- Handled class imbalance with **SMOTE**  
- Split into training/testing sets (80/20)

### 2️⃣ Model Training  
- Trained multiple classifiers (Logistic Regression, Decision Tree, Random Forest)  
- Selected **Decision Tree (max_depth=2)** for interpretability & high performance  
- Evaluated via **Cross-validation** and **ROC-AUC**

### 3️⃣ Model Explainability  
- Used **SHAP** to interpret global and local predictions  
- Identified top features influencing fraud likelihood  

### 4️⃣ Deployment  
- Serialized model and preprocessor using `joblib`  
- Built interactive front-end with **Streamlit**  
- Deployed on **Streamlit Cloud** for public access  

---

## 📈 Model Performance  

| Metric | Score |
|--------|-------:|
| **Accuracy** | 99.8% |
| **Precision** | 1.00 |
| **Recall** | 0.98 |
| **F1-Score** | 0.99 |
| **ROC-AUC** | 0.99 |

---

## 🧩 Input Features  

| Feature | Type | Description |
|----------|------|-------------|
| ClaimAmount | Numeric | Total amount claimed |
| PatientAge | Numeric | Age of patient |
| PatientIncome | Numeric | Reported income |
| ClaimType | Categorical | Type of claim (Inpatient, Outpatient, Emergency) |
| ClaimSubmissionMethod | Categorical | Method (Online, Paper, Phone) |
| ClaimStatus | Categorical | Status (Submitted, Pending, Approved, Denied) |
| PatientGender | Categorical | Gender of patient |
| PatientMaritalStatus | Categorical | Marital status |
| PatientEmploymentStatus | Categorical | Employment status |
| ProviderSpecialty | Categorical | Doctor/specialist type |
| Cluster | Numeric | Derived categorical group (from feature engineering) |

---

## 🧮 Sample Prediction  

**Input:**
| ClaimAmount | ClaimType | SubmissionMethod | PatientAge | PatientIncome | ClaimStatus |
|--------------|------------|------------------|-------------|----------------|--------------|
| 25000 | Emergency | Online | 56 | 40000 | Submitted |

**Output:**
> 🚨 **Fraudulent Claim Detected**  
> Probability: **92.4%**

---

## 🧰 Installation & Local Setup  

1️⃣ Clone the repository  
```bash
git clone https://github.com/vasuag09/health-insurance-fraud-detection.git
cd health-insurance-fraud-detection
```
2️⃣ Install dependencies

pip install -r requirements.txt


3️⃣ Run the Streamlit app

streamlit run app.py


4️⃣ Visit the app in your browser at
👉 http://localhost:8501

📦 Requirements
streamlit
scikit-learn
pandas
numpy
joblib
matplotlib
shap

---

## 🧾 Project Structure
Health-Insurance-Fraud-Detection/
│
├── app.py                        # Streamlit application
├── model/
│   ├── fraud_model.pkl           # Trained model
│   ├── preprocessor.pkl          # Preprocessing pipeline
│
├── data/
│   └── Health_Insurance_Fraud_Claims.xlsx
│
├── requirements.txt
└── README.md

---

## 🧠 Insights & Learnings

Designed a robust ML pipeline using ColumnTransformers

Implemented SMOTE balancing to handle fraud imbalance

Understood feature importance and interpretability with SHAP

Built a deployable and interactive model for non-technical users

---

## 👨‍💻 Author

Vasu Agrawal
AI / ML Engineer | Data Science Student | Full-Stack Developer
📧 vasuagrawal1040@gmail.com

🔗 LinkedIn
 | GitHub


---

## 🏁 Future Enhancements

Integrate XGBoost / LightGBM for higher generalization

Add real-time fraud probability monitoring dashboard

Include authentication system for multi-user usage

Deploy via Docker + Streamlit Cloud or FastAPI backend
