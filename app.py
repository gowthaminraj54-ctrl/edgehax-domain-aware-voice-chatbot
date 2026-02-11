
import ollama
import whisper
import pyttsx3
import speech_recognition as sr
from retriever import load_knowledge, retrieve

# Load STT
stt_model = whisper.load_model("base")

# Load TTS
tts = pyttsx3.init()
tts.setProperty("rate", 170)

def speak(text):
    print("Bot:", text)
    tts.say(text)
    tts.runAndWait()

# Load knowledge
chunks = load_knowledge("college_rules.txt")

def ask_llm(context, question):
    prompt = f"""
You are a domain-specific assistant.
Answer ONLY from the given context.
If answer not in context, say "I don't know based on the provided information."

Context:
{context}

Question:
{question}
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        return text

print("Voice Chatbot Started (Say 'exit' to quit)")

while True:
    try:
        question = voice_input()
        print("You:", question)

        if "exit" in question.lower():
            break

        context = "\n".join(retrieve(question, chunks))
        answer = ask_llm(context, question)

        speak(answer)

    except Exception as e:
        print("Error:", e)
