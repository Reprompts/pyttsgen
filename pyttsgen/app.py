import asyncio
import os
import edge_tts
import streamlit as st
import nest_asyncio

# Allow nested asyncio loops (required by Streamlit)
nest_asyncio.apply()

# Available voices
VOICES = {
    "American - Aria":       "en-US-AriaNeural",
    "American - Guy":        "en-US-GuyNeural",
    "British - Libby":       "en-GB-LibbyNeural",
    "Australian - Natasha":  "en-AU-NatashaNeural",
    "British - Ryan":        "en-GB-RyanNeural"
}

# Async TTS call
async def _generate(text: str, voice: str, out_file: str):
    comm = edge_tts.Communicate(text, voice)
    await comm.save(out_file)

def run_tts(text: str, voice: str, out_file: str):
    asyncio.run(_generate(text, voice, out_file))

# --- Streamlit UI ---

st.title("🎤 Personalized Text-to-Speech Generator")
st.write("Enter text, pick a voice, name your file & format, then generate.")

# 1) Text input
text = st.text_area("Your text here:", height=150)

# 2) Voice selection
voice_choice = st.selectbox("Select voice:", list(VOICES.keys()))
selected_voice = VOICES[voice_choice]

# 3) Filename & format
file_stem = st.text_input("Output filename (no extension):", "output")
file_format = st.selectbox("Audio format:", ["mp3"])  # add more if you implement conversion
output_filename = f"{file_stem}.{file_format}"

# 4) Generate button
if st.button("Generate Audio"):
    if not text.strip():
        st.error("⚠️ Please enter some text before generating.")
    else:
        with st.spinner("Generating…"):
            run_tts(text, selected_voice, output_filename)
        st.success("✅ Audio generated!")

        # Read and display
        with open(output_filename, "rb") as f:
            audio_bytes = f.read()

        # 5) Audio player
        st.audio(audio_bytes, format=f"audio/{file_format}")

        # 6) Download button (only on click)
        st.download_button(
            label="Download Audio",
            data=audio_bytes,
            file_name=output_filename,
            mime=f"audio/{file_format}"
        )

        # (Optional) clean up file if you don't want to leave it on disk
        # os.remove(output_filename)
