import pickle 
import numpy as np
import streamlit as st

model = pickle.load(open('Customertravel.sav', 'rb'))

st.title('Prediksi Pelanggan Perjalanan')

#input
age = st.number_input('Umur')
flayer = st.number_input('Penerbang Sering')
AnnualIncome = st.number_input ('Kelas Penghasilan Tahunan')
service = st.number_input('Layanan Dipilih')
mediasocial = st.number_input('Akun Disinkronkan Ke Media Sosial')
booked = st.number_input('Booking')

travel_diagnosis = ''

if st.button('Prediksi Analisis Pelanggan Perjalanan'):
	prediksi = model.predict([[age, flayer, AnnualIncome,  service, mediasocial, booked]])
	if(prediksi[0] == 1):
		travel_diagnosis = 'target Tercapai'
	else :
		travel_diagnosis = 'target tidak tercapai'
st.success(travel_diagnosis)
