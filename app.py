import streamlit as st
import google.generativeai as genai

# 1. SET UP THE PAGE (MAKING IT LOOK GOOD)
st.set_page_config(page_title="AgroNova Smart Assistant", page_icon="🌱")

# Custom CSS to make it colourful
st.markdown("""
    <style>
    .main {
        background-color: #f0fdf4;
    }
    .stButton>button {
        background-color: #22c55e;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
    }
    h1 {
        color: #166534;
    }
    .reportview-container {
        margin-top: -2em;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌱 AgroNova: Smart Farmer Assistant")
st.write("Welcome! Get real, region-specific advice for your crops.")

# 2. API KEY SETUP
# In Streamlit Cloud, you will put this in "Secrets"
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')    # 3. USER INPUTS
    col1, col2 = st.columns(2)
    with col1:
        location = st.selectbox("Select your region", ["Canada", "India", "Ghana", "Other"])
    with col2:
        crop = st.text_input("What are you growing?", placeholder="e.g. Maize, Wheat, Rice")

    stage = st.select_slider(
        "What stage is your crop in?",
        options=["Planting", "Growing", "Flowering", "Harvesting"]
    )

    question = st.text_area("What is your specific question?", placeholder="e.g. How much water does my crop need today?")

    # 4. THE MAGIC BUTTON
    if st.button("Get Expert Advice"):
        if not crop or not question:
            st.warning("Please tell me what you are growing and your question!")
        else:
            # This is the "System Instruction" to ensure real advice
            prompt = f"""
            You are a professional Agricultural Scientist. Provide practical, accurate advice for a farmer in {location}.
            The crop is {crop} at the {stage} stage.
            Question: {question}
            
            Instructions for your response:
            1. Use bullet points for clarity.
            2. Give a "Reason Why" for every piece of advice.
            3. Keep the language simple and helpful.
            4. If the question is unsafe or not about farming, politely decline.
            """
            
            with st.spinner("Consulting agricultural records..."):
                response = model.generate_content(prompt)
                st.subheader("📋 Your Farming Plan")
                st.success(response.text)
else:
    st.info("Please enter your Gemini API Key in the sidebar to start.")
