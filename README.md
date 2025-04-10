# Personal_voice_activated_AI_assistant
This is a personal voice-activated AI assistant for your personal computer. It uses the latest LLM models, like DeepSeek, but you can also use any other LLM models.
# Personal_voice_activated_AI_assistant
This is an personal voice activated AI assistant for your personal computer using latest LLM models like deepseek and you can use any other LLM model also 
 # Personal Voice Activated AI Assistant

This is a personal voice-activated AI assistant for your computer. It leverages the latest LLM models, such as `deepseek-r1`, and can be configured to use other LLM models as well.

## Features
- Voice recognition using `speech_recognition`.
- Text-to-speech responses using `pyttsx3`.
- Integration with local or remote LLM models like `deepseek-r1`.
- Customizable to use other LLMs via APIs or local inference.

## Prerequisites
- Python 3.7 or higher
- Required Python libraries:
  - `requests`
  - `speech_recognition`
  - `pyttsx3`
  - `ollama` (optional, for local model inference)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/Personal_voice_activated_AI_assistant.git
   cd Personal_voice_activated_AI_assistant

2. Install and configure ollama(optional, for local model inference):
 - Download and install ollama from https://ollama.com/
 -pull the deepseek-r1 model:
 
 ollama pull deepseek-r1

3.Start the ollama server (if using local inference):
ollama serve
 You can change the bind address using the OLLAMA_HOST environment variable.

 On Linux / macOS (bash): 
 export OLLAMA_HOST=Your_Ip_address:11434
 ollama serve

 On Windows (Command Prompt):
 set OLLAMA_HOST=Your_Ip_address:11434
 ollama serve

On Windows (PowerShell):
$env:OLLAMA_HOST="Your_Ip_address:11434"
ollama serve


4. Run the assistant:
python LLM_main.py


Speak into your microphone when prompted. The assistant will recognize your speech, process it using the LLM, and respond via text-to-speech.


5. Configuration
To use a different LLM model, update the model field in the askme function in LLM_main.py:

data = {
    "model": "your-model-name",
    "messages": conversation,
    "stream": False
}

If using a remote LLM API, replace the url in the askme function with the appropriate endpoint.
