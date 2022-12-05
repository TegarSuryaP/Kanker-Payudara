import pickle
import streamlit as st

breast_model = pickle.load(open('breast_model.sav', 'rb'))

st.title('Prediksi Kanker Payudara')

col1, col2, col3 = st.columns(3)

with col1 :
    id = st.text_input ('Input Nilai id')
with col2 :
    clump_thickness = st.text_input ('Input Nilai clump thickness')
with col3 :
    size_uniformity = st.text_input ('Input Nilai size uniformity')
with col1 :
    shape_uniformity = st.text_input ('Input Nilai shape uniformity')
with col2 :
    marginal_adhesion = st.text_input ('Input Nilai marginal adhesion')
with col3 :
    epithelial_size = st.text_input ('Input Nilai epithelial size')
with col1 :
    bare_nucleoli = st.text_input ('Input Nilai bare nucleoli')
with col2 :
    bland_chromatin = st.text_input ('Input Nilai bland chromatin')
with col3 :
    normal_nucleoli = st.text_input ('Input Nilai normal_nucleoli')
with col1 :
    mitoses = st.text_input ('Input Nilai mitoses')

breast_diagnosis = ''

if st.button('Test Prediksi Kanker Payudara') :
    breast_prediction = breast_model.predict([[id, clump_thickness, size_uniformity, shape_uniformity, marginal_adhesion, epithelial_size, bare_nucleoli, bland_chromatin, normal_nucleoli, mitoses]])

    if (breast_prediction[0] == 2):
        breast_diagnosis = 'Kanker Jinak'
    else : breast_diagnosis = 'Kanker Ganas'

    if (breast_prediction[0] == 4):
         breast_diagnosis = 'Kanker Ganas'
    else : breast_diagnosis = 'Kanker Jinak'
st.success(breast_diagnosis)