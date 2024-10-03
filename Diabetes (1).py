


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved model
diabetes_model = pickle.load(open('LR_Classifier.pkl', 'rb'))


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
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        try:
            # Validate and convert inputs, replacing empty inputs with 0
            Pregnancies = int(Pregnancies) if Pregnancies else 0
            Glucose = float(Glucose) if Glucose else 0.0
            BloodPressure = float(BloodPressure) if BloodPressure else 0.0
            SkinThickness = float(SkinThickness) if SkinThickness else 0.0
            Insulin = float(Insulin) if Insulin else 0.0
            BMI = float(BMI) if BMI else 0.0
            DiabetesPedigreeFunction = float(DiabetesPedigreeFunction) if DiabetesPedigreeFunction else 0.0
            Age = int(Age) if Age else 0

            # Predict using the model
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

        except ValueError:
            st.error('Please enter valid numerical values for all inputs.')

    st.success(diab_diagnosis)
    