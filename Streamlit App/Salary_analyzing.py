import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib
# import seaborn as sns

#Sidebar

#Bio
img=Image.open('E:\LAB\LAB\Thesis\Code App\Streamlit App\scott-graham-OQMZwNd3ThU-unsplash.jpg')
st.sidebar.image(img)
st.sidebar.markdown("#### About")
st.sidebar.success("This web app helps you to analyze the salary of IT jobs in the Vietnam labor market")
st.sidebar.markdown("#### Instruction")
st.sidebar.warning("Enter the required fields below and click on the 'Check' button to check")

#form
with st.sidebar.form(key='form'):
    question1= st.text_input("What kind of IT job do you want to check?")
    cities= ["Ha noi","Ho Chi Minh","Da Nang","Others"]
    question2= st.selectbox('Which city do you want to work', cities)

    submit_button = st.form_submit_button(label='Check')

#Result:
    if submit_button:
        st.success("Checked successfully. Please check the result on the main page!")
    
# Main page

#title
st.title("Salary Analytical Application")
st.write("Salary analytic for : {}".format(question1))

#job_information
df=pd.read_csv('E:\LAB\LAB\Thesis\Code App\Data Cleaning\ITviec_database_without_duplicate_check.csv')
st.dataframe(df)

#data visulaziation
st.bar_chart(df['Address'])