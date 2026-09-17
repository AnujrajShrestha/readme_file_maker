from pathlib import Path


def _extract_content(response):
    """
    Extract text from a LangChain agent response.
    """
    # AIMessage
    if hasattr(response, "content"):
        return response.content

    # New LangGraph agent output
    if isinstance(response, dict):
        if "messages" in response:
            messages = response["messages"]
            if messages:
                last = messages[-1]
                return getattr(last, "content", str(last))

        if "output" in response:
            return response["output"]

    return str(response)


def create_readme(state: dict, repo_url: str):
    """
    Generate README.md in the cloned repository.
    """

    repo_name = repo_url.rstrip("/").split("/")[-1].replace(".git", "")
    repo_path = Path("repositories") / repo_name

    readme_path = repo_path / "README.md"

    groq_output = _extract_content(state["groq_result"])
    mistral_output = _extract_content(state["mistral_result"])

    author = state["author_result"]["author"]
    github = state["author_result"]["github_id_url"]
    note = state["author_result"]["decs"]

    markdown = f"""# {repo_name}

> AI-generated project documentation.

---

## 📖 Overview

This README was automatically generated using an AI-powered GitHub Repository Analyzer.

Repository:

```
{repo_url}
```

---

## 🏗️ Project Architecture

{mistral_output}

---

## ⚙️ Installation

{groq_output}

---

## 👨‍💻 Author

**{author}**

GitHub: {github}

---

## ⭐ Support

{note}

---

*This README was generated automatically using LangChain, RAG, Mistral AI, and Groq.*
"""

    readme_path.write_text(markdown, encoding="utf-8")

    print(f"\n✅ README created successfully!")
    print(readme_path)