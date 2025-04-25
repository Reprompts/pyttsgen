import argparse
import subprocess
from pathlib import Path
from .config import VOICES, DEFAULT_VOICE
from .engine import generate_speech

def list_voices():
    print("Available voices:")
    for name, vid in VOICES.items():
        print(f"  • {name}: {vid}")

def main():
    parser = argparse.ArgumentParser(
        prog="pyttsgen",
        description="pyttsgen — CLI for text-to-speech"
    )
    parser.add_argument("text", nargs="?", help="Text to synthesize")
    parser.add_argument("--voice", default=DEFAULT_VOICE,
                        help="Voice identifier (use --list-voices to see)")
    parser.add_argument("--output", default="output.mp3",
                        help="Where to save the MP3 output")
    parser.add_argument("--list-voices", action="store_true",
                        help="Show available voices and exit")
    parser.add_argument("app", nargs="?", help="Run Streamlit UI: pyttsgen app")
    args = parser.parse_args()

    # Launch the packaged UI if user typed 'app'
    if args.app == "app":
        return launch_app()

    if args.list_voices:
        return list_voices()

    if not args.text:
        parser.print_help()
        print("\nExamples:")
        print("  pyttsgen 'Hello world!'")
        print("  pyttsgen --list-voices")
        print("  pyttsgen app\n")
        return

    generate_speech(args.text, args.voice, args.output)
    print(f"✅ Audio saved to: {args.output}")

def launch_app():
    """
    Launch the Streamlit UI that lives inside the pyttsgen package.
    """
    # Locate pyttsgen/web.py in the installed package
    script = Path(__file__).resolve().parent / "app.py"
    if not script.is_file():
        print(f"❌ Could not find the UI script at {script}")
        return
    # Run streamlit on that file
    subprocess.run(["streamlit", "run", str(script)])
