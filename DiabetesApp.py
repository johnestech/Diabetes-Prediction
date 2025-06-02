import streamlit as st
import pandas as pd
import pickle.load

with open('Diabetes.pkl', 'rb') as mod:
    model = pickle.load(mod)

st.title('Diabetes Disease Dictector')
st.write('Prediction model for diabetes. Enter all values')

def var_input():
    pregnacies = st.selectbox('Number of Pregnacies',(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
    glucose = st.number_input('Glucose Level (Plasma glucose concentration after 2 hours in an oral glucose tolerance test')
    blood_pressure = st.number_input('Blood Pressure Level ( Diastolic blood pressure [mm Hg])')
    skin_thickness = st.number_input('Skin Thickness (Triceps skinfold thickness [mm])')
    insulin = st.number_input('Insulin Level (2-hour serum insulin [mu U/ml])')
    bmi = st.number_input('Body Mass Index (weight in kg / height in m²)')
    diabetes_pedigree = st.number_input('DiabetesPedigreeFunction (Genetic diabetes score)')
    patient_age = st.slider('Patient Age',1,90)
    
    
    data = {
        'Pregnancies': pregnacies,
        'Glucose': glucose,
        'BloodPressure': blood_pressure,
        'SkinThickness': skin_thickness,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': diabetes_pedigree,
        'Age': patient_age
    }
    data_input = pd.DataFrame(data, index=[0])
    return data_input

user_input = var_input()

if st.button('Predict'):
    predictions = model.predict(user_input)
    
    if predictions[0] == 0:
        st.success('Patient is Negative')
    elif predictions[0] == 1:
        st.error('Patient has Diabetes')
    else:
        st.info('Values cannot be Empty')
