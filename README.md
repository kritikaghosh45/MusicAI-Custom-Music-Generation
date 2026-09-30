# MusicAI: Custom Music Generation 🎵

## Project Domain
**Generative AI (GenAI)**

## Project Overview
MusicAI is a Generative AI application that creates original short instrumental music from natural-language prompts. Users can specify a genre, mood, tempo, and instruments. The application converts these preferences into a text prompt and sends it to a pretrained music-generation model.

## Key Features
- Natural-language music prompts
- Genre selection
- Mood selection
- Tempo selection
- Instrument selection
- AI-generated instrumental audio
- In-browser audio playback
- WAV download
- Simple Streamlit interface

## Technology Stack
- Python
- Streamlit
- Hugging Face Inference API
- Meta MusicGen (`facebook/musicgen-small`)
- Requests

## Architecture
User Preferences → Prompt Builder → MusicGen Model → Generated Audio → Streamlit Player/Download

## How to Run

### 1. Clone the repository
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd MusicAI_Custom_Music_Generation
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get a Hugging Face token
Create an access token from your Hugging Face account with permission to use inference.

### 4. Run the application
```bash
streamlit run app.py
```

The application will open in your browser.

## Example Prompts
- Calm lo-fi piano music for studying
- Energetic electronic music with synths and drums
- Peaceful cinematic music with piano and strings
- Happy pop instrumental with guitar and light percussion

## Project Objective
The objective is to demonstrate how Generative AI can transform human language instructions into creative audio content.

## Future Enhancements
- Longer music generation
- Melody and chord controls
- User-uploaded reference audio
- Automatic looping
- Genre-specific presets
- Background music generation for videos
- User accounts and saved generations
- Cloud deployment

## Note
This project uses a pretrained Generative AI model through an inference API. Generated audio should be used in accordance with the model provider's terms and applicable copyright/licensing requirements.
