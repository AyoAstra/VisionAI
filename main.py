import openai
import os
import speech_recognition as sr
import pyttsx3
import re

# Set up your OpenAI API key
openai.api_key = ("your_open_ai_api_key")

# Set up your prompt and response templates
prompt_template = "{}\nUser: {}\nAI:"
response_template = "{}"

# Set up text-to-speech engine
engine = pyttsx3.init()

# Define your chat function
def chat():
    # Initialize an empty string for your training data
    training_data = ""

    # Set the path to your training data file
    training_data_file = "path/to/training/data/file`/training_data.txt"

    # Load your training data from a text file
    with open(training_data_file, "r") as f:
        training_data = f.read()

    # Listen for user speech input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source)

    # Convert speech input to text
    try:
        user_input = r.recognize_google(audio, language="en-IN")
        print("User input:", user_input)
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
        return "Sorry, I could not understand your speech."
    except sr.RequestError as e:
        print("Sorry, could not request results from Google Speech Recognition service; {0}".format(e))
        return "Sorry, could not request results from Google Speech Recognition service."

    # Set up your OpenAI API parameters
    model_engine = "text-davinci-002"
    prompt_text = prompt_template.format(training_data, user_input)
    temperature = 0.5
    max_tokens = 200

    # Generate your response using OpenAI API
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_text,
        temperature=temperature,
        max_tokens=max_tokens
    )

    # Speak the AI's response
    ai_response = response_template.format(response.choices[0].text.strip())
    print("AI response:", ai_response)
    engine.say(ai_response)
    engine.runAndWait()

    # Return the AI's response
    return ai_response

# Start the chat loop
while True:
    chat()
