
import streamlit
import pandas as pd
import requests

streamlit.title('LETF Spread Dashboard')

fruits = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.multiselect('pick fruits or die:', list(fruits.index))
streamlit.dataframe(fruits)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
while 1:
  for i in range(10):
    streamlit.text(str(i))

