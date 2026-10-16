import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(
    page_title="For My Favourite Person ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load your birthday website HTML file
HTML_FILE = Path(__file__).parent / "index.html"

st.markdown(
    """
    <style>
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        footer {
            visibility: hidden;
        }

        [data-testid="stMainBlockContainer"] {
            padding: 0 !important;
            max-width: 100% !important;
        }

        .stApp {
            background: #10080d;
        }

        iframe {
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Check whether index.html exists
if not HTML_FILE.exists():
    st.error(
        "index.html not found! Upload index.html "
        "into the same GitHub repository folder as app.py."
    )
    st.stop()

# Display the complete birthday website
html_content = HTML_FILE.read_text(encoding="utf-8")

components.html(
    html_content,
    height=1000,
    scrolling=True
)
