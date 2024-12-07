# Set Up a Virtual Environment

A virtual environment is an isolated Python workspace where you can install specific dependencies for a project without affecting other projects or the system's global Python installation. Using virtual environments is considered a best practice for Python development, especially for automation testing projects.

---

#### Why Use a Virtual Environment?
- **Isolation**: Avoid conflicts between different project dependencies.
- **Version Control**: Test your automation scripts with specific library versions.
- **Clean Setup**: Keep your global Python environment uncluttered.

---

#### Creating and Activating a Virtual Environment

##### 1. **Create a Virtual Environment**
To create a virtual environment, run the following command in your project directory:
```bash
python -m venv venv
```