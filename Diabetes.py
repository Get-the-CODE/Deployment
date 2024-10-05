

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import joblib

# loading the saved model
diabetes_model = joblib.load('LR_Classifier.pkl')


# sidebar for navigation
with st.sidebar:
    selected = option_menu('Diabetes Prediction System',
                           ['Diabetes Prediction'],
                           icons=['activity'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)

    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0.0, step=0.1)

    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0.0, step=0.1)

    with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0.0, step=0.1)

    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0.0, step=0.1)

    with col3:
        BMI = st.number_input('BMI value', min_value=0.0, step=0.1)

    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, step=0.01)

    with col2:
        Age = st.number_input('Age of the Person', min_value=0, step=1)


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        Pregnancies = float(Pregnancies)
        Glucose = float(Glucose)
        BloodPressure = float(BloodPressure)
        SkinThickness = float(SkinThickness)
        Insulin = float(Insulin)
        BMI = float(BMI)
        DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
        Age = float(Age)

        input_data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        diab_prediction = diabetes_model.predict(input_data)

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)
    