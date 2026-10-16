import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(
    page_title="For My Favourite Person ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep index.html in the same folder as app.py.
HTML_PATH = Path(__file__).parent / "index.html"

st.markdown(
    """
    <style>
      [data-testid="stHeader"], [data-testid="stToolbar"], footer {visibility: hidden;}
      .stApp { background: #10080d; }
      [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        max-width: 100% !important;
      }
      iframe { border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

if not HTML_PATH.exists():
    st.error(
        "Could not find index.html. Upload index.html in the same GitHub repository "
        "and folder as app.py."
    )
    st.stop()

html = HTML_PATH.read_text(encoding="utf-8")
components.html(html, height=950, scrolling=True)
