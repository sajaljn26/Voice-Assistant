
Voice Assistant
This is a Python-based voice assistant that can recognize voice commands, provide news updates, open popular websites, and interact with OpenAI's ChatGPT.

Features
Voice recognition using the speech_recognition library.
Text-to-speech functionality using the pyttsx3 library.
Fetches top news headlines using the NewsAPI.
Opens popular websites like Google, YouTube, Facebook, Twitter, Amazon, Reddit, Wikipedia, GitHub, and StackOverflow.
Interacts with OpenAI's ChatGPT to get responses based on user prompts.
Installation
Clone the repository:

git clone <repository_url>
cd <repository_directory>
Install the required packages:


pip install -r requirements.txt
Set up API keys:

Replace YOUR_NEWSAPI_KEY in the code with your actual NewsAPI key.
Replace YOUR_OPENAI_API_KEY in the code with your actual OpenAI API key.
Usage
Run the script:


python voice_assistant.py
Commands:

Open Websites:
"Open Google"
"Open YouTube"
"Open Facebook"
"Open Twitter"
"Open Amazon"
"Open Reddit"
"Open Wikipedia"
"Open GitHub"
"Open StackOverflow"
Get News:
"News"
"Latest News"
"Headlines"
Exit Program:
"Exit program"
"Close program"
"Stop program"
ChatGPT Interaction:
Any other commands will be processed through ChatGPT.
Example
Start the voice assistant:


python voice_assistant.py
Speak "Money" to activate the assistant.

Give a command, for example, "Open Google".

Dependencies
os
speech_recognition
pyttsx3
webbrowser
sys
newsapi
openai
Make sure to install the dependencies using the provided requirements.txt file.

Notes
Ensure your microphone is properly configured and working.
The assistant will listen for the keyword "Money" to activate and then process commands.
The speech recognition might not be perfect; you might need to repeat commands.
Troubleshooting
If the assistant fails to recognize commands, check your microphone settings.
Make sure you have a stable internet connection for fetching news and interacting with ChatGPT.
Verify that the API keys are correctly set.
License
This project is licensed under the MIT License.


