# examples/basic_usage.py
from pyttsgen import TTS

if __name__ == "__main__":
    tts = TTS()  # Uses default voice (en-US-AriaNeural)
    tts.speak_to_file("This is awesome! Welcome to pyttsgen.", "speech.mp3")
    
    # Get raw audio bytes for integration into frameworks (e.g., chatbots)
    audio_bytes = tts.speak_to_bytes("I work in any framework!")
    
    # For example, encode to base64 for APIs or web applications.
    audio_base64 = tts.speak_to_base64("Send me to the browser!")
    
    print("Audio generation successful!")
