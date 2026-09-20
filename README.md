# MCQ-GENERATOR
# 📝  MCQ Generator

An AI-powered **Multiple Choice Question (MCQ) Generator** built using **Python, Streamlit, and Hugging Face**. The application allows users to enter a topic, select the number of questions and difficulty level, and automatically generate multiple-choice questions using a Large Language Model (LLM).

---

## 📌 Project Overview

Creating MCQs manually can take considerable time, especially when preparing quizzes, assignments, and practice tests.

This project uses **Generative AI** to automatically create MCQs from a given topic.

The user provides:

* 📚 Topic
* 🔢 Number of questions
* 🎯 Difficulty level

The application sends these requirements to a **Hugging Face-hosted language model**, which generates questions containing four options and the correct answer.

The generated questions are then displayed directly in the Streamlit application.

---

## 🎯 Objectives

The main objectives of this project are:

1. To generate MCQs automatically using AI.
2. To understand how Large Language Models can be integrated into applications.
3. To use the Hugging Face Inference API for text generation.
4. To build a simple interactive application using Streamlit.
5. To reduce the time required to manually create quiz questions.
6. To provide customizable questions based on topic and difficulty.

---

## ✨ Features

* 🤖 AI-powered MCQ generation
* 📚 Custom topic input
* 🔢 Select number of questions
* 🎯 Choose difficulty level
* 🔤 Four options for every question
* ✅ Automatically generated correct answers
* ⚡ Fast question generation
* 🌐 Simple Streamlit web application
* 🔐 Secure Hugging Face API token using Streamlit secrets

---

## 🛠️ Technologies Used

| Technology                   | Purpose                                  |
| ---------------------------- | ---------------------------------------- |
| Python                       | Application development                  |
| Streamlit                    | Web application interface                |
| Hugging Face                 | AI/LLM inference                         |
| Hugging Face InferenceClient | Connects Python application to the model |
| TOML                         | Secure API key configuration             |
| Large Language Model         | Generates MCQs                           |

---

## 🏗️ System Architecture

```text
              ┌─────────────────────┐
              │       User          │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │     Streamlit       │
              │   Web Application   │
              └──────────┬──────────┘
                         │
              Topic + Number + Level
                         │
                         ▼
              ┌─────────────────────┐
              │  Prompt Generation  │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Hugging Face LLM    │
              │      Inference      │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Generated MCQs    │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Display Results    │
              │    in Streamlit     │
              └─────────────────────┘
```

---

## 🔄 How the Application Works

### Step 1: User enters a topic

The user enters a subject such as:

```text
Python Programming
```

or:

```text
Artificial Intelligence
```

### Step 2: User selects quiz settings

The user chooses:

* Number of questions
* Difficulty level

For example:

```text
Topic: Python Programming
Questions: 5
Difficulty: Medium
```

### Step 3: Prompt is created

The application creates a prompt containing the user's requirements.

Example:

```text
Generate 5 multiple choice questions about Python Programming.

Difficulty: Medium

Each question should contain:
A, B, C, D options
and the correct answer.
```

### Step 4: Hugging Face generates the questions

The prompt is sent to a language model through the Hugging Face `InferenceClient`.

### Step 5: Results are displayed

The generated questions are returned to the Streamlit application and displayed to the user.

---

## 📂 Project Structure

```text
MCQ_Generator/
│
├── app.py
│
├── .streamlit/
│   └── secrets.toml
│
└── README.md
```

### `app.py`

Contains the main Python application, including:

* Streamlit components
* User input
* Prompt creation
* Hugging Face API connection
* MCQ generation
* Result display

### `secrets.toml`

Stores the Hugging Face access token securely.

```toml
Access_Token = "hf_your_token_here"
```

**Never upload your actual token to GitHub.**

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project

```bash
cd MCQ_Generator
```

### 3. Install required libraries

```bash
pip install streamlit huggingface_hub
```

---

## 🔑 Hugging Face API Configuration

Create the following folder:

```text
.streamlit
```

Inside it, create:

```text
secrets.toml
```

Add your Hugging Face access token:

```toml
Access_Token = "hf_your_actual_token"
```

The application accesses it using:

```python
st.secrets["Access_Token"]
```

### ⚠️ Security

Do not upload `secrets.toml` containing your real token to GitHub.

Add it to `.gitignore`:

```text
.streamlit/secrets.toml
```

---

## ▶️ Running the Application

Run the following command in the terminal:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually it will be available at:

```text
http://localhost:8501
```

---

## 🧪 Example

### Input

```text
Topic: Database Management System
Number of Questions: 5
Difficulty: Medium
```

### Output

```text
Question 1:
Which of the following is used to uniquely identify a record?

A. Foreign Key
B. Primary Key
C. Candidate Table
D. View

Answer: B
```

The application generates the requested number of questions in a similar format.

---

## 📊 Input and Output

### Input

| Input               | Description                                |
| ------------------- | ------------------------------------------ |
| Topic               | Subject for which MCQs should be generated |
| Number of Questions | Number of questions required               |
| Difficulty          | Easy, Medium, or Hard                      |

### Output

The application generates:

* Question
* Option A
* Option B
* Option C
* Option D
* Correct Answer

---

## 💡 Example Topics

The application can be used for different subjects, including:

* Python
* Java
* C Programming
* Artificial Intelligence
* Machine Learning
* DBMS
* Data Structures
* Operating Systems
* Computer Networks
* Cloud Computing
* Prompt Engineering
* General Knowledge

---

## 🚀 Future Enhancements

The project can be extended with additional features:

* 📊 Quiz score calculation
* 📝 Interactive quiz mode
* ⏱️ Timer for each quiz
* 📥 Download questions as PDF
* 📄 Upload study material and generate MCQs
* 🧠 Different question types
* 📈 Performance analysis
* 💾 Save generated quizzes
* 👤 User login system
* 🗄️ Database integration
* 🔊 Text-to-speech support

---

## 🎓 Learning Outcomes

Through this project, the following concepts can be learned:

### 1. Streamlit

Understanding how Python applications can be converted into interactive web applications.

### 2. Hugging Face

Learning how to use pretrained and hosted AI models through an inference API.

### 3. Prompt Engineering

Learning how to create structured prompts to obtain a desired output from an LLM.

### 4. API Integration

Understanding how an external AI service can be connected to a Python application.

### 5. Generative AI

Understanding how Large Language Models can generate educational content.

### 6. Secure API Key Management

Learning how API credentials can be stored using Streamlit secrets instead of directly placing them in source code.

---

## ⚠️ Limitations

Although the application uses an AI model, generated questions may occasionally contain:

* Incorrect information
* Ambiguous options
* Repeated concepts
* Incorrect answers

Therefore, generated questions should be reviewed before being used for formal examinations or educational assessment.

---

## 🔮 Future Scope

The MCQ Generator can be developed into a complete AI-based educational platform.

Future versions could allow students or teachers to upload **PDFs, notes, or study materials**, automatically extract the content, generate questions, conduct interactive quizzes, calculate scores, and provide personalized performance analysis.

---

## 👩‍💻 Author

**D. Hasini**

B.Sc. Computer Science with AI

---

## 📜 License

This project is created for **educational and academic purposes**.
