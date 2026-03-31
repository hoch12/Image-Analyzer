# Vulgarism Image Analyzer 🔍

A professional desktop application built with Python and MediaPipe for automatic moderation of profile pictures. It detects offensive hand gestures (specifically the middle finger) using a pre-trained Random Forest classifier.

---

## 🚀 Getting Started

Follow these steps to set up and run the application on your local machine.

### 1. Prerequisites
- **Python 3.12** (Mandatory for MediaPipe compatibility)
  - **Windows Note:** If you don't have Python 3.12 installed and the commands below fail, you can quickly install it via terminal using `winget`:
    ```bash
    winget install -e --id Python.Python.3.12
    ```
    *(Important: Restart your terminal after installation! Alternatively, download the installer from [python.org](https://www.python.org/downloads/windows/) and ensure "Add python.exe to PATH" is checked).*
- **Git**
- **Tkinter Support**:
  - macOS: `brew install python-tk@3.12`
  - Linux/Windows: Usually included with Python installation.

### 2. Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/hoch12/Image-Analyzer.git](https://github.com/hoch12/Image-Analyzer.git)
   cd Image-Analyzer
   ```

2. **Create a virtual environment:**
   ```bash
   # macOS / Linux:
   python3.12 -m venv .venv

   # Windows (via Python Launcher):
   py -3.12 -m venv .venv
   ```

3. **Activate the virtual environment:**
   ```bash
   # macOS / Linux:
   source .venv/bin/activate

   # Windows (Git Bash):
   source .venv/Scripts/activate

   # Windows (Command Prompt / CMD):
   .venv\Scripts\activate
   ```

4. **Install dependencies:**
   *(Make sure your environment is activated from the previous step)*
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## 💻 Usage

1.  **Activating the virtual environment:**
    Always activate the environment before running the project (see step 2.3). You will know it's activated when you see the `(.venv)` prefix in your terminal.

2.  **Running the GUI:**
    If your virtual environment is activated, the command is the same for all systems:
    ```bash
    python -m src.gui
    ```

    *Or run directly without activation (using absolute paths):*
    ```bash
    # macOS / Linux:
    ./.venv/bin/python -m src.gui

    # Windows (Git Bash):
    ./.venv/Scripts/python -m src.gui
    ```

3.  **Running tests:**
    With activated virtual environment:
    ```bash
    python -m unittest discover tests
    ```

    *Without activating the environment:*
    ```bash
    # macOS / Linux:
    ./.venv/bin/python -m unittest discover tests

    # Windows (Git Bash):
    ./.venv/Scripts/python -m unittest discover tests
    ```

---

## 🏗️ Project Architecture

- `src/`: Core source code.
  - `gui.py`: CustomTkinter desktop interface.
  - `engine.py`: Inference logic and model loading.
  - `features.py`: MediaPipe landmark extraction.
  - `config.py`: Centralized configuration and paths.
- `models/`: Pre-trained Scikit-Learn model (`.pkl`).
- `data_collection/`: Scripts used for harvesting the 1500+ image dataset.
- `docs/`: Detailed development and testing documentation.
- `tests/`: Automated unit tests.

---

## 🧪 Documentation
For deeper technical insights and customization, please refer to the following:
- [Configuration Guide](docs/configuration.md) — How to customize AI sensitivity and UI.
- [Development Lifecycle](docs/development.md)
- [Testing Methodology](docs/testing.md)
- [Changelog](changelog.md)

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
