# AI-Powered Marketing Copy Generator
Personal Project
- A Python tool that generates personalized ad copy using Ollama and local LLMs (e.g., Llama3).

## Requirements
- Python 3.8+
- Ollama (install from ollama.com)
- Libraries: `ollama`, `streamlit` (via pip)

## Installation
1. Install Ollama: `curl -fsSL https://ollama.com/install.sh | sh`
2. Pull a model: `ollama pull llama3`
3. Set up Python env: `pip install -r requirements.txt`

## How to Run
- Start Ollama: `ollama serve`
- CLI: `python generator.py`
- Web UI: `streamlit run generator.py`