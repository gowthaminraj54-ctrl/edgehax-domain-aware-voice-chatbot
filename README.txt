
EDGEHAX DOMAIN-AWARE VOICE CHATBOT
# Domain-Aware Chatbot – College Rules & FAQs

## Problem Description
This project implements a simple domain-aware chatbot that answers user questions
based only on a predefined knowledge source related to college rules and FAQs.

## Domain Chosen
College Rules & FAQs  
Chosen because the information is structured, easy to verify, and suitable for
demonstrating grounded responses.

## Technology Used
- Programming Language: Python
- Interface: Command Line Interface (CLI)

## Data Source
- Text file located at: data/college_rules.txt

## How the Chatbot Works
1. Loads the knowledge document.
2. Accepts a user question.
3. Matches keywords from the question with the knowledge source.
4. Returns a relevant answer if found.
5. Responds with “I don’t know” if the answer is not present.

## How to Run
1. Install Python 3.10 or above.
2. Open terminal inside the project folder.
3. Run:
   python app.py

## Sample Questions
- What is the attendance rule?
- What are the library timings?
- What are the college working hours?

## LLM & Voice Enhancement
This project was enhanced to use a local 7B parameter LLM via Ollama.
Speech-to-Text is handled using Whisper, and Text-to-Speech using pyttsx3,
enabling full voice-based interaction while keeping responses grounded
in the provided domain document.
