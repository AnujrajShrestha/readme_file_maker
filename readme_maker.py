from pathlib import Path

def repo_path(url: str) -> dict:
    repo_name = url.rstrip("/").split("/")[-1]
    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]

    return {
        "name": repo_name,
        "path": Path("repositories") / repo_name
    }

def format_list(items) -> str:
    """Helper to convert lists or strings into clean markdown bullet points."""
    if not items:
        return "* None specified\n"
    if isinstance(items, str):
        return f"- {items}\n"
    return "\n".join(f"- {item}" for item in items) + "\n"

def create_readme(state: dict, url: str) -> Path:
    repo_info = repo_path(url)
    save_dir = repo_info["path"]
    save_dir.mkdir(parents=True, exist_ok=True)
    
    readme_path = save_dir / "README.md"

    # Safely extract objects from state
    analysis = state.get("analysis_result")
    features = state.get("features_result")
    arch = state.get("architecture_result")
    struct = state.get("structure_result")
    tech = state.get("techstack_result")
    install = state.get("installation_result")
    env_vars = state.get("env_result")
    usage = state.get("usage_result")
    improvements = state.get("improvements_result")
    author = state.get("author_result")

    with open(readme_path, "w", encoding="utf-8") as fs:
        # Title & Header
        proj_name = getattr(analysis, "project_name", repo_info["name"])
        description = getattr(analysis, "description", "")
        fs.write(f"# {proj_name}\n\n")
        if description:
            fs.write(f"> {description}\n\n")

        # Overview Table
        if analysis:
            category = getattr(analysis, "category", "N/A")
            purpose = getattr(analysis, "purpose", "N/A")
            fs.write("## 📌 Project Overview\n\n")
            fs.write("| Property | Details |\n")
            fs.write("| :--- | :--- |\n")
            fs.write(f"| **Category** | {category} |\n")
            fs.write(f"| **Purpose** | {purpose} |\n\n")

        # Features
        if features and hasattr(features, "features"):
            fs.write("## 🚀 Features\n\n")
            fs.write(format_list(features.features))
            fs.write("\n")

        # Tech Stack
        if tech:
            fs.write("## ⚙️ Tech Stack\n\n")
            if hasattr(tech, "languages") and tech.languages:
                fs.write(f"**Languages:** {', '.join(tech.languages)}\n\n")
            if hasattr(tech, "frameworks") and tech.frameworks:
                fs.write(f"**Frameworks:** {', '.join(tech.frameworks)}\n\n")
            if hasattr(tech, "llms") and tech.llms:
                fs.write(f"**LLMs & Frameworks:** {', '.join(tech.llms)}\n\n")
            if hasattr(tech, "libraries") and tech.libraries:
                fs.write(f"**Libraries:** {', '.join(tech.libraries)}\n\n")
            if hasattr(tech, "databases") and tech.databases:
                fs.write(f"**Databases:** {', '.join(tech.databases)}\n\n")

        # Architecture
        if arch:
            fs.write("## 🏗️ Architecture\n\n")
            if hasattr(arch, "title"):
                fs.write(f"### {arch.title}\n")
            if hasattr(arch, "architecture_type"):
                fs.write(f"**Type:** `{arch.architecture_type}`  \n")
            if hasattr(arch, "entry_point"):
                fs.write(f"**Entry Point:** `{arch.entry_point}`\n\n")

            if hasattr(arch, "workflow") and arch.workflow:
                fs.write("### Execution Workflow\n\n")
                for step_item in arch.workflow:
                    if isinstance(step_item, dict):
                        s_num = step_item.get("step", "")
                        comp = step_item.get("component", "")
                        desc = step_item.get("description", "")
                    else:
                        s_num = getattr(step_item, "step", "")
                        comp = getattr(step_item, "component", "")
                        desc = getattr(step_item, "description", "")
                    fs.write(f"{s_num}. **{comp}**: {desc}\n")
                fs.write("\n")

        # Project Structure
        if struct:
            fs.write("## 📁 Project Structure\n\n")
            if hasattr(struct, "important_files") and struct.important_files:
                fs.write("**Key Files:**\n")
                fs.write(format_list(struct.important_files))
            if hasattr(struct, "folders") and struct.folders:
                fs.write("\n**Directories:**\n")
                fs.write(format_list(struct.folders))
            fs.write("\n")

        # Installation
        if install:
            fs.write("## 📦 Installation\n\n")
            if hasattr(install, "requirements") and install.requirements:
                fs.write("### Prerequisites\n")
                fs.write(format_list(install.requirements))
                fs.write("\n")
            if hasattr(install, "install_steps") and install.install_steps:
                fs.write("### Setup Steps\n\n")
                for step in install.install_steps:
                    fs.write(f"{step}\n\n")

        # Environment Variables
        if env_vars and hasattr(env_vars, "variables") and env_vars.variables:
            fs.write("## 🔑 Environment Variables\n\n")
            fs.write("Make sure to configure the following environment variables:\n\n")
            for var in env_vars.variables:
                fs.write(f"- `{var}`\n")
            fs.write("\n")

        # Workflow / Usage
        if usage:
            fs.write("## 📸 Usage & Workflow\n\n")
            if hasattr(usage, "commands") and usage.commands:
                fs.write("### Commands\n")
                fs.write(format_list(usage.commands))
            if hasattr(usage, "workflow") and usage.workflow:
                fs.write("\n### Workflow Steps\n")
                fs.write(format_list(usage.workflow))
            fs.write("\n")

        # Future Improvements
        if improvements and hasattr(improvements, "improvements"):
            fs.write("## 🎯 Future Improvements\n\n")
            fs.write(format_list(improvements.improvements))
            fs.write("\n")

        # Author Info
        if author:
            fs.write("## 👨‍💻 Author Information\n\n")
            name = getattr(author, "author", "Contributor")
            github_url = getattr(author, "github_id_url", "")
            desc = getattr(author, "decs", "")

            if github_url:
                fs.write(f"Created by [{name}]({github_url})\n\n")
            else:
                fs.write(f"Created by **{name}**\n\n")
            
            if desc:
                fs.write(f"{desc}\n")

    print(f"✅ README successfully written to: {readme_path}")
    return save_dir