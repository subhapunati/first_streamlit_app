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
