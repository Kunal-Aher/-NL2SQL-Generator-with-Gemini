# NL2SQL-Generator-with-Gemini


# 🤖 NLP to SQL, Pandas & NumPy Code Generator

Transform natural language instructions into executable **SQL queries**, **Pandas**, and **NumPy** code using **Google Gemini** (Generative AI) and an intuitive **Streamlit interface**.

![App Screenshot](https://user-images.githubusercontent.com/your-screenshot-placeholder.png)
![Screenshot 2025-04-24 223302](https://github.com/user-attachments/assets/873684a7-23e9-46d9-b45b-43324097cf35)
![Screenshot 2025-04-24 223609](https://github.com/user-attachments/assets/fb5fab3c-0fb1-4466-aa3f-6a9a9531a829)
![Screenshot 2025-04-24 223841](https://github.com/user-attachments/assets/ebb8a889-458b-482b-a60d-5a66dea028ed)
![Screenshot 2025-04-24 224738](https://github.com/user-attachments/assets/81e6a5cc-ec5c-4882-af12-765904007abd)
![Screenshot 2025-04-24 225608](https://github.com/user-attachments/assets/2620d1a7-0f8a-4ebe-b375-76b48d02cfc0)

---

## 🚀 Features

- 🔍 Convert English questions to **SQL queries**
- 🐼 Generate **Pandas**/ **NumPy** code from plain instructions
- 💬 Uses **Google Gemini AI API** for powerful NLP understanding
- 🧑‍💻 Connect to live **MySQL** database and return query results
- 🌐 Deployable on **Streamlit Cloud**, **GCP**, or any cloud platform
- 📦 Easy to extend for other libraries like Matplotlib or Seaborn

---

## 🏗️ Project Structure

```
nlp-to-code/
├── app.py                # Main Streamlit app
├── .env                  # API keys and secrets (not included in repo)
├── requirements.txt      # Required Python packages
├── utils/
│   ├── sql_generator.py     # Gemini prompt logic for SQL
│   ├── pandas_generator.py  # Gemini prompt logic for Pandas/NumPy
```

---

## ⚙️ Installation

### Step 1: Clone the repo

```bash
git clone https://github.com/your-username/NL2SQL-Generator-with-Gemini
.git
cd NL2SQL-Generator-with-Gemini

```

### Step 2: Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure `.env`

Create a `.env` file with your credentials:

```dotenv
GOOGLE_API_KEY=your_google_gemini_api_key
DB_HOST=your_mysql_host
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_NAME=your_database_name
DB_PORT=3306
```

### Step 5: Run the app

```bash
streamlit run app.py
```

---

## ✨ Usage

1. Choose your task: SQL, Pandas, or NumPy
2. Type an instruction like:
   - “Get total number of students”
   - “Find mean of ‘Price’ column”
   - “Create a 5x5 identity matrix”
3. See the auto-generated code and/or results instantly

---

## 🧠 Sample Prompts

| Instruction                            | Output                               |
|----------------------------------------|---------------------------------------|
| How many rows are in the table?        | `SELECT COUNT(*) FROM STUDENTS;`      |
| Show students in class Data Science    | `SELECT * FROM STUDENTS WHERE CLASS="Data Science";` |
| Get mean of ‘Sales’ column             | `df['Sales'].mean()`                 |
| Create a 3x3 matrix with ones          | `np.ones((3,3))`                     |

---

## ☁️ Deployment

- **Streamlit Cloud** (free hosting for public repos)
- **GCP App Engine / Cloud Run**
- **Docker** + any cloud provider
- (Optional) Snowflake Snowpark for Snowflex integration

---

## 🙋 Contribution

Contributions are welcome!  
Feel free to fork this repo, raise issues, or create pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request

---

## 👤 Author

**Kunal Aher**  
📧 kunalaher0538@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/kunal-aher-506162210/)

---

## 📄 License

MIT License. See `LICENSE` file for details.

