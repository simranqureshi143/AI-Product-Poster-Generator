import streamlit as st
import ollama

# Connect to Ollama server
client = ollama.Client(host="http://localhost:11434")

st.set_page_config(page_title="Poster Generator", layout="centered")

st.title("🧴 AI Product Poster Generator (Gemma)")

# Fixed poster values
brand_style = "Minimal, clean, pastel theme"
headline = "Premium Organic Skincare"
subheadline = "Glow naturally with our new formula"
price = "Only ₹999"
cta = "Shop Now"
extra = "Professional, aesthetic, modern ecommerce poster"

if st.button("Generate Poster Text"):
    st.write("⏳ Generating poster... Please wait...")

    prompt = f"""
Create an aesthetic product poster text.

🎨 Brand Style: {brand_style}
📝 Headline: {headline}
✨ Subheadline: {subheadline}
💰 Price: {price}
🛒 Call to Action: {cta}
📌 Extra Details: {extra}

Return only the poster text.
"""

    try:
        # Ask Gemma model for text
        response = client.chat(
            model="gemma:2b",
            messages=[{"role": "user", "content": prompt}]
        )

        # Show poster text
        poster_text = response["message"]["content"]
        st.subheader("📣 Poster Preview (Text)")
        st.markdown(poster_text)

        # Show the image you uploaded
        st.subheader("🖼️ Poster Image")
        st.image("A_promotional_digital_graphic_design_advertisement.png")

    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.info("Try running: ollama run gemma:2b")




