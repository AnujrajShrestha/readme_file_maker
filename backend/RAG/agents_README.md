# csv_file_analyzer

> AI-generated project documentation.

---

## 📖 Overview

This README was automatically generated using an AI-powered GitHub Repository Analyzer.

Repository:

```
https://github.com/AnujrajShrestha/csv_file_analyzer
```

---

## 🏗️ Project Architecture

## **Multi-Agent CSV File Analyzer: Architecture Overview**

### **1. Overview**
The **Multi-Agent CSV File Analyzer** is a **Streamlit-based application** that leverages **multiple AI agents** to perform **Exploratory Data Analysis (EDA), visualization, correlation analysis, and summarization** on uploaded CSV files. The system follows a **modular, agent-based architecture** where each agent specializes in a specific task, and a **pipeline orchestrates** their execution.

---

## **2. High-Level Architecture**
The system consists of the following **major components**:

1. **Frontend (Streamlit UI)**
2. **Agent Pipeline (Orchestrator)**
3. **Specialized Agents**
   - **EDA Agent**
   - **Visualization Agent**
   - **Correlation Agent**
   - **Summary Agent**
4. **State Management**
5. **Report Generation**
6. **File Handling & Storage**

### **Architecture Diagram (Textual Representation)**
```
┌───────────────────────────────────────────────────────────────────────────────┐
│                                                                               │
│                                **User (Browser)**                             │
│                                                                               │
└───────────────────┬───────────────────────────────────────────┬───────────────┘
                    │                                       │
                    ▼                                       ▼
┌─────────────────────────────────┐       ┌─────────────────────────────────┐
│                                 │       │                                 │
│       **Streamlit UI**          │       │       **Command-Line Mode**     │
│                                 │       │                                 │
└───────────────────┬─────────────┘       └───────────────┬─────────────────┘
                    │                                   │
                    ▼                                   ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                                                                           │
│                        **Agent Pipeline (Orchestrator)**                  │
│                                                                           │
└───────────────────┬───────────────────────┬───────────────────────┬───────┘
                    │                       │                       │
                    ▼                       ▼                       ▼
┌───────────────────────┐     ┌───────────────────────┐     ┌───────────────────┐
│                       │     │                       │     │                   │
│     **EDA Agent**     │     │ **Visualization Agent**│     │ **Correlation    │
│                       │     │                       │     │    Agent**        │
└───────────────┬───────┘     └───────────┬───────────┘     └───────┬───────────┘
                │                       │                           │
                ▼                       ▼                           ▼
┌───────────────────────┐     ┌───────────────────────┐     ┌───────────────────┐
│                       │     │                       │     │                   │
│   **Pandas (Data      │     │   **Matplotlib/Seaborn**     │   **Pandas/Seaborn**│
│    Processing)**      │     │   (Plot Generation)    │     │   (Correlation)   │
│                       │     │                       │     │                   │
└───────────────────────┘     └───────────┬───────────┘     └───────┬───────────┘
                                          │                           │
                                          ▼                           ▼
                                ┌───────────────────────┐     ┌───────────────────┐
                                │                       │     │                   │
                                │   **Plots Directory** │     │  **Correlation   │
                                │                       │     │   Output**        │
                                └───────────────────────┘     └───────┬───────────┘
                                                                          │
                                                                          ▼
                                                                ┌───────────────────┐
                                                                │                   │
                                                                │  **Summary Agent**│
                                                                │                   │
                                                                └───────┬───────────┘
                                                                        │
                                                                        ▼
                                                                ┌───────────────────┐
                                                                │                   │
                                                                │  **Report.txt**   │
                                                                │                   │
                                                                └───────────────────┘
```

---

## **3. Component Breakdown & Workflow**

### **3.1. Frontend (Streamlit UI)**
- **Purpose**: Provides a **user-friendly interface** for uploading CSV files and displaying results.
- **Key Features**:
  - File uploader for CSV files.
  - Dataset preview (first 10 rows).
  - Display of generated visualizations (plots).
  - Success/error feedback.
- **Technology**: `Streamlit`, `Pandas` (for data preview).

#### **Workflow**:
1. User uploads a CSV file.
2. The file is saved in the `uploads/` directory.
3. A preview of the dataset is displayed.
4. The **pipeline is triggered** to process the data.
5. Generated plots are displayed in a grid layout.

---

### **3.2. Agent Pipeline (Orchestrator)**
- **Purpose**: **Coordinates** the execution of all agents in a **sequential workflow**.
- **Key Responsibilities**:
  - Invokes each agent in order (EDA → Visualization → Correlation → Summary).
  - Manages the **shared state** (stores results from each agent).
  - Generates a **final report** (`report.txt`).
- **Technology**: Custom Python pipeline (`run_pipeline()`).

#### **Workflow**:
1. **Input**: User query (e.g., `"Perform EDA, Visualization, and correlation process"`).
2. **State Initialization**: A dictionary (`state`) stores results from each agent.
3. **Agent Execution**:
   - **EDA Agent** → **Visualization Agent** → **Correlation Agent** → **Summary Agent**.
4. **Report Generation**: `create_report()` writes results to `report.txt`.
5. **Output**: Returns the final `state` with all results.

---

### **3.3. Specialized Agents**
Each agent is a **LangChain-based tool** that performs a specific task and returns structured output.

| **Agent**            | **Purpose**                                                                 | **Input**               | **Output**                                                                 | **Key Libraries**          |
|----------------------|-----------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------|----------------------------|
| **EDA Agent**        | Performs **Exploratory Data Analysis** (missing values, duplicates, etc.). | CSV file path           | `EDAOutput` (Pydantic model with stats).                                  | `Pandas`, `Pydantic`       |
| **Visualization Agent** | Generates **plots** (histograms, box plots, etc.).                        | CSV file path           | `VisualizationOutput` (plot file paths).                                  | `Matplotlib`, `Seaborn`    |
| **Correlation Agent** | Computes **correlation matrices** and heatmaps.                            | CSV file path           | `CorrelationOutput` (correlation plot path).                              | `Pandas`, `Seaborn`        |
| **Summary Agent**    | Generates a **concise summary** of the dataset.                            | User query + CSV data   | `SummaryOutput` (structured summary).                                     | `LangChain`, `Pydantic`    |

#### **Agent Workflow**:
1. **EDA Agent**:
   - Reads the CSV file.
   - Computes statistics (rows, columns, missing values, etc.).
   - Returns structured output (`EDAOutput`).

2. **Visualization Agent**:
   - Generates plots (histograms, box plots, etc.).
   - Saves plots in `plots/` directory.
   - Returns plot file paths (`VisualizationOutput`).

3. **Correlation Agent**:
   - Computes correlation matrices.
   - Generates a heatmap and saves it as `correlation.png`.
   - Returns correlation details (`CorrelationOutput`).

4. **Summary Agent**:
   - Uses **LangChain** to generate a **natural language summary**.
   - Returns structured summary (`SummaryOutput`).

---

### **3.4. State Management**
- **Purpose**: Maintains **intermediate results** across agents.
- **Implementation**:
  - A **dictionary (`state`)** stores outputs from each agent.
  - Keys: `eda_result`, `visual_result`, `corr_result`, `summary_result`.
- **Workflow**:
  - Each agent updates the `state` with its results.
  - The pipeline passes the `state` between agents.

---

### **3.5. Report Generation**
- **Purpose**: Compiles all agent results into a **human-readable report**.
- **Implementation**:
  - `create_report()` writes results to `report.txt`.
  - Uses a **structured format** with separators for each agent’s output.
- **Output Example**:
  ```
  ------------------------------------------------------------
  Step 1 - EDA Agent
  ------------------------------------------------------------
  total_rows: 1000
  total_columns: 5
  numerical_columns: ['age', 'income']
  ...
  ------------------------------------------------------------
  Step 2 - Visualization Agent
  ------------------------------------------------------------
  status: Success
  output_files: ['plots/histogram_age.png', ...]
  ...
  ```

---

### **3.6. File Handling & Storage**
| **Directory/File** | **Purpose**                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `uploads/`         | Stores uploaded CSV files.                                                 |
| `plots/`           | Stores generated plots (histograms, heatmaps, etc.).                       |
| `report.txt`       | Final report containing all agent outputs.                                 |

---

## **4. Data Flow**
1. **User uploads CSV** → Saved in `uploads/`.
2. **Pipeline starts** → Passes CSV to **EDA Agent**.
3. **EDA Agent** processes data → Updates `state`.
4. **Visualization Agent** generates plots → Saves in `plots/` → Updates `state`.
5. **Correlation Agent** computes correlations → Saves heatmap → Updates `state`.
6. **Summary Agent** generates summary → Updates `state`.
7. **Report Generator** writes `report.txt`.
8. **Streamlit UI** displays plots and success message.

---

## **5. Key Technologies**
| **Category**       | **Technologies**                                                                 |
|--------------------|---------------------------------------------------------------------------------|
| **Frontend**       | Streamlit                                                                       |
| **Data Processing**| Pandas, NumPy                                                                    |
| **Visualization**  | Matplotlib, Seaborn                                                              |
| **AI Agents**      | LangChain, LangChain-Groq, LangChain-MistralAI                                  |
| **State Management** | Python dictionaries, Pydantic (for structured outputs)                        |
| **File Storage**   | Local filesystem (`uploads/`, `plots/`)                                         |
| **Environment**    | Python-dotenv (for environment variables)                                       |

---

## **6. Execution Modes**
1. **Streamlit Mode** (Primary):
   - User interacts via a **web UI**.
   - Plots are displayed in the browser.
2. **Command-Line Mode** (Secondary):
   - User runs the script manually.
   - Can **delete generated plots** (`0` input).
   - Exits on `exit` command.

---

## **7. Summary of Workflow**
1. **User Interaction** → Upload CSV via Streamlit or CLI.
2. **Data Ingestion** → CSV saved in `uploads/`.
3. **Agent Execution** → EDA → Visualization → Correlation → Summary.
4. **State Management** → Results stored in `state` dictionary.
5. **Report Generation** → `report.txt` created.
6. **Output Display** → Plots shown in Streamlit or saved in `plots/`.

This architecture ensures **modularity, scalability, and maintainability**, allowing each agent to be **independently updated** without affecting the overall system.

---

## ⚙️ Installation

To install the required libraries and tools for the CSV File Analyzer, you can use pip, the Python package manager. The required libraries include streamlit, pandas, numpy, matplotlib, seaborn, and sentence-transformers. You can install them using the following command:
```
pip install streamlit pandas numpy matplotlib seaborn sentence-transformers
```
Additionally, you may need to install other libraries such as langchain, chromadb, and tiktoken, depending on the specific requirements of your project. You can install them using the following commands:
```
pip install langchain chromadb tiktoken
```
Make sure to install the libraries in the correct order and with the correct versions to avoid any compatibility issues. Also, ensure that you have the necessary dependencies installed, such as Python and pip, before installing the libraries.

---

## 👨‍💻 Author

**Anuj shrestha**

GitHub: https://github.com/AnujrajShrestha

---

## ⭐ Support

⭐ If you found this project useful, consider giving it a star on GitHub!

---

*This README was generated automatically using LangChain, RAG, Mistral AI, and Groq.*
