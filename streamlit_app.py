
import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('LETF Spread Dashboard')

def get_fruity_vice_data(this_fruit_choice):
    response = requests.get(f"https://fruityvice.com/api/fruit/{this_fruit_choice}")
    return pd.json_normalize(response.json())
  
fruits = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.multiselect('pick fruits or die:', list(fruits.index))
streamlit.dataframe(fruits)
try:
  
  fruit_choice = streamlit.text_input('What fruit tickles your fancy?', 'Kiwi')
  if not fruit_choice:
    streamlit.error('Please select a fruit to get information.')
  else:
    data= get_fruity_vice_data(fruit_choice)
    streamlit.dataframe(data)
except URLErorr as e:
    streamlit.error()
    
streamlit.text("The Fruit Load List:")
def get_fruit_list():
    with my_cnx.cursor() as cur:
        cur.execute("SELECT * from fruit_load_list")
        return cur.fetchall()

if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    streamlit.dataframe(get_fruit_list())

add_my_fruit = streamlit.text_input('What fruit tickles your fancy Part 2?', 'jackfruit')


              
