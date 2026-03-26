# Vulgarism Image Analyzer 🔍

A professional desktop application built with Python and MediaPipe for automatic moderation of profile pictures. It detects offensive hand gestures (specifically the middle finger) using a pre-trained Random Forest classifier.

---

## 🚀 Getting Started

Follow these steps to set up and run the application on your local machine.

### 1. Prerequisites
- **Python 3.12** (Mandatory for MediaPipe compatibility)
- **Git**
- **Tkinter Support**:
  - macOS: `brew install python-tk@3.12`
  - Linux/Windows: Usually included with Python installation.

### 2. Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hoch12/Image-Analyzer.git
   cd Image-Analyzer
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### 3. Usage

Run the GUI application directly from the root directory:
```bash
python3 -m src.gui
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
For deeper technical insights, please refer to the following:
- [Development Lifecycle](docs/development.md)
- [Testing Methodology](docs/testing.md)
- [Changelog](changelog.md)

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
