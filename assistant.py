import subprocess
import webbrowser
import requests
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
import threading
import keyboard
from dotenv import load_dotenv
import os

# ================= LOAD ENV =================
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")   # fake allowed
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

ASSISTANT_NAME = "NOVA"

PROGRAMS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad",
    "vscode": "code",
    "calculator": "calc",
}

WEBSITES = {
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "github": "https://github.com",
}

OLLAMA_URL = "http://localhost:11434"
OLLAMA_MODEL = "phi3"

# ================= AI =================
def ask_ai(command):
    try:
        r = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": command,
                "stream": False
            },
            timeout=60
        )
        return r.json().get("response", "No response")
    except Exception as e:
        return f"Ollama Error: {e}"

# ================= COMMAND =================
def execute(command):
    cmd = command.lower().strip()

    if cmd.startswith("open "):
        target = cmd.replace("open ", "").strip()

        if target in WEBSITES:
            webbrowser.open(WEBSITES[target])
            return f"Opening {target}"

        if target in PROGRAMS:
            subprocess.Popen(PROGRAMS[target])
            return f"Opening {target}"

        return "App or website not found"

    return ask_ai(command)

# ================= GUI =================
class Assistant:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NOVA Assistant")
        self.root.geometry("800x500")

        self.text = ScrolledText(
            self.root,
            wrap="word",
            bg="#111827",
            fg="#e5e7eb",
            font=("Consolas", 12)
        )
        self.text.pack(fill="both", expand=True)

        self.text.insert("end", "NOVA Ready\n> ")
        self.text.mark_set("input_start", "end-1c")
        self.text.bind("<Return>", self.on_enter)

        # Global Hotkey
        keyboard.add_hotkey("ctrl+alt+a", self.safe_toggle)

    def safe_toggle(self):
        self.root.after(0, self.toggle_window)

    def toggle_window(self):
        if self.root.state() == "normal":
            self.root.withdraw()
        else:
            self.root.deiconify()

    def on_enter(self, event):
        user_input = self.text.get("input_start", "end-1c").strip()
        if not user_input:
            return "break"

        timestamp = datetime.now().strftime("%H:%M:%S")
        self.text.insert("end", f"\n[{timestamp}] You: {user_input}\n")
        self.text.insert("end", f"[{timestamp}] NOVA: Processing...\n")
        self.text.see("end")

        threading.Thread(
            target=self.process_command,
            args=(user_input,),
            daemon=True
        ).start()

        return "break"

    def process_command(self, cmd):
        result = execute(cmd)
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.root.after(0, lambda: self.display_result(timestamp, result))

    def display_result(self, timestamp, result):
        self.text.insert("end", f"[{timestamp}] NOVA: {result}\n> ")
        self.text.mark_set("input_start", "end-1c")
        self.text.see("end")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Assistant()
    app.run()