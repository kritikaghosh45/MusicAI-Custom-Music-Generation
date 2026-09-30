import os
import io
import numpy as np
import soundfile as sf
import streamlit as st
from huggingface_hub import InferenceClient


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="MusicAI - Custom Music Generation",
    page_icon="🎵",
    layout="centered"
)


# ---------------------------------------------------------
# Title
# ---------------------------------------------------------

st.title("🎵 MusicAI: Custom Music Generation")

st.write(
    "Create personalized instrumental music using Generative AI. "
    "Choose your mood, genre, tempo, and instruments."
)


# ---------------------------------------------------------
# Hugging Face Token
# ---------------------------------------------------------

def get_hf_token():

    # Streamlit Cloud Secrets
    try:
        token = st.secrets["HF_TOKEN"]

        if token:
            return token

    except Exception:
        pass

    # Local environment variable
    return os.getenv("HF_TOKEN")


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:

    st.header("🎛️ Music Settings")

    genre = st.selectbox(
        "Genre",
        [
            "Pop",
            "Lo-fi",
            "Classical",
            "Rock",
            "Electronic",
            "Jazz",
            "Cinematic"
        ]
    )

    mood = st.selectbox(
        "Mood",
        [
            "Happy",
            "Calm",
            "Energetic",
            "Sad",
            "Dreamy",
            "Epic",
            "Peaceful"
        ]
    )

    tempo = st.selectbox(
        "Tempo",
        [
            "Slow",
            "Medium",
            "Fast"
        ]
    )

    instruments = st.text_input(
        "Instruments",
        "piano, soft drums"
    )


# ---------------------------------------------------------
# Music Prompt
# ---------------------------------------------------------

default_prompt = (
    f"A {mood.lower()} {genre.lower()} instrumental track "
    f"with {instruments}, {tempo.lower()} tempo"
)

prompt = st.text_area(
    "🎼 Describe the music you want",
    value=default_prompt,
    height=100
)


st.info(
    "Example: Calm cinematic piano music with soft strings "
    "for studying and relaxation."
)


# ---------------------------------------------------------
# Generate Music
# ---------------------------------------------------------

def generate_music(prompt, token):

    client = InferenceClient(
        provider="hf-inference",
        api_key=token
    )

    # Check whether the deployed Hugging Face library
    # supports text-to-audio
    if not hasattr(client, "text_to_audio"):
        raise RuntimeError(
            "The deployed Hugging Face library does not support "
            "text_to_audio(). Please reboot the Streamlit app "
            "after updating requirements.txt."
        )

    result = client.text_to_audio(
        prompt,
        model="facebook/musicgen-small"
    )

    audio = result.audio
    sampling_rate = result.sampling_rate

    buffer = io.BytesIO()

    sf.write(
        buffer,
        np.asarray(audio),
        int(sampling_rate),
        format="WAV"
    )

    buffer.seek(0)

    return buffer.read()

# ---------------------------------------------------------
# Generate Button
# ---------------------------------------------------------

if st.button(
    "🎵 Generate Music",
    type="primary",
    use_container_width=True
):

    token = get_hf_token()

    if not token:

        st.error(
            "Hugging Face token is not configured. "
            "Please add HF_TOKEN in Streamlit Secrets."
        )

    elif not prompt.strip():

        st.warning(
            "Please enter a description for the music."
        )

    else:

        with st.spinner(
            "🎶 AI is composing your music..."
        ):

            try:

                audio_bytes = generate_music(
                    prompt,
                    token
                )

                st.success(
                    "✅ Music generated successfully!"
                )

                st.audio(
                    audio_bytes,
                    format="audio/wav"
                )

                st.download_button(
                    label="⬇️ Download Music",
                    data=audio_bytes,
                    file_name="musicai_generated.wav",
                    mime="audio/wav",
                    use_container_width=True
                )

            except Exception as e:

                st.error(
                    f"Music generation failed:\n\n{e}"
                )


# ---------------------------------------------------------
# About Project
# ---------------------------------------------------------

st.divider()

st.subheader("🤖 About MusicAI")

st.write(
    """
    **MusicAI** is a Generative AI application that converts
    natural-language instructions into original instrumental
    music.

    Users can customize:

    - 🎵 Genre
    - 😊 Mood
    - ⚡ Tempo
    - 🎹 Instruments

    The application uses Meta's **MusicGen** model through
    Hugging Face Inference Providers.
    """
)

st.caption(
    "Built with Python • Streamlit • Generative AI • MusicGen"
)
