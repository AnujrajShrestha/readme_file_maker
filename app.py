import streamlit as st
from pathlib import Path
from rag_engine import run_pipeline

st.set_page_config(
    page_title="AI GitHub README Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI GitHub README Generator")
st.caption("Generate professional README files using RAG + LangChain Agents")

repo_url = st.text_input("GitHub Repository URL")
project_name = st.text_input("Project Name")
author = st.text_input("Author Name")
github = st.text_input("GitHub Profile URL")

if st.button("🚀 Generate README", use_container_width=True):

    progress = st.progress(0)
    status = st.empty()

    status.write("📥 Cloning repository...")
    progress.progress(10)

    state = run_pipeline({
        "url": repo_url,
        "project_name": project_name,
        "author_name": author,
        "github_id_url": github
    })

    progress.progress(100)
    status.success("README generated successfully!")

    repo = repo_url.rstrip("/").split("/")[-1].replace(".git", "")
    readme_path = Path("repositories") / repo / "README.md"

    if readme_path.exists():
        markdown = readme_path.read_text(encoding="utf-8")

        preview_tab, markdown_tab = st.tabs(["📖 Preview", "📝 Markdown"])

        with preview_tab:
            st.markdown(markdown)

        with markdown_tab:
            st.code(markdown, language="markdown")

        st.download_button(
            "⬇ Download README",
            data=markdown,
            file_name="README.md",
            mime="text/markdown",
            use_container_width=True
        )