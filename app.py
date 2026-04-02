import streamlit as st
import pandas as pd
import joblib
import numpy as np

@st.cache_resource
def load_assets():
    # Memuat model terbaik
    model = joblib.load('model/gradient_boosting_model.joblib')
    
    # Memuat semua scaler 
    s_age = joblib.load('model/scaler_Age_at_enrollment.joblib')
    s_sem1_g = joblib.load('model/scaler_Curricular_units_1st_sem_grade.joblib')
    s_sem2_g = joblib.load('model/scaler_Curricular_units_2nd_sem_grade.joblib')
    
    return model, s_age, s_sem1_g, s_sem2_g

try:
    model, s_age, s_sem1_g, s_sem2_g = load_assets()
except Exception as e:
    st.error(f"Asset tidak ditemukan! Pastikan file di folder 'model' lengkap. Error: {e}")
    st.stop()

st.set_page_config(page_title="Student Dropout Predictor", layout="centered")
st.title("🎓 Prediksi Keberhasilan Mahasiswa")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📚 Akademik Semester 1")
    sem1_grade = st.number_input("Rata-rata Nilai Sem 1", 0.0, 20.0, 12.0)
    sem1_approved = st.number_input("SKS Lulus Sem 1", 0, 30, 15)
    
    st.subheader("📚 Akademik Semester 2")
    sem2_grade = st.number_input("Rata-rata Nilai Sem 2", 0.0, 20.0, 12.0)
    sem2_approved = st.number_input("SKS Lulus Sem 2", 0, 30, 15)

with col2:
    st.subheader("👤 Profil & Ekonomi")
    age = st.number_input("Usia Saat Masuk", 17, 60, 20)
    tuition = st.selectbox("UKT Lunas?", [1, 0], format_func=lambda x: "Ya" if x==1 else "Tidak")
    scholarship = st.selectbox("Penerima Beasiswa?", [1, 0], format_func=lambda x: "Ya" if x==1 else "Tidak")
    debtor = st.selectbox("Punya Hutang?", [1, 0], format_func=lambda x: "Ya" if x==1 else "Tidak")
    gender = st.selectbox("Gender", [1, 0], format_func=lambda x: "Laki-laki" if x==1 else "Perempuan")
    app_mode = st.number_input("Application Mode ID", 1, 60, 1)

if st.button("Analisis Status Mahasiswa", use_container_width=True):
    # Urutan kolom 
    feature_names = [
        'Application_mode', 'Debtor', 'Tuition_fees_up_to_date', 'Gender', 
        'Scholarship_holder', 'Age_at_enrollment', 
        'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade', 
        'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade'
    ]
    
    data = pd.DataFrame([[
        app_mode, debtor, tuition, gender, scholarship, age,
        sem1_approved, sem1_grade, sem2_approved, sem2_grade
    ]], columns=feature_names)

    # Proses Scaling 
    data['Age_at_enrollment'] = s_age.transform(data[['Age_at_enrollment']])
    data['Curricular_units_1st_sem_grade'] = s_sem1_g.transform(data[['Curricular_units_1st_sem_grade']])
    data['Curricular_units_2nd_sem_grade'] = s_sem2_g.transform(data[['Curricular_units_2nd_sem_grade']])

    # Eksekusi Prediksi
    prediction = model.predict(data)
    proba = model.predict_proba(data)

    st.markdown("---")
    if prediction[0] == 0:
        st.success(f"### HASIL: **GRADUATE** (LULUS)")
        st.write(f"Tingkat Keyakinan: **{np.max(proba)*100:.2f}%**")
    else:
        st.error(f"### HASIL: **DROPOUT** (BERISIKO)")
        st.write(f"Tingkat Keyakinan: **{np.max(proba)*100:.2f}%**")