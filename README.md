# Voice-Activated Personal Assistant (Ashria Sir)

## Overview
This Python script implements a voice-activated personal assistant named "Ashria Sir." It utilizes various libraries and APIs to perform tasks such as fetching information from Wikipedia, opening applications, playing music, providing weather forecasts, and more, all through voice commands.

## Requirements
Ensure you have the following libraries installed:
- **pyttsx3**: `pip install pyttsx3`
- **speech_recognition**: `pip install SpeechRecognition`
- **wikipedia**: `pip install wikipedia`
- **pywhatkit**: `pip install pywhatkit`
- **PyPDF2**: `pip install PyPDF2`
- **pyaudio**: `pip install pyaudio` (Note: Requires portaudio. You may need to install it separately.)

## Usage
1. Run the script in a Python environment.
2. Upon execution, Ashria Sir will greet the user and await voice commands.
3. Speak commands such as "Wikipedia [topic]", "Open Notepad," "Play music," "What's the time," etc., to interact with the assistant.
4. Ashria Sir will execute the corresponding tasks based on the command received.

## Features
- Speech recognition and synthesis for hands-free interaction.
- Ability to fetch information from Wikipedia.
- Open applications like Notepad, Command Prompt, Google, and Stack Overflow.
- Play music from a local directory.
- Get the current time and weather forecast for a specified city.
- Send messages using WhatsApp (requires a contacts file).
- Read text content from PDF files.
- Ability to shut down or restart the computer.

## Note
- Make sure to set up the necessary API keys (e.g., OpenWeatherMap API) and permissions (e.g., for sending WhatsApp messages) as required.

## Credits
- This project is created by Harsh Sehgal.
- Special thanks to the creators and contributors of the libraries and APIs used in this project.
