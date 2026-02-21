import streamlit as st
import anthropic

client = anthropic.Anthropic(api_key="your-api-key-here")

def luxury_advisor(vibe, budget, occasion):
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": f"""You are an expert luxury fashion advisor.
            
A client is looking for recommendations:
- Aesthetic/Vibe: {vibe}
- Budget: {budget} (strict limit, do not recommend anything above this)
- Occasion: {occasion}

Give them:
1. 3 brand recommendations with one sentence explanation each
2. 2 specific product suggestions with price and where to find it
3. One styling tip

Be specific and speak like a high-end personal stylist."""}
        ]
    )
    return message.content[0].text

st.title("Luxury Advisor")
st.write("AI-powered luxury fashion recommendations")

vibe = st.text_input("Describe your aesthetic/vibe")
budget = st.text_input("Budget (e.g. €500)")
occasion = st.text_input("Occasion")

if st.button("Get Recommendations"):
    if vibe and budget and occasion:
        with st.spinner("Generating your edit..."):
            result = luxury_advisor(vibe, budget, occasion)
            st.markdown(result)
    else:
        st.warning("Please fill in all fields")