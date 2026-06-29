import streamlit as st
import pandas as pd
import pickle

# Load saved model, scaler, and training columns
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.set_page_config(page_title="AttriSense AI", layout="wide")

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #111827 0%, #020617 45%, #020617 100%);
    color: white;
}

.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
}

.main-title {
    font-size: 58px;
    font-weight: 900;
    color: #ffffff;
    margin-bottom: 0px;
    line-height: 1.1;
}

.gradient-text {
    background: linear-gradient(90deg, #a855f7, #3b82f6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    color: #a5b4fc;
    font-size: 19px;
    margin-top: 10px;
    margin-bottom: 35px;
}

.metric-card {
    background: linear-gradient(135deg, rgba(88,28,135,0.45), rgba(15,23,42,0.95));
    border: 1px solid rgba(168,85,247,0.35);
    border-radius: 18px;
    padding: 24px;
    box-shadow: 0 0 35px rgba(168,85,247,0.12);
    min-height: 155px;
}

.metric-card-blue {
    background: linear-gradient(135deg, rgba(30,64,175,0.45), rgba(15,23,42,0.95));
    border: 1px solid rgba(59,130,246,0.35);
}

.metric-card-green {
    background: linear-gradient(135deg, rgba(6,95,70,0.45), rgba(15,23,42,0.95));
    border: 1px solid rgba(52,211,153,0.35);
}

.metric-card-yellow {
    background: linear-gradient(135deg, rgba(146,64,14,0.45), rgba(15,23,42,0.95));
    border: 1px solid rgba(251,191,36,0.35);
}

.metric-label {
    color: #c4b5fd;
    font-size: 17px;
    font-weight: 700;
}

.metric-value {
    color: white;
    font-size: 40px;
    font-weight: 900;
    margin-top: 8px;
}

.metric-caption {
    color: #cbd5e1;
    font-size: 14px;
    margin-top: 8px;
}

.info-card {
    background: linear-gradient(90deg, rgba(15,23,42,0.95), rgba(49,46,129,0.35));
    border: 1px solid rgba(99,102,241,0.35);
    border-radius: 18px;
    padding: 28px;
    margin-top: 28px;
    margin-bottom: 28px;
    box-shadow: 0 0 35px rgba(59,130,246,0.10);
}

.result-card {
    background: rgba(15,23,42,0.85);
    border: 1px solid rgba(148,163,184,0.25);
    border-radius: 18px;
    padding: 26px;
    margin-top: 18px;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #a855f7, #2563eb);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 0.95rem 1rem;
    font-size: 20px;
    font-weight: 800;
    margin-top: 20px;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #9333ea, #1d4ed8);
    color: white;
    border: none;
}

hr {
    border-color: rgba(148,163,184,0.25);
}

.footer {
    text-align: center;
    color: #94a3b8;
    padding: 25px;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div>
    <div class="main-title">AttriSense <span class="gradient-text">AI</span></div>
    <div class="subtitle">AI-Powered Employee Attrition Prediction & HR Analytics</div>
</div>
""", unsafe_allow_html=True)

# Metric Cards
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">👥 Employees</div>
        <div class="metric-value">1470</div>
        <div class="metric-caption">Total Employees</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card metric-card-blue">
        <div class="metric-label">🤖 Best Model</div>
        <div class="metric-value">SVM</div>
        <div class="metric-caption">Selected Model</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card metric-card-green">
        <div class="metric-label">🎯 Accuracy</div>
        <div class="metric-value">80.95%</div>
        <div class="metric-caption">Model Accuracy</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-card metric-card-yellow">
        <div class="metric-label">📈 ROC-AUC</div>
        <div class="metric-value">0.804</div>
        <div class="metric-caption">Model ROC-AUC</div>
    </div>
    """, unsafe_allow_html=True)

# Insight Card
st.markdown("""
<div class="info-card">
    <h3>AI-Powered Insights</h3>
    <p>
    AttriSense AI helps identify employees at risk of leaving, enabling HR teams
    to take proactive and data-driven retention actions.
    </p>
</div>
""", unsafe_allow_html=True)

# Employee Information
st.markdown("## 👥 Employee Information")
st.caption("Enter employee details to predict attrition risk.")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", 18, 60, 30)
    monthly_income = st.number_input("Monthly Income", 1000, 20000, 5000)
    daily_rate = st.number_input("Daily Rate", 100, 1500, 800)
    hourly_rate = st.number_input("Hourly Rate", 30, 100, 60)
    monthly_rate = st.number_input("Monthly Rate", 2000, 27000, 12000)

with col2:
    distance = st.number_input("Distance From Home", 1, 30, 5)
    total_years = st.number_input("Total Working Years", 0, 40, 8)
    years_company = st.number_input("Years At Company", 0, 40, 5)
    years_role = st.number_input("Years In Current Role", 0, 20, 3)
    years_manager = st.number_input("Years With Current Manager", 0, 20, 3)

with col3:
    job_satisfaction = st.selectbox("Job Satisfaction", [1, 2, 3, 4])
    environment_satisfaction = st.selectbox("Environment Satisfaction", [1, 2, 3, 4])
    work_life = st.selectbox("Work Life Balance", [1, 2, 3, 4])
    job_involvement = st.selectbox("Job Involvement", [1, 2, 3, 4])
    performance = st.selectbox("Performance Rating", [3, 4])

st.markdown("## 💼 Work Details")

col4, col5, col6 = st.columns(3)

with col4:
    overtime = st.selectbox("OverTime", ["No", "Yes"])
    business_travel = st.selectbox("Business Travel", ["Travel_Rarely", "Travel_Frequently", "Non-Travel"])
    department = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])

with col5:
    job_role = st.selectbox(
        "Job Role",
        [
            "Sales Executive",
            "Research Scientist",
            "Laboratory Technician",
            "Manufacturing Director",
            "Healthcare Representative",
            "Manager",
            "Sales Representative",
            "Research Director",
            "Human Resources"
        ]
    )
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
    gender = st.selectbox("Gender", ["Female", "Male"])

with col6:
    education_field = st.selectbox(
        "Education Field",
        ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Human Resources", "Other"]
    )
    education = st.selectbox("Education Level", [1, 2, 3, 4, 5])
    job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])

# Prepare input
input_raw = pd.DataFrame({
    "Age": [age],
    "BusinessTravel": [business_travel],
    "DailyRate": [daily_rate],
    "Department": [department],
    "DistanceFromHome": [distance],
    "Education": [education],
    "EducationField": [education_field],
    "EnvironmentSatisfaction": [environment_satisfaction],
    "Gender": [gender],
    "HourlyRate": [hourly_rate],
    "JobInvolvement": [job_involvement],
    "JobLevel": [job_level],
    "JobRole": [job_role],
    "JobSatisfaction": [job_satisfaction],
    "MaritalStatus": [marital_status],
    "MonthlyIncome": [monthly_income],
    "MonthlyRate": [monthly_rate],
    "NumCompaniesWorked": [1],
    "OverTime": [overtime],
    "PercentSalaryHike": [15],
    "PerformanceRating": [performance],
    "RelationshipSatisfaction": [3],
    "StockOptionLevel": [1],
    "TotalWorkingYears": [total_years],
    "TrainingTimesLastYear": [2],
    "WorkLifeBalance": [work_life],
    "YearsAtCompany": [years_company],
    "YearsInCurrentRole": [years_role],
    "YearsSinceLastPromotion": [1],
    "YearsWithCurrManager": [years_manager]
})

input_encoded = pd.get_dummies(input_raw, drop_first=True)
input_encoded = input_encoded.reindex(columns=columns, fill_value=0)
input_scaled = scaler.transform(input_encoded)

# Prediction
if st.button("🚀 Run AI Prediction"):
    probability = model.predict_proba(input_scaled)[0][1]

    st.markdown("## Prediction Result")

    if probability >= 0.70:
        risk_level = "High Risk"
        st.error(f"🔴 {risk_level} of Attrition — Probability: {probability:.2%}")
        recommendation = "Schedule an HR retention meeting and review workload, compensation, and job satisfaction."

    elif probability >= 0.40:
        risk_level = "Medium Risk"
        st.warning(f"🟡 {risk_level} of Attrition — Probability: {probability:.2%}")
        recommendation = "Monitor the employee and improve engagement, work-life balance, and career development opportunities."

    else:
        risk_level = "Low Risk"
        st.success(f"🟢 {risk_level} of Attrition — Probability: {probability:.2%}")
        recommendation = "Continue regular engagement and employee satisfaction monitoring."

    st.markdown(f"""
    <div class="result-card">
        <h3>AI Analysis Summary</h3>
        <p><b>Risk Level:</b> {risk_level}</p>
        <p><b>Risk Probability:</b> {probability:.2%}</p>
        <p><b>Recommended Action:</b> {recommendation}</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Business Recommendations
st.markdown("## Business Recommendations")
st.write("""
- Monitor employees with high overtime and low satisfaction.
- Improve work-life balance and career development opportunities.
- Review compensation for employees with high attrition risk.
- Support employees in early years at the company to improve retention.
""")

# Footer
st.markdown("""
<div class="footer">
    <h4>Developed by <b>Norah Altimyat</b></h4>
    <p>Data Science | Machine Learning | Python</p>
    <p>© 2026 AttriSense AI</p>
</div>
""", unsafe_allow_html=True)
