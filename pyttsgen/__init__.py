__version__ = "0.1.2"

from .engine import generate_speech, generate_speech_base64
from .utils import setup_logger

class TTS:
    def __init__(self, voice: str = None):
        from .config import DEFAULT_VOICE
        self.voice = voice if voice else DEFAULT_VOICE
        self.logger = setup_logger()

    def speak_to_file(self, text: str, output_path: str) -> None:
        self.logger.info("Generating speech to file: %s", output_path)
        generate_speech(text, self.voice, output_path)

    def speak_to_bytes(self, text: str) -> bytes:
        self.logger.info("Generating speech to bytes.")
        return generate_speech(text, self.voice)
    
    def speak_to_base64(self, text: str) -> str:
        self.logger.info("Generating speech to base64 string.")
        return generate_speech_base64(text, self.voice)

    def speak_batch_to_files(self, texts: list, output_folder: str = "./") -> None:
        import os
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        for i, text in enumerate(texts, start=1):
            output_path = os.path.join(output_folder, f"output_{i}.mp3")
            self.logger.info("Generating file: %s", output_path)
            generate_speech(text, self.voice, output_path)
