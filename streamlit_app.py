import streamlit
streamlit.title("My parents New Healthy Diner")
streamlit.header ("Breakfast Menu")
streamlit.text("Omega 3 & Bluberry oatmeal")
streamlit.text("Hard boiled egg")
streamlit.header ("Build your own smoothie")

import pandas
my_fruit_list=pandas.read.csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
