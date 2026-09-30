
import os
import requests
import streamlit as st

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
# Hugging Face Model
# ---------------------------------------------------------
HF_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"

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
# Prompt
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
# Get Hugging Face Token
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
    token = os.getenv("HF_TOKEN")

    return token


# ---------------------------------------------------------
# Generate Music
# ---------------------------------------------------------
def generate_music(prompt, token):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(
        HF_URL,
        headers=headers,
        json={
            "inputs": prompt
        },
        timeout=180
    )

    if response.status_code != 200:

        try:
            error_message = response.json()
        except Exception:
            error_message = response.text

        raise RuntimeError(
            f"Music generation failed.\n\n{error_message}"
        )

    return response.content


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

                # Audio player
                st.audio(
                    audio_bytes,
                    format="audio/wav"
                )

                # Download button
                st.download_button(
                    label="⬇️ Download Music",
                    data=audio_bytes,
                    file_name="musicai_generated.wav",
                    mime="audio/wav",
                    use_container_width=True
                )

            except Exception as e:

                st.error(
                    f"Something went wrong:\n\n{e}"
                )


# ---------------------------------------------------------
# Project Information
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
    the Hugging Face Inference API.
    """
)

st.caption(
    "Built with Python • Streamlit • Generative AI • MusicGen"
)
