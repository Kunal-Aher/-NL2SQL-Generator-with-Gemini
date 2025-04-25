from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables
import os
import streamlit as st
import mysql.connector
from mysql.connector import Error
import google.generativeai as generativeai
import pandas as pd

generativeai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# create a function to load  gemini model
def load_gemini_model(prompt,question):
    model = generativeai.GenerativeModel(model_name="models/gemini-1.5-pro")

    response = model.generate_content([prompt, question])
    return response.text

def read_sql_query(sql_query):
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=os.getenv("DB_PORT")
    )
    if connection.is_connected():
        print("Connection successful")
    else:
        print("Connection failed")
        return None
    cursor = connection.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return rows

def get_sql_query(sql_query,connection):
    cursor = connection.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    question=st.text_input("Enter your question here", "How many entries of records are present?")
    submit_button = st.button("Submit")
    if submit_button:
        # Load the Gemini model and generate the SQL query
        sql_query = load_gemini_model(prompt, question)
        st.subheader("Generated SQL Query:")
        st.code(sql_query, language="sql")
        st.write("SQL Query:")
    connection.commit()
    connection.close()

    return rows
    
    

prompt = """
You are a SQL expert. You will be given a SQL query and you will explain the query in detail.
You will also provide the output of the query.
You will also provide the schema of the table used in the query.
You will also provide the data types of the columns in the table.
You will also provide the primary key of the table.
You will also provide the foreign key of the table.
You will also provide the indexes of the table.
You will also provide the constraints of the table.
You will also provide the relationships of the table with other tables.
You will also provide the data in the table.
You will also provide the data in the table in a tabular format.
You will also provide the data in the table in a json format.
You will also provide the data in the table in a csv format.
You will also provide the data in the table in a xml format.
You will also provide the data in the table in a html format.
You will also provide the data in the table in a markdown format.
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENTS and has the following columns - NAME, CLASS, 
SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
the SQL command will be something like this SELECT COUNT(*) FROM STUDENTS ;
\nExample 2 - Tell me all the students studying in Data Science class?, 
the SQL command will be something like this SELECT * FROM STUDENTS
where CLASS="Data Science"; 
also the sql code should not have ``` in beginning or end and sql word in output """

# CREATING STREAMLIT APP
st.set_page_config(page_title="SQL Query Generator", page_icon=":guardsman:", layout="wide")
st.title("SQL Query Generator")
st.subheader("Generate SQL Queries from English Questions")
st.write("This app generates SQL queries from English questions using the Gemini model.")
st.write("The app uses the Google Gemini model to generate SQL queries from English questions.")
st.write("The app uses the MySQL database to execute the SQL queries.")
st.write("The app uses the MySQL database to execute the SQL queries and display the results.")

question = st.text_input("Enter your question here", "How many entries of records are present?")
submit_button = st.button("Submit")
if submit_button:
    # Load the Gemini model and generate the SQL query
    sql_query = load_gemini_model(prompt, question)
    st.subheader("Generated SQL Query:")
    st.code(sql_query, language="sql")
    st.write("SQL Query:")
    # Establish the database connection
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT")
        )
        if connection.is_connected():
            st.success("Connection to the database was successful.")
        else:
            st.error("Connection to the database failed.")
    except Error as e:
        st.error(f"Error: {e}")
    # Use the connection to fetch data
        data = pd.read_sql(sql_query,connection)
        connection.close()  # Close the connection after use
        st.write(sql_query)
        st.subheader("SQL Query Result is:")
    except Exception as e:
        st.error(f"Error: {e}")
        st.write("An error occurred while executing the SQL query.")
    # Display the result in a table format
    for row in data:
        print(row)
        # Display the result in a table format
        st.write(row)
        st.write("Data fetched successfully.")
    
    # Create a connection to the MySQL database