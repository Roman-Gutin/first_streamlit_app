
import streamlit
import pandas as pd
import requests
import snowflake.connector
from urlib.error import URLError

streamlit.title('LETF Spread Dashboard')

fruits = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.multiselect('pick fruits or die:', list(fruits.index))
streamlit.dataframe(fruits)

fruit = streamlit.text_input('What fruit tickles your fancy?', 'Kiwi')
fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit}")
streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The Fruit Load List:")
streamlit.dataframe(my_data_row)
add_my_fruit = streamlit.text_input('What fruit tickles your fancy Part 2?', 'jackfruit')
my_cur.execcute("insert into fruit_load_list values ('from streamlist')")
streamlit.stop()
              
