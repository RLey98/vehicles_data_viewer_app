import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
car_data['manufactured'] = car_data['model'].str.split().str[0]

st.title('Vehicle Ads Data')

st.header('Data vehicles viewer')

st.dataframe(car_data)

st.header('Vehicle types by manufacturer')
data_grouped = car_data.groupby("manufactured")["type"].value_counts().reset_index()
fig = px.bar(data_grouped, x="manufactured", y="count", color="type")
st.plotly_chart(fig, use_container_width=True)

st.header('Relationship between model year and odometer by transmission type.')
fig = px.scatter(car_data, x="model_year", y="odometer", color="transmission", symbol="transmission")
st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Build histogram')  
if build_histogram:
    # escribir un mensaje
    st.header(f"Histogram of {car_data.columns[3]} vs {car_data.columns[1]}")
    fig = px.histogram(car_data, x="model_year", color="condition")
    st.plotly_chart(fig, use_container_width=True)

st.header('Compare price distribution between manufactrers')
manufacturer_1 = st.selectbox("Select manufacturer 1", options=car_data['manufactured'].unique())
manufacturer_2 = st.selectbox("Select manufacturer 2", options=car_data['manufactured'].unique())

df_grouped = car_data[(car_data['manufactured'] == manufacturer_1)|(car_data['manufactured'] == manufacturer_2)]

fig = px.histogram(df_grouped, x="price", color=df_grouped['manufactured'])
st.plotly_chart(fig, use_container_width=True)

toggle_fuel = st.toggle("Fuel types by manufacturer chart")
if toggle_fuel:
    st.header('Fuel types by manufacturer')
    df_fuel_grouped = car_data.groupby("manufactured")["fuel"].value_counts().reset_index()
    fig = px.bar(df_fuel_grouped, x="manufactured", y="count", color="fuel")
    st.plotly_chart(fig, use_container_width=True)
    
st.link_button("Go to repository", "https://github.com/RLey98/vehicles_data_viewer_app")
