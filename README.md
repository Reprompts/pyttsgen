# pyttsgen

**pyttsgen** is a plug-and-play TTS (Text-to-Speech) generator for Python. It supports:

- 🔧 Python scripting
- 🖥️ CLI access
- 🌐 Streamlit UI

## 🔌 Installation

```bash
pip install pyttsgen
🧪 Usage


1. 🧑‍💻 Python Scripting
python

from pyttsgen import TTS

tts = TTS()
tts.speak_to_file("Hello from Python!", "hello.mp3")
audio_bytes = tts.speak_to_bytes("In-memory audio!")
base64_audio = tts.speak_to_base64("Base64 audio for web!")


2. 💻 CLI

pyttsgen "This is CLI-based speech" --voice en-GB-RyanNeural --output speech.mp3
List all voices

pyttsgen --list-voices
Show usage help

pyttsgen


3. 🌐 UI (Streamlit)

Typing "app" in the CLI
Opens a browser UI to enter text and download audio.

