from setuptools import setup, find_packages
from pathlib import Path

def get_version():
    text = Path("pyttsgen/__init__.py").read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Version not found")

long_description = Path("README.md").read_text(encoding="utf-8")

setup(
    name="pyttsgen",
    version=get_version(),
    description="A developer-friendly, plug-and-play TTS library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="RePromptsQuest",
    author_email="repromptsquest@gmail.com",
    packages=find_packages(),
    install_requires=[
        "edge_tts",
        "streamlit",
        "nest_asyncio"
    ],
    entry_points={
        "console_scripts": [
            "pyttsgen=pyttsgen.cli:main",
            "app=pyttsgen.cli:launch_app"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
