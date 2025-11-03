<h1 align="center">LangGraph & LlamaIndex Chatbot Agent</h1>

## Table of Contents
- [1. Overview](#1-overview)
- [2. Folder Structure](#2-folder-structure)
- [3. Setup](#3-setup)
  - [3.1. Prerequisites](#31-prerequisites)
  - [3.2. Installation](#32-installation)
- [4. Usage](#4-usage)
- [5. How it Works](#5-how-it-works)
- [6. Notes](#6-notes)

# 1. Overview
This project provides a user-friendly chatbot agent that combines the LangGraph framework with LlamaIndex for LLM-powered text generation via a local HuggingFace model. The chatbot receives a user question, routes it through a LangGraph agent, which delegates to a LlamaIndex-powered node that produces the answer.

# 2. Folder Structure
- `chatbot_agent.py` — Main Python script combining LangGraph agent and LlamaIndex node for Q&A.
- `requirements.txt` — Python dependencies for both LangGraph and LlamaIndex.
- `.env` — Environment variables (set your HuggingFace model path here).
- `.gitignore` — Files and directories to be ignored by Git.
- `README.md` — Project documentation and setup guide (this file).

# 3. Setup
## 3.1. Prerequisites
- Python 3.8 or higher
- A HuggingFace large language model downloaded on your machine

## 3.2. Installation
1. Clone this repository.
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Edit `.env` and set `HUGGINGFACE_MODEL_PATH` to the path where your model is located (e.g., `C:/path/to/your/huggingface-model`).

# 4. Usage
Run the chatbot via:
```bash
python chatbot_agent.py
```
You will be prompted to enter a question. The chatbot will reply with an answer from your local model using a LangGraph agent whose LLM node is powered by LlamaIndex.

# 5. How it Works
- The conversation flow:
  1. User enters a question.
  2. The LangGraph agent receives the input and passes it to an LLM node.
  3. The node uses LlamaIndex to query the specified HuggingFace LLM for a response.
  4. The answer is printed in the terminal.

# 6. Notes
- No proprietary APIs or paid services: everything runs locally.
- Ensure your HuggingFace model supports text generation and is compatible with `llama_index.llms.HuggingFaceLLM`.
