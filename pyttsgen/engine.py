import asyncio
import base64
import os
import tempfile
from io import BytesIO
import edge_tts
from .config import DEFAULT_VOICE

async def _generate_speech_async(text: str, voice: str, output_path: str = None) -> bytes:
    communicate = edge_tts.Communicate(text, voice)
    if output_path:
        await communicate.save(output_path)
        with open(output_path, "rb") as f:
            return f.read()
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            temp_file = tmp.name
        try:
            await communicate.save(temp_file)
            with open(temp_file, "rb") as f:
                return f.read()
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)

def generate_speech(text: str, voice: str = DEFAULT_VOICE, output_path: str = None) -> bytes:
    return asyncio.run(_generate_speech_async(text, voice, output_path))

def generate_speech_base64(text: str, voice: str = DEFAULT_VOICE) -> str:
    audio_bytes = generate_speech(text, voice)
    return base64.b64encode(audio_bytes).decode('utf-8')
