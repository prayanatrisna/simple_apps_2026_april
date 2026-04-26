import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

st.set_page_config(
		page_title = "Global Weather",
		layout = 'wide'
	)

########### load data
data = pd.read_csv("Global_Weather.csv")
subdata = data.copy()
joblib.load('model_tersimpan.pkl')

########### sidebar + widget
with st.sidebar:
	country = st.text_input(
			"Country"
		)
	
	wind_degree_min = st.slider(
			"Minimum wind degree",
			max_value = 500,
			min_value = 0,
			value = 0
		)
	wind_degree_max = st.slider(
			"Maximum wind degree",
			max_value = 500,
			min_value = 0,
			value = 500
		)

########### filter
if country:
	subdata = subdata.query('country == @country')

subdata = subdata.query('wind_degree >= @wind_degree_min')
subdata = subdata.query('wind_degree <= @wind_degree_max')

########### visualisasi
fig1 = px.scatter(
	subdata, x = 'air_quality_Sulphur_dioxide',
	y = 'air_quality_PM10')
fig2 = px.line(
	subdata, x = 'last_updated',
	y = 'gust_kph')
fig3 = px.scatter(
	subdata, x = 'air_quality_Ozone',
	y = 'visibility_km')
fig4 = px.scatter(
	subdata, x = 'feels_like_fahrenheit',
	y = 'cloud')

########### layouting
st.title('Global Weather')
col1, col2 = st.columns((1,1))
col3, col4, col5 = st.columns((1,1,2))

with col1:
	st.dataframe(subdata)

with col2:
	st.code('def func(x: str, y: int) -> int: return x')

with col3:
	st.plotly_chart(fig2)

with col4:
	st.markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

with col5:
	st.plotly_chart(fig4)