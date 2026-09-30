# MusicAI: Custom Music Generation

## 1. Introduction
MusicAI is a Generative AI project designed to create original instrumental music from textual instructions. Instead of manually composing every part of a track, the user describes the desired musical characteristics and an AI music model generates the corresponding audio.

## 2. Problem Statement
Creating customized background music traditionally requires musical knowledge, instruments, recording equipment, or professional software. MusicAI provides a simple interface through which users can describe the music they need and receive an AI-generated audio track.

## 3. Objectives
1. Build a user-friendly music generation application.
2. Accept natural-language descriptions of music.
3. Allow users to control genre, mood, tempo, and instruments.
4. Generate original instrumental audio using a pretrained GenAI model.
5. Allow playback and download of generated music.

## 4. Methodology
The application collects user preferences and constructs a text prompt. The prompt is submitted to the MusicGen generative model through the Hugging Face Inference API. The model generates audio, which is returned to the Streamlit application for playback and download.

## 5. System Flow
Input → Preference Selection → Prompt Construction → MusicGen → Audio Generation → Playback/Download

## 6. Technologies
Python, Streamlit, Requests, Hugging Face Inference API, Meta MusicGen.

## 7. Expected Output
The system produces a short instrumental audio clip matching the user's requested musical characteristics.

## 8. Conclusion
MusicAI demonstrates a practical application of Generative AI in creative media generation. It provides a simple interface for converting natural-language musical ideas into generated audio.
