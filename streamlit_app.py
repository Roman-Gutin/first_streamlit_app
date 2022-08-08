
import streamlit
import pandas as pd
import requests

streamlit.title('LETF Spread Dashboard')

fruits = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.multiselect('pick fruits or die:', list(fruits.index))
streamlit.dataframe(fruits)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
