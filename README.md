# AI Coding Assistant

A Streamlit app that helps with everyday coding tasks: writing code from a
plain-English description, explaining existing code, spotting bugs,
converting code between languages, and generating documentation and tests.

## Why I built this

I wanted hands-on practice with LLM API integration and prompt engineering,
and a working tool I could actually use day to day, not just a tutorial
exercise.

## Features

- Generate code from a description
- Explain what a piece of code does
- Find and explain bugs
- Convert code between languages
- Generate documentation
- Generate pytest unit tests

## How it works

The interface (`app.py`) collects your input in Streamlit and sends it to
`assistant.py`, which builds a prompt and calls the OpenAI API. The response
comes back and is shown directly in the app.

## Setup

1. Clone this repo and move into it:
   ```
   git clone <your-repo-url>
   cd ai-coding-assistant
   ```
2. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate      # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your own OpenAI API key:
   ```
   cp .env.example .env
   ```
4. Run the app:
   ```
   streamlit run app.py
   ```

## Project structure

```
ai-coding-assistant/
├── app.py              # Streamlit interface
├── assistant.py         # Functions that call the AI model
├── requirements.txt
├── .env.example
├── tests/
│   └── test_assistant.py
└── README.md
```

## Possible next steps

- Upload a GitHub repo and analyze it file by file
- Score code quality automatically
- Support multi-file projects instead of single snippets
