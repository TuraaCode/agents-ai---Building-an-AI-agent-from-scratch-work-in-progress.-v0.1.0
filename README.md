# agents-ai---Building-an-AI-agent-from-scratch-work-in-progress.-v0.1.0
Simple open source AI agent with real-time web search, built with Python, LangChain, LangGraph, DuckDuckGo Search  and Ollama (Mistral) running fully local and free.

# Agents AI 🐯
> Building an AI agent from scratch, work in progress.

Simple open source AI agent with real-time web search, built with Python, LangChain, LangGraph, DuckDuckGo Search and Ollama (Mistral) running fully local and free.

---

## ✨ Features
- Real-time web search (DuckDuckGo, no API key needed)
- Multilingual — responds in the user's language automatically
- Runs 100% locally — no cloud, no cost, no limits
- Conversation history within session
- Current date and time awareness

---

## 🖥️ Requirements
- Windows 10/11
- Python 3.11+
- Node.js v22 LTS
- Ollama
- 8GB RAM minimum (16GB+ recommended)
- NVIDIA GPU recommended

---

## 🚀 Installation

### 1. Install Python
Download Python 3.11+ from:
👉 https://python.org/downloads
> ⚠️ Check "Add Python to PATH" during installation

### 2. Install Ollama
Download from:
👉 https://ollama.com
> After installing, Ollama runs in the background automatically.

### 3. Download Mistral model
Open terminal (CMD) and run:
```bash
ollama pull mistral
```

### 4. Clone this repository
```bash
git clone https://github.com/TuraaCode/agents-ai.git
cd agents-ai
```

### 5. Install dependencies
```bash
pip install langchain langchain-community langchain-core langchain-ollama langgraph ddgs
```

---

## ▶️ Usage

### Option 1 — Double click
Run `START.bat` — opens everything automatically.

### Option 2 — Terminal
```bash
python agents.py
```

Then just type your question and press Enter.
Type `exit` or `sair` to quit.

---

## 📁 Project Structure

agents-ai/
├── START.bat       ← double click to run
├── agents.py       ← main chatbot
├── config.py       ← settings (model, name, version)
└── tools.py        ← web search and utilities

---

## ⚙️ Configuration
Edit `config.py` to customize:
```python
MODEL = "mistral"    # change AI model here
NAME = "Agents AI"   # change assistant name here
VERSION = "0.1.0"    # version
```

---

## 🗺️ Roadmap
- [x] Real-time web search
- [x] Multilingual support
- [x] Conversation history
- [ ] Persistent memory
- [ ] Multi-agent support
- [ ] Web interface
- [ ] Emotion system

---

## 🛠️ Built With
- [Python](https://python.org)
- [LangChain](https://langchain.com)
- [LangGraph](https://langchain-ai.github.io/langgraph)
- [Ollama](https://ollama.com)
- [Mistral](https://mistral.ai)
- [DuckDuckGo Search](https://pypi.org/project/ddgs)

---

## 📄 License
MIT License — feel free to use, modify and distribute.

---

<p align="center">Built by <a href="https://github.com/TuraaCode">TuraaCode</a></p>
