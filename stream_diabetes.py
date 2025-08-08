import pickle
import streamlit as st
import numpy as np

# Membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul web
st.title('Prediksi Diabetes')
st.write("Masukkan data pasien untuk memprediksi kemungkinan diabetes.")

# Input data dengan contoh angka valid untuk pengujian
Pregnancies = st.text_input('Pregnancies', '2')
Glucose = st.text_input('Glucose', '120')
BloodPressure = st.text_input('BloodPressure', '70')
SkinThickness = st.text_input('SkinThickness', '20')
Insulin = st.text_input('Insulin', '80')  # Tambahan input
BMI = st.text_input('BMI', '25.0')
DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction', '0.5')
Age = st.text_input('Age', '30')

diabetes_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Prediksi'):
    try:
        # Konversi input menjadi numerik
        inputs = np.array([[float(Pregnancies), float(Glucose), float(BloodPressure),
                            float(SkinThickness), float(Insulin), float(BMI),
                            float(DiabetesPedigreeFunction), float(Age)]])

        # Lakukan prediksi
        diabetes_prediksi = diabetes_model.predict(inputs)
        
        if diabetes_prediksi[0] == 1:
            diabetes_diagnosis = 'Pasien Terkena Diabetes'
        else:
            diabetes_diagnosis = 'Pasien tidak terkena Diabetes'
            
        st.success(diabetes_diagnosis)
    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
