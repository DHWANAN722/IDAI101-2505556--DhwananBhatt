import streamlit as st
import pandas as pd
import random

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="SMART FARM AI",
    page_icon="🚜",
    layout="wide"
)

# ---------- NEON / GRADIENT STYLES ----------
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
}
.main {
    background: rgba(255,255,255,0.05);
}
h1, h2, h3, h4 {
    color: #00ffcc;
}
.card {
    background: rgba(0,0,0,0.6);
    padding: 20px;
    border-radius: 15px;
    border: 2px solid #00ffcc;
    color: #ffffff;
    margin-bottom: 20px;
}
.footer {
    text-align: center;
    color: #cccccc;
}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR (ACCOUNT / SETTINGS) ----------
st.sidebar.title("👤 Account Settings")

username = st.sidebar.text_input("Username", "Farmer01")
language = st.sidebar.selectbox("Language", ["English", "Hindi", "Marathi"])
theme = st.sidebar.selectbox("Theme", ["Neon", "Dark", "Green"])
notifications = st.sidebar.checkbox("Enable Alerts", True)

st.sidebar.markdown("---")
st.sidebar.write("Logged in as:", username)

# ---------- MAIN TITLE ----------
st.markdown("<h1>🚜 SMART FARM AI</h1>", unsafe_allow_html=True)
st.markdown("### Neon-powered smart farming assistant")

# ---------- INPUT SECTION ----------
col1, col2 = st.columns(2)

with col1:
    location = st.selectbox(
        "📍 Select Location",
        ["Maharashtra, India", "Punjab, India", "Ghana", "Canada"]
    )

with col2:
    question_type = st.selectbox(
        "❓ What do you need help with?",
        ["Crop Recommendation", "Pest Control", "Water Management", "Soil & Fertilizer", "Weather Advice"]
    )

st.markdown("---")

# ---------- LOGIC (THIS FIXES THE SAME-ANSWER BUG) ----------
responses = {
    "Maharashtra, India": {
        "Crop Recommendation": ["Soybean", "Cotton", "Bajra"],
        "Pest Control": ["Neem oil spray", "Early leaf removal", "Light irrigation"],
        "Water Management": ["Drip irrigation", "Morning watering", "Mulching"],
        "Soil & Fertilizer": ["Organic compost", "Crop rotation", "Soil testing"],
        "Weather Advice": ["Avoid sowing before heavy rain", "Harvest in dry window"]
    },
    "Punjab, India": {
        "Crop Recommendation": ["Wheat", "Rice", "Maize"],
        "Pest Control": ["Pheromone traps", "Balanced pesticide use"],
        "Water Management": ["Canal irrigation", "Laser land leveling"],
        "Soil & Fertilizer": ["Nitrogen control", "Green manure"],
        "Weather Advice": ["Monitor frost warnings"]
    },
    "Ghana": {
        "Crop Recommendation": ["Maize", "Cassava", "Groundnut"],
        "Pest Control": ["Ash-based control", "Neem extract"],
        "Water Management": ["Rainwater harvesting"],
        "Soil & Fertilizer": ["Organic mulch"],
        "Weather Advice": ["Plant after consistent rainfall"]
    },
    "Canada": {
        "Crop Recommendation": ["Wheat", "Barley", "Canola"],
        "Pest Control": ["Cold-resistant pest monitoring"],
        "Water Management": ["Snowmelt planning"],
        "Soil & Fertilizer": ["Nitrogen balancing"],
        "Weather Advice": ["Frost protection measures"]
    }
}

# ---------- BUTTON ----------
if st.button("⚡ Generate Smart Advice"):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"### 📊 Advice for **{location}**")

    advice = responses[location][question_type]

    for item in advice:
        st.write("✅", item)

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- GRAPH SECTION ----------
    st.markdown("### 📈 Resource Impact Analysis")

    data = {
        "Factor": ["Water Use", "Cost", "Risk", "Sustainability"],
        "Score": [
            random.randint(40, 90),
            random.randint(40, 90),
            random.randint(40, 90),
            random.randint(40, 90)
        ]
    }

    df = pd.DataFrame(data)
    st.bar_chart(df.set_index("Factor"))

# ---------- FOOTER ----------
st.markdown("---")
st.markdown(
    "<div class='footer'>FA-2 Prototype | Smart Farm AI | Streamlit Deployment</div>",
    unsafe_allow_html=True
)
