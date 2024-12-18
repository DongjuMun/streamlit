import streamlit as st
import pandas as pd
import numpy as np

st.title('Police Incident Reports from 2018 to 2020 in San Francisco')

df = pd.read_csv("Policev1.csv")


st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018')

mapa = pd.DataFrame()
mapa['Data'] = df['Incident Date']
mapa['Day'] = df['Incident Day of Week']
mapa['Police District'] = df['Police District']
mapa['Neighborhood'] = df['Analysis Neighborhood']
mapa['Incident Category'] = df['Incident Category']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitud']
mapa['lon'] = df['Logitud']
mapa = mapa.dropna()
