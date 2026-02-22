import streamlit as st
import anthropic
from datetime import datetime

st.set_page_config(page_title="Luxury Advisor", page_icon="🖤", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400&display=swap');

    /* ── Base ── */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #080808 !important;
    }
    .stApp {
        background-color: #080808;
        color: #e8e0d4;
        font-family: 'Inter', sans-serif;
        font-weight: 300;
    }

    /* Hide Streamlit chrome */
    #MainMenu, footer, header { visibility: hidden; }
    [data-testid="stToolbar"] { display: none; }

    /* ── Masthead ── */
    .masthead-rule {
        border: none;
        border-top: 1px solid #e8e0d4;
        margin: 0 0 0.6rem 0;
    }
    .masthead-meta {
        display: flex;
        justify-content: space-between;
        font-family: 'Inter', sans-serif;
        font-size: 0.62rem;
        letter-spacing: 0.22em;
        color: #6a6258;
        text-transform: uppercase;
        margin-bottom: 2.2rem;
    }
    .masthead-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.4rem, 6vw, 4rem);
        font-weight: 400;
        letter-spacing: 0.18em;
        color: #e8e0d4;
        text-align: center;
        line-height: 1;
        margin: 0.4rem 0 0.5rem 0;
    }
    .masthead-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 0.62rem;
        letter-spacing: 0.35em;
        color: #b8a98a;
        text-align: center;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }
    .masthead-rule-bottom {
        border: none;
        border-top: 1px solid #e8e0d4;
        margin: 0 0 2.8rem 0;
    }

    /* ── Input labels ── */
    .stTextInput label {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.6rem !important;
        font-weight: 400 !important;
        letter-spacing: 0.28em !important;
        color: #b8a98a !important;
        text-transform: uppercase !important;
        margin-bottom: 0.4rem !important;
    }

    /* ── Inputs (underline style) ── */
    .stTextInput > div > div > input {
        background-color: transparent !important;
        color: #e8e0d4 !important;
        border: none !important;
        border-bottom: 1px solid #333 !important;
        border-radius: 0 !important;
        padding: 0.4rem 0 0.5rem 0 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.82rem !important;
        font-weight: 300 !important;
        letter-spacing: 0.04em !important;
        box-shadow: none !important;
        outline: none !important;
        transition: border-color 0.25s ease !important;
    }
    .stTextInput > div > div > input:focus {
        border-bottom: 1px solid #b8a98a !important;
        box-shadow: none !important;
    }
    .stTextInput > div > div > input::placeholder {
        color: #3a3530 !important;
        font-style: italic;
    }
    .stTextInput > div {
        border: none !important;
        box-shadow: none !important;
    }

    /* ── Button ── */
    .stButton {
        display: flex;
        justify-content: center;
        margin-top: 2.2rem;
    }
    .stButton > button {
        background-color: transparent !important;
        color: #e8e0d4 !important;
        border: 1px solid #e8e0d4 !important;
        border-radius: 0 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.6rem !important;
        font-weight: 400 !important;
        letter-spacing: 0.3em !important;
        text-transform: uppercase !important;
        padding: 0.85em 3.5em !important;
        width: auto !important;
        transition: background-color 0.25s ease, color 0.25s ease !important;
    }
    .stButton > button:hover {
        background-color: #e8e0d4 !important;
        color: #080808 !important;
    }
    .stButton > button:focus {
        box-shadow: none !important;
        outline: none !important;
    }

    /* ── Spinner ── */
    .stSpinner > div {
        border-top-color: #b8a98a !important;
    }

    /* ── Result ── */
    .result-outer {
        margin-top: 3rem;
        border-top: 1px solid #1e1a16;
        padding-top: 2rem;
    }
    .result-eyebrow {
        font-family: 'Inter', sans-serif;
        font-size: 0.58rem;
        letter-spacing: 0.3em;
        color: #b8a98a;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
    }
    .result-body {
        font-family: 'Playfair Display', serif;
        font-size: 0.92rem;
        line-height: 2;
        color: #cfc8bc;
        border-left: 1px solid #b8a98a;
        padding-left: 1.6rem;
        white-space: pre-wrap;
    }
    .result-rule {
        border: none;
        border-top: 1px solid #1e1a16;
        margin: 2.5rem 0 0 0;
    }

    /* ── Warning ── */
    .stAlert {
        background-color: transparent !important;
        border: 1px solid #3a3530 !important;
        color: #6a6258 !important;
        border-radius: 0 !important;
        font-size: 0.72rem !important;
        letter-spacing: 0.08em !important;
    }

    /* ── Column gap ── */
    [data-testid="stHorizontalBlock"] {
        gap: 2rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# ── Masthead ──────────────────────────────────────────────────────────────────
now = datetime.now()
edition = f"Vol. I  No. {now.strftime('%-m')}  {now.strftime('%B %Y').upper()}"

st.markdown('<hr class="masthead-rule">', unsafe_allow_html=True)
st.markdown(f"""
    <div class="masthead-meta">
        <span>THE STYLE INTELLIGENCE</span>
        <span>{edition}</span>
    </div>
""", unsafe_allow_html=True)
st.markdown('<h1 class="masthead-title">LUXURY ADVISOR</h1>', unsafe_allow_html=True)
st.markdown('<p class="masthead-subtitle">AI&#8202;&#8202;—&#8202;&#8202;Powered Fashion Curation</p>', unsafe_allow_html=True)
st.markdown('<hr class="masthead-rule-bottom">', unsafe_allow_html=True)

# ── API Client ────────────────────────────────────────────────────────────────
client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

def luxury_advisor(vibe, budget, occasion):
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": f"""You are an expert luxury fashion advisor.

A client is looking for recommendations:
- Aesthetic/Vibe: {vibe}
- Budget: {budget} (this is a HARD limit — every product must be within this budget)
- Occasion: {occasion}

Give them:
1. 3 brand recommendations with one sentence explanation each
2. 2 specific product suggestions with price and where to find it
3. One styling tip

Be specific and speak like a high-end personal stylist."""}
        ]
    )
    return message.content[0].text

# ── Inputs ────────────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
with col1:
    vibe = st.text_input("Aesthetic / Vibe", placeholder="e.g. quiet luxury")
with col2:
    budget = st.text_input("Budget", placeholder="e.g. $500")
with col3:
    occasion = st.text_input("Occasion", placeholder="e.g. gallery opening")

if st.button("Get Recommendations"):
    if vibe and budget and occasion:
        with st.spinner("Curating your edit…"):
            result = luxury_advisor(vibe, budget, occasion)
        st.markdown(f"""
            <div class="result-outer">
                <div class="result-eyebrow">Your Curated Edit</div>
                <div class="result-body">{result}</div>
                <hr class="result-rule">
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please complete all three fields to receive your edit.")
