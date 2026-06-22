# FastAPI LLM API 🚀

A FastAPI-based REST API that integrates Large Language Models (LLMs) to generate AI-powered content such as summaries, interview questions, ATS scores, LinkedIn headlines, and elevator pitches.

## 📌 Features

* ✅ ATS Resume Score Analysis
* ✅ AI-generated Interview Questions
* ✅ LinkedIn Headline Generator
* ✅ Elevator Pitch Generator
* ✅ RESTful API built with FastAPI
* ✅ Structured Request and Response Models using Pydantic
* ✅ Environment Variable Management using `.env`
* ✅ Interactive API Documentation with Swagger UI

---

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **Pydantic**
* **Groq API**
* **Uvicorn**
* **python-dotenv**

---

## 📂 Project Structure

```bash
FastApi_llm/
│
├── main.py                 # FastAPI application
├── llm_client.py           # Groq LLM integration
├── prompts.py              # Prompt templates
├── schemas.py              # Pydantic request/response models
├── .env                    # Environment variables (not pushed to GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Gehna-01/FastApi_llm.git
cd FastApi_llm
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server will run at:

```bash
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically generates interactive documentation.

### Swagger UI

```bash
http://127.0.0.1:8000/docs
```

### ReDoc

```bash
http://127.0.0.1:8000/redoc
```

---

## 📡 Available Endpoints

### POST `/ats-score`

Analyzes a resume and returns an ATS score.

### POST `/interview-questions`

Generates interview questions based on skills and experience.

### POST `/linkedin-headline`

Generates professional LinkedIn headlines.

### POST `/elevator-pitch`

Creates a concise and impactful elevator pitch.

---

## Example Request

```json
{
  "name": "John Doe",
  "skills": ["Python", "FastAPI", "Machine Learning"],
  "experience": 3,
  "job_role": "AI Engineer"
}
```

---

## Future Enhancements

* Multi-LLM Support
* Authentication & Rate Limiting
* Docker Deployment

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository and submit pull requests.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by **Gehna**
