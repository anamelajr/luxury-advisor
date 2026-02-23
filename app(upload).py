import streamlit as st
import anthropic

st.set_page_config(page_title="Luxury Advisor", page_icon="🖤", layout="centered")

st.markdown("""
    <style>
    body { background-color: #0a0a0a; }
    .stApp { background-color: #0a0a0a; color: #f0f0f0; }
    h1 { font-family: Georgia, serif; letter-spacing: 0.15em; color: #f0f0f0; }
    .stTextInput > div > div > input {
        background-color: #1a1a1a;
        color: #f0f0f0;
        border: 1px solid #333;
        border-radius: 0px;
    }
    .stButton > button {
        background-color: #000;
        color: #f0f0f0;
        border: 1px solid #f0f0f0;
        border-radius: 0px;
        letter-spacing: 0.15em;
        width: auto;
        padding: 0.75em 3em;
        margin-top: 1em;
    }
    .stButton > button:hover {
        background-color: #f0f0f0;
        color: #000;
    }
    .result-box {
        background-color: #111;
        border-left: 2px solid #f0f0f0;
        padding: 1.5em;
        margin-top: 1.5em;
        font-family: Georgia, serif;
        line-height: 1.8;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>LUXURY ADVISOR</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#888; letter-spacing:0.1em; font-size:0.85em;'>AI-POWERED FASHION CURATION</p>", unsafe_allow_html=True)
st.markdown("---")

client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

def luxury_advisor(vibe, budget, occasion):
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": f"""You are an expert luxury fashion advisor.

A client is looking for recommendations:
- Aesthetic/Vibe: {vibe}
- Budget: {budget} (this is a HARD limit. Every single product recommended must be purchasable within this budget. If the budget is low, recommend affordable brands and high street options, never luxury brands above this price point)
- Occasion: {occasion}

Give them:
1. 3 brand recommendations with one sentence explanation each
2. 2 specific product suggestions with price and where to find it
3. One styling tip

Be specific and speak like a high-end personal stylist."""}
        ]
    )
    return message.content[0].text

col1, col2, col3 = st.columns(3)
with col1:
    vibe = st.text_input("AESTHETIC / VIBE")
with col2:
    budget = st.text_input("BUDGET")
with col3:
    occasion = st.text_input("OCCASION")

st.markdown("")

if st.button("GET RECOMMENDATIONS"):
    if vibe and budget and occasion:
        with st.spinner("Curating your edit..."):
            result = luxury_advisor(vibe, budget, occasion)
            st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please fill in all fields")