import streamlit as st

st.set_page_config(page_title="SMART FARM AI")

st.title("SMART FARM AI")
st.subheader("AI-powered farming advice")

location = st.text_input("Enter your location (e.g., Maharashtra, India)")
question = st.text_input("Ask your farming question")

if st.button("Get Advice"):
    if location and question:
        st.markdown("### 🌱 Farming Advice")

        # Pretending this is Gemini's response
        if "crop" in question.lower():
            st.write("""
            - **Soybean** – Suitable for monsoon season and black soil  
            - **Cotton** – Grows well in warm climate  
            - **Bajra** – Requires less water and is drought-resistant  
            """)

        elif "pest" in question.lower():
            st.write("""
            - Use **neem oil spray** for organic pest control  
            - Remove infected leaves early  
            - Avoid overwatering  
            """)

        elif "water" in question.lower():
            st.write("""
            - Use drip irrigation  
            - Water early morning  
            - Avoid excess irrigation  
            """)

        else:
            st.write("""
            - Monitor weather conditions  
            - Maintain soil health  
            - Use sustainable farming practices  
            """)
    else:
        st.warning("Please enter both location and question.")
