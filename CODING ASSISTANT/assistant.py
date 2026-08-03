"""
assistant.py
------------
This file holds every function that talks to the AI model.
app.py (the Streamlit interface) just calls these functions and
shows the result on screen. Keeping them separate makes the
project easier to read and easier to test.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

client = OpenAI(api_key=API_KEY)

# You can swap this for any chat model your account has access to.
MODEL = "gpt-4o-mini"


def _ask(system_prompt: str, user_prompt: str) -> str:
    """
    One shared function that every feature below calls.
    It sends a system prompt (the instruction for how the AI should behave)
    and a user prompt (the actual code or question) to the model.
    """
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content


def generate_code(request: str) -> str:
    """Turns a plain-English request into working code."""
    system = (
        "You are a coding assistant. Write clean, correct, working code "
        "for the user's request. Add short comments only where the logic "
        "isn't obvious. Reply with code only, no extra explanation."
    )
    return _ask(system, request)


def explain_code(code: str) -> str:
    """Explains what a piece of code does, in plain language."""
    system = (
        "You are a coding tutor. Explain the following code in simple, "
        "everyday language, as if teaching a beginner. Walk through what "
        "it does step by step."
    )
    return _ask(system, code)


def find_bugs(code: str) -> str:
    """Looks for bugs in code and explains the fix."""
    system = (
        "You are a code reviewer. Find bugs or issues in the following code. "
        "For each one, state: the bug, why it happens, and the fix. "
        "If there are no bugs, say so plainly."
    )
    return _ask(system, code)


def convert_code(code: str, target_language: str) -> str:
    """Converts code from one language to another."""
    system = (
        f"You are a code translator. Convert the following code to "
        f"{target_language}, keeping the same logic and behavior. "
        f"Reply with the converted code only."
    )
    return _ask(system, code)


def generate_docs(code: str) -> str:
    """Writes documentation/docstrings for a piece of code."""
    system = (
        "You are a technical writer. Write clear documentation "
        "(docstring style) for the following code, covering what it does, "
        "its parameters, and its return value."
    )
    return _ask(system, code)


def generate_tests(code: str) -> str:
    """Writes pytest unit tests for a function."""
    system = (
        "You are a test engineer. Write pytest unit tests for the following "
        "code. Cover normal cases and edge cases. Reply with test code only."
    )
    return _ask(system, code)
