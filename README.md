# NOVA Assistant (V1 - Building Block)

NOVA is a lightweight desktop AI assistant built using Python and Tkinter, powered by a local language model through Ollama.

This repository contains Version 1 — the foundational build focused on core functionality, stability, and architecture setup.

---

## 🚀 About The Project

NOVA is designed as a personal desktop assistant that can:

- Execute basic automation commands  
- Open applications and websites  
- Provide AI-generated responses using a local model  
- Run with a global keyboard shortcut  

This version is an early-stage implementation intended as a building block for future improvements.

---

## ✨ Features

- Terminal-style desktop interface  
- Local AI responses via Ollama  
- Global hotkey (Ctrl + Alt + A) to toggle the window  
- Open installed applications (Notepad, Chrome, VS Code, Calculator)  
- Open websites (YouTube, Google, GitHub)  
- Timestamped command responses  

---

## 🛠 Tech Stack

- Python 3.x  
- Tkinter (GUI)  
- Requests  
- Keyboard (Global Hotkeys)  
- Ollama (Local LLM Engine)  

---

## 📂 Project Structure

AI_Assistant/
│
├── assistant.py  
├── requirements.txt  
├── .gitignore  
└── README.md  

Note: A `.env` file is required locally but is not included in this repository for security reasons.

---

## ⚙️ Installation & Setup

### 1. Install Python
Make sure Python 3.10 or higher is installed.

### 2. Install Ollama
Download and install Ollama from:
https://ollama.com

Pull a model (example):
ollama pull phi3

Start Ollama server:
ollama serve

### 3. Install Dependencies

Inside the project folder:
pip install -r requirements.txt

If pip does not work:
python -m pip install -r requirements.txt

### 4. Run the Assistant

python assistant.py

(Optional: Run as Administrator for stable global hotkey behavior.)

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

OPENAI_API_KEY=sk-fake-key  
SERPAPI_KEY=your_key_if_needed  

OpenAI key is not required when using Ollama locally, but the structure is prepared for future API integrations.

The `.env` file is ignored using `.gitignore`.

---

## 📌 Current Status

Version 1 is a functional prototype.

Known limitations:
- Basic command parsing  
- Limited automation scope  
- No system tray integration  
- Minimal error handling  

This version establishes the core structure for future expansion.

---

## 🔮 Planned Improvements (Future Versions)

- Improved natural language command understanding  
- Background system tray integration  
- Voice input support  
- Modular architecture refactor  
- Smarter automation capabilities  

---

## 👨‍💻 Purpose

This project was built as a hands-on exploration of:

- Desktop automation  
- Local LLM integration  
- GUI-based AI tools  
- System-level keyboard event handling  

---

## 📄 License

This project is open-source and intended for learning and experimentation.
