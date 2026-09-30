import os
import io
import base64
import requests
import streamlit as st

st.set_page_config(page_title="MusicAI - Custom Music Generation", page_icon="🎵", layout="centered")

st.title("🎵 MusicAI: Custom Music Generation")
st.write("Generate short, original music from a natural-language prompt using a Generative AI music model.")

HF_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"

with st.sidebar:
    st.header("Generation Settings")
    genre = st.selectbox("Genre", ["Pop", "Lo-fi", "Classical", "Rock", "Electronic", "Jazz", "Cinematic"])
    mood = st.selectbox("Mood", ["Happy", "Calm", "Energetic", "Sad", "Dreamy", "Epic", "Peaceful"])
    tempo = st.selectbox("Tempo", ["Slow", "Medium", "Fast"])
    duration = st.slider("Approx. duration (seconds)", 4, 12, 6)
    instruments = st.text_input("Instruments", "piano, soft drums")

prompt = st.text_area(
    "Describe the music you want",
    f"A {mood.lower()} {genre.lower()} instrumental track with {instruments}, {tempo.lower()} tempo"
)

def generate_music(text, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(
        HF_URL,
        headers=headers,
        json={"inputs": text},
        timeout=180
    )
    if response.status_code != 200:
        raise RuntimeError(f"Generation failed ({response.status_code}): {response.text[:500]}")
    return response.content

if st.button("🎼 Generate Music", type="primary"):
    token = os.getenv("HF_TOKEN") or st.session_state.get("hf_token")
    if not token:
        st.warning("Enter your Hugging Face token below to use the online model.")
    else:
        try:
            with st.spinner("Generating your music..."):
                audio_bytes = generate_music(prompt, token)
            st.success("Music generated successfully!")
            st.audio(audio_bytes, format="audio/wav")
            st.download_button(
                "⬇️ Download Music",
                data=audio_bytes,
                file_name="musicai_generated.wav",
                mime="audio/wav"
            )
        except Exception as e:
            st.error(str(e))

with st.expander("🔑 Hugging Face Token"):
    st.caption("Create a Hugging Face access token with inference permission and paste it here. It is used only for this session.")
    st.session_state["hf_token"] = st.text_input("HF_TOKEN", type="password")
