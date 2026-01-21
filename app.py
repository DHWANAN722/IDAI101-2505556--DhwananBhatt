import streamlit as st
import pandas as pd
import random

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Smart Farm AI",
    page_icon="🌾",
    layout="wide"
)

# ---------- CLEAN STYLING ----------
st.markdown("""
<style>
body {
    background-color: #f4f6f8;
}
h1 {
    color: #2e7d32;
}
.card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.footer {
    text-align: center;
    color: #777777;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1>🌾 Smart Farm AI</h1>", unsafe_allow_html=True)
st.write("A simple web app that provides region-specific farming advice.")

# ---------- LANGUAGE SELECTION (REAL, NOT FAKE) ----------
language = st.selectbox("Select Language", ["English", "Hindi", "Marathi"])

def translate(text):
    translations = {
        "Hindi": {
            "Advice": "सलाह",
            "Resource Analysis": "संसाधन विश्लेषण"
        },
        "Marathi": {
            "Advice": "सल्ला",
            "Resource Analysis": "संसाधन विश्लेषण"
        }
    }
    return translations.get(language, {}).get(text, text)

st.markdown("---")

# ---------- INPUTS ----------
col1, col2 = st.columns(2)

with col1:
    location = st.selectbox(
        "Location",
        ["Maharashtra, India", "Punjab, India", "Ghana", "Canada"]
    )

with col2:
    question_type = st.selectbox(
        "Question Type",
        ["Crop Recommendation", "Pest Control", "Water Management", "Soil & Fertilizer", "Weather Advice"]
    )

# ---------- RESPONSE DATA ----------
responses = {
    "Maharashtra, India": {
        "Crop Recommendation": ["Soybean", "Cotton", "Bajra"],
        "Pest Control": ["Neem oil spray", "Remove infected leaves", "Avoid overwatering"],
        "Water Management": ["Drip irrigation", "Mulching", "Morning watering"],
        "Soil & Fertilizer": ["Organic compost", "Soil testing", "Crop rotation"],
        "Weather Advice": ["Avoid sowing before heavy rain", "Harvest during dry weather"]
    },
    "Punjab, India": {
        "Crop Recommendation": ["Wheat", "Rice", "Maize"],
        "Pest Control": ["Pheromone traps", "Balanced pesticide use"],
        "Water Management": ["Canal irrigation", "Laser land leveling"],
        "Soil & Fertilizer": ["Green manure", "Nitrogen balance"],
        "Weather Advice": ["Watch for frost warnings"]
    },
    "Ghana": {
        "Crop Recommendation": ["Maize", "Cassava", "Groundnut"],
        "Pest Control": ["Neem extract", "Ash-based control"],
        "Water Management": ["Rainwater harvesting"],
        "Soil & Fertilizer": ["Organic mulching"],
        "Weather Advice": ["Plant after steady rainfall"]
    },
    "Canada": {
        "Crop Recommendation": ["Wheat", "Barley", "Canola"],
        "Pest Control": ["Monitor cold-resistant pests"],
        "Water Management": ["Snowmelt planning"],
        "Soil & Fertilizer": ["Nitrogen management"],
        "Weather Advice": ["Protect crops from frost"]
    }
}

# ---------- BUTTON ----------
if st.button("Get Advice"):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"### {translate('Advice')} for **{location}**")

    advice = responses[location][question_type]
    for item in advice:
        st.write("•", item)

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- GRAPH ----------
    st.markdown(f"### {translate('Resource Analysis')}")
    df = pd.DataFrame({
        "Factor": ["Water Use", "Cost", "Risk", "Sustainability"],
        "Score": [random.randint(50, 90) for _ in range(4)]
    })
    st.bar_chart(df.set_index("Factor"))

# ---------- FOOTER ----------
st.markdown("---")
st.markdown(
    "<div class='footer'>FA-2 Smart Farming Assistant | Streamlit Deployment</div>",
    unsafe_allow_html=True
)
