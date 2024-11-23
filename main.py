import openai
import speech_recognition as sr
import os
import pygame
from openai import OpenAI
import pyttsx3
import tempfile
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Set up OpenAI API key

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

def transcribe_audio(audio):
    recognizer = sr.Recognizer()
    text = recognizer.recognize_google(audio)
    return text

def generate_ai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",  # or your preferred model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def text_to_speech(text):
    # Generate speech using OpenAI API
    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",  # Try different voices: alloy, echo, fable, onyx, nova, shimmer
        input=text
    )

    # Create a temporary file to store the audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_audio.write(response.content)
        temp_audio_path = temp_audio.name

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load and play the audio
    pygame.mixer.music.load(temp_audio_path)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up
    pygame.mixer.quit()
    os.remove(temp_audio_path)

def main():
    print("Welcome to your AI conversation partner!")
    recognizer = sr.Recognizer()
    while True:
        print("Listening...")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        
        try:
            text = transcribe_audio(audio)
            print(f"You said: {text}")
            ai_response = generate_ai_response(text)
            print("AI:", ai_response)
            text_to_speech(ai_response)
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

if __name__ == "__main__":
    main()
