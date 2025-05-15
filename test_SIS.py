import streamlit as st
from ultralytics import solutions
import os
from PIL import Image

st.set_page_config(page_title="Visual AI Search", layout="centered")

st.markdown("<h1 style='text-align: center;'>🧠 Visual AI Search</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Select an image folder, enter a prompt, and find similar images using Ultralytics.</p>", unsafe_allow_html=True)

# --- Folder Selection ---
folder_path = st.text_input("📁 Enter full path to the image folder")

# --- Search Prompt ---
prompt = st.text_input("📝 Enter your search prompt:")

# --- Options ---
col1, col2 = st.columns(2)
with col1:
    device = st.selectbox("💻 Device", ["cpu", "cuda"])
with col2:
    top_k = st.slider("🎯 Top-K Results", min_value=1, max_value=20, value=5)

# --- Run Search ---
if st.button("🚀 Run Search"):
    if not os.path.exists(folder_path):
        st.error("❌ Folder does not exist.")
    elif not prompt.strip():
        st.warning("Please enter a valid search prompt.")
    else:
        with st.spinner("🔍 Searching..."):
            searcher = solutions.VisualAISearch(data=folder_path, device=device)
            results = searcher(prompt)

        st.success(f"Top {top_k} results for: '{prompt}'")

        for match in results[:top_k]:
            img_path = os.path.join(folder_path, match)  # match is a string filename

            cols = st.columns([1, 4, 1])
            with cols[1]:  # center column
                st.image(img_path, width=300, caption=os.path.basename(match))


# --- FOOTER ---
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 18px;'>Built by ❤️| Powered by Ultralytics</p>
""", unsafe_allow_html=True)

