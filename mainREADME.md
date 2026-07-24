# 📘 AI GitHub Repository README Generator

> An AI-powered GitHub Repository README Generator that automatically analyzes any public GitHub repository using **RAG (Retrieval-Augmented Generation)**, **LangChain Agents**, **Mistral AI**, **Groq**, and **ChromaDB**, then generates a professional `README.md` file.

---

# 🚀 Overview

Writing a good README is time-consuming and often neglected. This project automates the entire documentation process.

The application clones a GitHub repository, indexes its source code into a vector database, retrieves relevant repository context using RAG, and uses **multiple AI agents** to generate different sections of a professional README file.

The generated README includes:

* Project Overview
* Technology Stack
* Architecture
* Folder Structure
* Installation Guide
* Environment Variables
* Usage
* Features
* Future Improvements
* Author Information

The system combines the strengths of **Groq (Llama 3.3)** for fast documentation generation and **Mistral Large** for deeper repository analysis.

---

# ✨ Features

* 🔍 Analyze any public GitHub repository
* 📂 Clone repositories automatically
* 📑 Load source code and documentation
* 🧩 RAG-based repository understanding
* 🤖 Multi-Agent architecture
* ⚡ Fast README generation
* 🧠 Automatic architecture explanation
* 📦 Detect technology stack
* 🏗️ Generate installation instructions
* 🔐 Detect environment variables
* 📁 Explain repository structure
* 💡 Suggest future improvements
* 📝 Produce a complete professional README.md

---

# 🏗️ System Architecture

```
                    User
                      │
                      ▼
           Enter GitHub Repository URL
                      │
                      ▼
               git_clone.py
                      │
          Clone Repository Locally
                      │
                      ▼
                  db.py
                      │
      Load Repository Source Files
                      │
                      ▼
     RecursiveCharacterTextSplitter
                      │
                      ▼
          Mistral Embeddings
                      │
                      ▼
             Chroma Vector DB
                      │
                      ▼
            RAG Retriever (MMR)
                      │
         Repository Context Retrieved
                      │
          ┌───────────┴────────────┐
          ▼                        ▼
     Groq Agent              Mistral Agent
 (Project Documentation) (Architecture Analysis)
          │                        │
          └───────────┬────────────┘
                      ▼
              README Generator
          (readme_maker.py)
                      │
                      ▼
          Professional README.md
```

---

# ⚙️ Workflow

## Step 1 — Clone Repository

The repository URL is provided by the user.

`git_clone.py`

* Extracts repository name
* Clones the repository
* Stores it inside

```
repositories/
```

---

## Step 2 — Load Source Code

`db.py`

Loads important project files including

* Python
* JavaScript
* TypeScript
* React
* HTML
* CSS
* JSON
* YAML
* SQL
* PHP
* C/C++
* Docker
* Git files
* Text files

---

## Step 3 — Create Chunks

Large files are split using

```
RecursiveCharacterTextSplitter
```

```
Chunk Size : 800

Chunk Overlap : 80
```

---

## Step 4 — Create Vector Database

Each chunk is converted into embeddings using

```
Mistral Embeddings
```

and stored inside

```
ChromaDB
```

---

## Step 5 — Retrieve Context

When generating documentation,

MMR Retrieval is used

```
k = 8

fetch_k = 12

lambda = 0.5
```

to retrieve only the most relevant repository context.

---

## Step 6 — Multi-Agent Processing

### 🚀 Groq Agent

Uses

```
Llama-3.3-70B-Versatile
```

Responsible for:

* Project Overview
* Installation Guide
* Features
* Future Improvements

---

### 🧠 Mistral Agent

Uses

```
Mistral Large Latest
```

Responsible for:

* Architecture
* Technology Stack
* Folder Structure
* Environment Variables
* Usage Instructions

---

## Step 7 — README Generation

Both agent outputs are merged into a professional

```
README.md
```

inside the cloned repository.

---

# 📂 Project Structure

```
AI-GitHub-README-Generator
│
├── repositories/
│
├── git_clone.py
├── db.py
├── tools.py
├── agents.py
├── rag_engine.py
├── readme_maker.py
├── config.py
├── requirements.txt
├── .env
└── README.md
```

---

# 🛠️ Technology Stack

## AI & LLM

* LangChain
* LangGraph Agent API
* Mistral AI
* Groq
* Llama 3.3 70B
* Mistral Large Latest

---

## Vector Database

* ChromaDB

---

## Embeddings

* Mistral Embeddings

---

## Retrieval

* Retrieval-Augmented Generation (RAG)
* Maximum Marginal Relevance (MMR)

---

## Programming Language

* Python

---

## Supporting Libraries

* LangChain Community
* LangChain Chroma
* LangChain MistralAI
* LangChain Groq
* Pydantic
* python-dotenv

---

# 📥 Installation

## Clone the Repository

```bash
git clone <repository-url>

cd AI-GitHub-README-Generator
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file.

```env
MISTRAL_API_KEY=your_mistral_api_key

GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Usage

Run

```bash
python rag_engine.py
```

Provide

```
Repository URL

Project Name

Author Name

GitHub Profile URL
```

Example

```
Enter repository url:
https://github.com/user/project

Enter project name:
My Project

Enter author name:
John Doe

Enter github ID url:
https://github.com/johndoe
```

The application will automatically

1. Clone the repository
2. Build the vector database
3. Analyze repository code
4. Invoke AI agents
5. Generate a professional README.md

---

# 🧠 AI Agents

| Agent         | Responsibility                                    |
| ------------- | ------------------------------------------------- |
| Groq Agent    | Installation, Features, Improvements              |
| Mistral Agent | Architecture, Tech Stack, Usage, Folder Structure |

---

# 📊 RAG Pipeline

```
Repository

      │

      ▼

Document Loader

      │

      ▼

Text Splitter

      │

      ▼

Mistral Embeddings

      │

      ▼

Chroma Vector DB

      │

      ▼

Retriever (MMR)

      │

      ▼

Repository Context

      │

      ▼

AI Agents

      │

      ▼

README Generator
```

---

# 🔮 Future Improvements

* 🌐 Streamlit or React web interface
* 📊 Generate Mermaid architecture diagrams
* 📄 Export documentation as PDF
* 🔍 Automatic dependency analysis
* 🧪 Generate API documentation
* 📝 Create CONTRIBUTING.md automatically
* 📜 Generate LICENSE recommendations
* 🧩 Multi-LLM support (OpenAI, Gemini, Claude)
* ☁️ Deploy as a cloud-based SaaS application

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 👨‍💻 Author

**Anuj Shrestha**

GitHub: https://github.com/AnujrajShrestha

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.
