import streamlit
streamlit.title("My parents New Healthy Diner")
streamlit.header ("Breakfast Menu")
streamlit.text("Omega 3 & Bluberry oatmeal")
streamlit.text("Hard boiled egg")
streamlit.header ("Build your own smoothie")

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected =streamlit.multiselect("pick some fruits :", list(my_fruit_list.index),['Avacado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)


streamlit.header("Fruityvice Fruit Advice!")


# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("My fruit load list contains:")
streamlit.text(my_data_row)
