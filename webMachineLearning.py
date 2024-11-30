import pickle
import streamlit as st
import pandas as pd
import numpy as np
from streamlit import button

model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))
# open file csv
df1 = pd.read_csv('CarPrice.csv')
st.markdown("<h1 style='text-align: center; color: red;'> Prediksi Harga Mobil </h1>", unsafe_allow_html=True)

def Dashboard():
    dataset()

def Prediksi():
    model_prediksi()

def dataset():
    st.header("Dataset")
    st.dataframe(df1)

    st.write("Gragik Highway-mpg")
    chart_highwaympg = (df1['highwaympg'])
    st.line_chart(chart_highwaympg)

    st.write("Grafik curbeweight")
    chart_curbeweight = (df1['curbweight'])
    st.line_chart(chart_curbeweight)

    st.write("Grafik horsepower")
    chart_horsepower = pd.DataFrame(df1, columns=["horsepower"])
    st.line_chart(chart_horsepower)

def model_prediksi():
    # input nilai dari variable independent
    highwaympg = st.number_input("highwaympg", 0, 10000)
    curbweight = st.number_input("curbweight", 0, 10000)
    horsepower = st.number_input("horsepower", 0, 10000)

    if st.button('Prediksi'):
        # Prediksi variable yang telah diinputkan
        car_prediction = model.predict([[highwaympg, curbweight, horsepower]])

        # Convert ke string
        harga_mobil_str = np.array(car_prediction)
        harga_mobil_float = float(harga_mobil_str[0])

        # Tampilkan hasil prediksi
        harga_mobil_formated = f"${harga_mobil_float:,.2f}"

        st.write(f"Prediksi Harga Mobil {harga_mobil_formated}")

navPage = st.navigation([st.Page(Dashboard), st.Page(Prediksi)])
navPage.run()

st.caption("Project by Bagus Prasetyo")








