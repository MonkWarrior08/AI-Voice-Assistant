# AI Voice Assistant

## Description
This AI Voice Assistant is an interactive conversation partner that uses speech recognition, natural language processing, and text-to-speech capabilities. It allows users to have spoken conversations with an AI, powered by OpenAI's GPT-4o model and speech services.

## Features
- Real-time speech recognition
- Natural language processing using OpenAI's GPT-4o
- Text-to-speech conversion with multiple voice options
- Interactive conversation flow
- High-quality audio playback

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MonkWarrior08/AI_Voice_Assistant.git
cd AI_Voice_Assistant
```

2. Install dependencies using the requirements file:
```
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage
1. Run the program:
```bash
python main.py
```

2. Start speaking when you see "Listening..." prompt
3. Wait for the AI's response, which will be both displayed and spoken

## Voice Options
Available voices:
- alloy
- echo
- fable
- onyx
- nova
- shimmer

## Error Handling
The program includes error handling for:
- Unrecognized speech
- API communication issues
- Audio playback problems

## License

This project is open source and available under the [MIT License](LICENSE).


