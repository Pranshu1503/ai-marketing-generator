import ollama
import streamlit as st

def generate_ad_copy(brand_name, product_description, target_audience, tone="Exciting"):
    # Structured prompt for Ollama
    tone_prompt = f"Use a {tone.lower()} tone"
    prompt = (
        f"{tone_prompt}. Write a catchy ad headline (max 10 words) followed by '||' "
        f"and a 2-3 sentence marketing description for {brand_name}. "
        f"Product: {product_description}. Target audience: {target_audience}. "
        "Keep it concise, creative, and engaging."
    )
    
    # Generate text with Ollama
    response = ollama.generate(model="llama3", prompt=prompt)
    generated_text = response["response"].strip()
    
    # Split into headline and description
    if "||" in generated_text:
        headline, description = generated_text.split("||", 1)
    else:
        headline, description = generated_text, ""
    
    # Clean and limit headline
    headline = headline.strip()
    headline_words = headline.split()[:10]  # Max 10 words
    headline = " ".join(headline_words) if headline_words else f"{brand_name} Shines Bright!"
    
    # Clean and ensure complete description
    description = description.strip()
    sentences = [s.strip() for s in description.split(". ") if s.strip()]
    if len(sentences) < 2 or not description:
        description = (
            f"Experience {brand_name}'s {product_description} like never before. "
            f"Perfect for {target_audience}—join the revolution today."
        )
    else:
        description = ". ".join(sentences[:3]) + "."
    
    # Tone-specific CTA
    cta = {
        "exciting": "Grab yours now and ignite your journey!",
        "professional": "Elevate your experience—contact us today.",
        "casual": "Check it out and vibe with us!"
    }.get(tone.lower(), "Act now!")
    
    return headline, description, cta

# Streamlit UI
def main():
    st.title("AI Marketing Copy Generator")
    st.write("Enter details to generate creative ad copy!")

    # Input fields
    brand = st.text_input("Brand Name", "EcoPure")
    product = st.text_area("Product/Service Description", "A reusable water bottle made from recycled materials")
    audience = st.text_input("Target Audience", "Eco-conscious consumers")
    tone = st.selectbox("Tone", ["Exciting", "Professional", "Casual"], index=0)

    # Generate button
    if st.button("Generate Ad Copy"):
        with st.spinner("Generating your ad copy..."):
            headline, description, cta = generate_ad_copy(brand, product, audience, tone)
            st.subheader("Generated Ad Copy")
            st.write(f"**Headline:** {headline}")
            st.write(f"**Description:** {description}")
            st.write(f"**Call-to-Action:** {cta}")

if __name__ == "__main__":
    main()