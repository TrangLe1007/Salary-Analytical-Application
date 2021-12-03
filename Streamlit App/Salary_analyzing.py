import streamlit as st
from PIL import Image
import pandas as pd


#Sidebar
#Bio
img=Image.open('E:\LAB\LAB\Thesis\Code App\Streamlit App\scott-graham-OQMZwNd3ThU-unsplash.jpg')
st.sidebar.image(img)
st.sidebar.markdown("#### About")
st.sidebar.success("This web app helps you to analyze the salary of IT jobs in the Vietnam labor market")
st.sidebar.markdown("#### Instruction")
st.sidebar.warning("Enter the required fields below and click on the 'Check' button to check")
#data
df =pd.read_csv('E:\LAB\LAB\Thesis\Code App\Data Cleaning\ITviec_database_without_duplicate_check.csv')
#form
with st.sidebar.form(key='form'):
    jobs= df['Title_job'].unique()
    question1= st.selectbox("What kind of IT job do you want to check?",jobs)
    cities= ["Ha noi","Ho Chi Minh","Da Nang","Others"]
    question2= st.selectbox('Which city do you want to work', cities)

    submit_button = st.form_submit_button(label='Check')
    if submit_button:
        st.success("Checked successfully. Please check the result on the main page!")  

# Main page

#title
st.title("Salary Analytical Application")
st.write("Salary analytic for : {}".format(question1))

#filter data
df_selected=df.loc[df['Title_job'] == question1] 
df_selected_city=df.loc[(df['Address'] == question2) & (df['Title_job'] == question1)]
df_selected_city_min=df.loc[(df['Address'] == question2) & (df['Title_job'] == question1)& (df['Salary'] != 0)]

#data visulaziation


count_job_city = df_selected[['Title_job','Address']].groupby('Address').agg({'Title_job': 'count'})
average_job_city = df_selected.groupby('Address').agg({'Salary': 'mean'})
min = df_selected_city_min.agg({'Salary': 'min'})
max = df_selected_city.agg({'Salary': 'max'})

#The min max salary
st.subheader("The min salary for : {} in {}".format(question1, question2))
st.write(min)
st.subheader("The max salary for : {} in {}".format(question1, question2))
st.write(max)

#table detail information
st.subheader('The detail job information')
st.dataframe(df_selected_city)

#average salary
st.subheader('The average salary by location')
st.write('Currency: USD')
#st.write(average_job_city)
st.bar_chart(average_job_city)

#amount of job
st.subheader('The number of job by location')
#st.write(count_job_city)
st.bar_chart(count_job_city)













