# tests/test_engine.py
import unittest
from pyttsgen import TTS

class TestEngine(unittest.TestCase):
    def setUp(self):
        self.tts = TTS()

    def test_speak_to_bytes(self):
        audio = self.tts.speak_to_bytes("Test audio")
        self.assertTrue(isinstance(audio, bytes))
        self.assertGreater(len(audio), 0)

if __name__ == '__main__':
    unittest.main()
