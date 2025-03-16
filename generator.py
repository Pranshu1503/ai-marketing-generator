from transformers import pipeline
import streamlit as st

# Initialize the generator
generator = pipeline("text-generation", model="distilgpt2")

def generate_ad_copy(brand_name, product_description, target_audience, tone="Exciting"):
    tone_prompt = f"Use a {tone.lower()} tone"
    prompt = (
        f"{tone_prompt}. Generate a catchy ad headline (max 10 words) and a 2-3 sentence marketing description "
        f"for {brand_name}. Product: {product_description}. Target audience: {target_audience}. "
        "Be creative, concise, and engaging."
    )
    
    result = generator(prompt, max_length=150, num_return_sequences=1, temperature=0.9, truncation=True)
    generated_text = result[0]["generated_text"].replace(prompt, "").strip()
    lines = [line.strip() for line in generated_text.split(". ") if line.strip()]
    
    headline = lines[0][:10] if lines else f"{brand_name} Unleashes Greatness!"
    headline = " ".join(headline.split()[:10])
    
    description_lines = lines[1:4] if len(lines) > 1 else [f"Discover {brand_name}'s amazing product now!"]
    description = ". ".join(description_lines[:3]) + "."
    
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
    
    brand = st.text_input("Brand Name", "FitLife")
    product = st.text_area("Product/Service Description", "A smart fitness tracker with heart rate monitoring")
    audience = st.text_input("Target Audience", "Fitness enthusiasts")
    tone = st.selectbox("Tone", ["Exciting", "Professional", "Casual"], index=0)
    
    if st.button("Generate Ad Copy"):
        headline, description, cta = generate_ad_copy(brand, product, audience, tone)
        st.subheader("Generated Ad Copy")
        st.write(f"**Headline:** {headline}")
        st.write(f"**Description:** {description}")
        st.write(f"**Call-to-Action:** {cta}")

if __name__ == "__main__":
    main()