import streamlit as st

# Page config
st.set_page_config(
    page_title="SMART FARM AI",
    page_icon="🌾",
    layout="centered"
)

# Custom CSS for colors and vibe
st.markdown("""
<style>
body {
    background-color: #f5fff5;
}
.main {
    background-color: #ffffff;
    border-radius: 15px;
    padding: 20px;
}
h1 {
    color: #2e7d32;
    text-align: center;
}
h3 {
    color: #388e3c;
}
.advice-box {
    background-color: #e8f5e9;
    padding: 15px;
    border-radius: 12px;
    border-left: 6px solid #43a047;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🌱 SMART FARM AI</h1>", unsafe_allow_html=True)
st.markdown("<h3>Simple farming advice made easy</h3>", unsafe_allow_html=True)

# Inputs
location = st.text_input("📍 Enter your location", placeholder="e.g. Maharashtra, India")
question = st.text_input("💬 Ask your farming question", placeholder="e.g. What crop should I grow in August?")

# Button
if st.button("🌾 Get Advice"):
    if not location or not question:
        st.warning("Please enter both location and question.")
    else:
        q = question.lower()

        st.markdown('<div class="advice-box">', unsafe_allow_html=True)
        st.markdown("### ✅ Recommended Advice")

        # Crop related
        if "crop" in q or "grow" in q or "plant" in q:
            st.write("""
            **Best crop options:**
            - 🌿 **Soybean** – Suitable for monsoon and black soil  
            - 🌾 **Cotton** – Thrives in warm climate  
            - 🌽 **Bajra** – Needs less water, drought-resistant  
            """)

        # Pest related
        elif "pest" in q or "insect" in q or "disease" in q:
            st.write("""
            **Pest control suggestions:**
            - 🐛 Spray **neem oil** for organic control  
            - ✂️ Remove infected leaves early  
            - 💧 Avoid overwatering crops  
            """)

        # Water related
        elif "water" in q or "irrigation" in q:
            st.write("""
            **Water management tips:**
            - 💦 Use **drip irrigation**  
            - ⏰ Water early morning or evening  
            - 🚫 Avoid flooding the field  
            """)

        # Soil related
        elif "soil" in q or "fertilizer" in q:
            st.write("""
            **Soil & fertilizer advice:**
            - 🌱 Add **organic compost**  
            - 🧪 Use soil testing before fertilizers  
            - ♻️ Rotate crops to improve soil health  
            """)

        # Weather related
        elif "rain" in q or "weather" in q:
            st.write("""
            **Weather-based guidance:**
            - ☁️ Delay sowing if heavy rain is expected  
            - 🌞 Harvest during dry periods  
            - 📅 Check weekly weather updates  
            """)

        # Fallback
        else:
            st.write("""
            **General farming tips:**
            - 🌍 Follow sustainable farming practices  
            - 📊 Monitor crop health regularly  
            - 🤝 Seek expert advice when needed  
            """)

        st.markdown(f"*📌 Location considered: **{location}***")
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<center>🌾 Built for FA-2 | Smart Farming Assistant</center>",
    unsafe_allow_html=True
)
