from dotenv import load_dotenv
load_dotenv()  # Load environment variables

import os
import streamlit as st
import mysql.connector
from mysql.connector import Error
import google.generativeai as generativeai
import pandas as pd

# Configure the Gemini model
generativeai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt to convert English to SQL
prompt = """
You are an expert in converting English questions to SQL queries!

Your task is to convert natural language questions into MySQL queries for a database containing a single table named STUDENTS.

Table Schema:
STUDENTS(NAME VARCHAR, garde VARCHAR, SECTION VARCHAR)

Follow these rules strictly:
1.  Analyze the user's question to understand the intent.
2.  Identify the necessary SQL clauses (SELECT, WHERE, GROUP BY, ORDER BY, COUNT, DISTINCT, etc.).
3.  Generate a single, valid, and efficient MySQL query.
4.  Enclose all string literals within double quotes (e.g., WHERE CLASS="Data Science").
5.  Assume case-insensitive matching for string comparisons where appropriate (standard comparison or use LOWER() if needed).
6.  Format the SQL query clearly.
7.  Output **only** the generated SQL query.
8.  **Do not** include any explanations, introductory text, comments, or markdown formatting (like ```sql or ```).
9.  **Do not** include the word 'sql' or 'query' in your response.

Example 1:
Question: "How many students are there in total?"
SQL: SELECT COUNT(*) FROM STUDENTS;

Example 2:
Question: "Show me the names of all students in the Science class, section A."
SQL: SELECT NAME FROM STUDENTS WHERE SUBJECT="Science" AND SECTION="A";

Example 3:
Question: "List all unique classes available."
SQL: SELECT DISTINCT CLASS FROM STUDENTS;

Now, convert the following question:
Question: "{question}"

"""

prompt2="""
You are a Python data manipulation expert.

Your job is to convert English instructions into **accurate** and **concise** Pandas or NumPy code.

- Do not include explanations, comments, or the word "Python" in your response.
- Only return the code block as if it were part of a working script.
- Use best practices with Pandas and NumPy syntax.
- The variable `df` refers to the DataFrame, and `np` refers to NumPy.
- Assume all necessary libraries like pandas and numpy are already imported.

Examples:

Instruction: Get the number of rows in the DataFrame  
Output: df.shape[0]

Instruction: Calculate the mean of the column 'Sales'  
Output: df['Sales'].mean()

Instruction: Drop rows with missing values  
Output: df.dropna()

Instruction: Get the unique values in the column 'Country'  
Output: df['Country'].unique()

Instruction: Replace all NaN values in the column 'Price' with 0  
Output: df['Price'].fillna(0, inplace=True)

Instruction: Filter rows where 'Age' is greater than 30  
Output: df[df['Age'] > 30]

Instruction: Sort the DataFrame by the column 'Salary' in descending order  
Output: df.sort_values(by='Salary', ascending=False)

Instruction: Create a new column 'Total' as product of 'Quantity' and 'Price'  
Output: df['Total'] = df['Quantity'] * df['Price']

Instruction: Rename the column 'OldName' to 'NewName'  
Output: df.rename(columns={'OldName': 'NewName'}, inplace=True)

Instruction: Reset the DataFrame index  
Output: df.reset_index(drop=True, inplace=True)

Instruction: Get summary statistics of all numeric columns  
Output: df.describe()

Instruction: Convert the column 'Date' to datetime  
Output: df['Date'] = pd.to_datetime(df['Date'])

Instruction: Create a NumPy array of shape (3, 4) filled with zeros  
Output: np.zeros((3, 4))

Instruction: Calculate the standard deviation of the column 'Marks'  
Output: df['Marks'].std()

Instruction: Check if there are any missing values  
Output: df.isnull().any()

Now, convert the following question:
Question: "{question}"

"""

# Load Gemini model and generate SQL query
def load_gemini_model(prompt,prompt2, question):
    model = generativeai.GenerativeModel(model_name="models/gemini-1.5-pro")
    response = model.generate_content([prompt,prompt2, question])
    return response.text.strip()

# Streamlit UI
with st.sidebar:
    st.set_page_config(page_title="SQL Query Generator", page_icon="📊",layout="wide")
    st.title("💬 Natural Language to SQL Query Generator")
    st.write("Ask a question in plain English and get the SQL query with result!")

# User input
question = st.sidebar.text_input("Enter your question", "How many entries of records are present?")
submit_button = st.sidebar.button("Submit")

# When the button is clicked
if submit_button:
    # Get the SQL query from Gemini
    sql_query = load_gemini_model(prompt,prompt2, question)
    st.subheader("Generated SQL Query:")
    st.code(sql_query, language="sql")

    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT"))
        )

        if connection.is_connected():
            st.success("✅ Connected to the MySQL database.")
            # Use pandas to fetch data
            data = pd.read_sql(sql_query, connection)
            st.subheader("Query Results:")
            st.dataframe(data)

        connection.close()

    except Error as e:
        st.error(f"❌ MySQL Error: {e}")
    except Exception as e:
        st.error(f"⚠️ Execution Error: {e}")
        st.write("An error occurred while executing the SQL query.")
    finally:    
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            st.success("🔒 Connection closed.")
