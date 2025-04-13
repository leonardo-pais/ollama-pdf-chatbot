# ollama-pdf-chatbot

A chatbot application that answers questions about a PDF document using LangChain and Ollama.

## Features

- Load and process PDF documents.
- Use advanced embeddings and language models from Ollama.
- Retrieve and format document content for question answering.
- Interactive and simple question-and-answer loop.
- This project was developed using uv (An extremely fast Python package and project manager, written in Rust)
- https://docs.astral.sh/uv/

## Requirements
- Ollama
- Dependencies listed in `uv.lock`

## Installation and Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/leonardo-pais/ollama-pdf-chatbot

2. Install Ollama:
   https://ollama.com/download

3. After installing Ollama, it's time to install the models
   ```bash
   ollama pull llama3
   ollama pull znbang/bge:small-en-v1.5-f32

4. Install dependecies listed in `uv.lock`
   ```bash
   uv install

5. Run application
   ```bash
   uv run app/main.py


## Example
Use the provided example PDF, the_curious_fox.pdf, to test the chatbot.
The chatbot will answer questions based on the content of the PDF.

![Example Image](example.png)

## Project Structure

ollama-pdf-chatbot/
├── app/
│   ├── data/                # Directory for PDF files
│   ├── main.py              # Main application script
├── [uv.lock](uv.lock)                  # Dependency lock file
├── [README.md](README.md)              # Project documentation
├── [example.png](example.png)          # .png from example execution  
├── [.gitignore](.gitignore)
├── [pyproject.toml](pyproject.toml)
├── [.python-version](.python-version)