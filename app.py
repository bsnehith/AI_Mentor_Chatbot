import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["HF_TOKEN"] = os.getenv("hf")

st.set_page_config(
    page_title="AI Mentor Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ===================== ADVANCED CSS + JS =====================
st.markdown("""
<style>

/* --------- Animated Gradient Background --------- */
.stApp {
    background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #141e30);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
    font-family: 'Segoe UI', sans-serif;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* --------- Floating Particles --------- */
.particle {
    position: fixed;
    width: 8px;
    height: 8px;
    background: rgba(255,255,255,0.15);
    border-radius: 50%;
    animation: float 12s infinite linear;
}

@keyframes float {
    from { transform: translateY(100vh) scale(0.6); }
    to { transform: translateY(-10vh) scale(1.2); }
}

/* --------- Glass Card --------- */
.card {
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(18px);
    border-radius: 24px;
    padding: 40px;
    max-width: 540px;
    margin: auto;
    box-shadow: 0 30px 60px rgba(0,0,0,0.45);
    animation: slideUp 0.9s ease;
    transition: transform 0.4s ease;
}

.card:hover {
    transform: scale(1.02);
}

/* --------- Animations --------- */
@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* --------- Title --------- */
.card h1 {
    text-align: center;
    color: white;
    font-size: 2.4rem;
    margin-bottom: 8px;
}

.card p {
    text-align: center;
    color: #dddddd;
    font-size: 1rem;
    margin-bottom: 32px;
}

/* --------- Labels --------- */
label {
    color: white !important;
    font-weight: 600;
}

/* --------- Pills (Modules) --------- */
div[data-baseweb="tag"] {
    background: rgba(255,255,255,0.25) !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: 500;
    transition: all 0.3s ease;
}

div[data-baseweb="tag"]:hover {
    background: rgba(0,198,255,0.45) !important;
    transform: translateY(-2px);
}

/* --------- Button --------- */
div.stButton > button {
    width: 100%;
    height: 52px;
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 16px;
    font-size: 1.05rem;
    font-weight: 700;
    border: none;
    animation: pulse 2s infinite;
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 15px 30px rgba(0,114,255,0.6);
}

/* Button pulse */
@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(0,198,255,0.6); }
    70% { box-shadow: 0 0 0 15px rgba(0,198,255,0); }
    100% { box-shadow: 0 0 0 0 rgba(0,198,255,0); }
}

/* --------- Number Input --------- */
input {
    border-radius: 12px !important;
}

</style>

<!-- Floating Particles -->
<div class="particle" style="left:10%; animation-delay:0s;"></div>
<div class="particle" style="left:25%; animation-delay:2s;"></div>
<div class="particle" style="left:40%; animation-delay:4s;"></div>
<div class="particle" style="left:55%; animation-delay:6s;"></div>
<div class="particle" style="left:70%; animation-delay:8s;"></div>
<div class="particle" style="left:85%; animation-delay:10s;"></div>

<script>
document.addEventListener("DOMContentLoaded", function() {
    const btn = document.querySelector("button");
    if(btn){
        btn.addEventListener("click", () => {
            btn.innerHTML = "✨ Preparing Mentor...";
        });
    }
});
</script>
""", unsafe_allow_html=True)

# ===================== HERO CARD =====================
st.markdown("""
<div class="card">
    <h1>🤖 AI Mentor Chatbot</h1>
    <p>Personalized mentorship powered by AI — tailored to your skills & experience</p>
</div>
""", unsafe_allow_html=True)

# ===================== ORIGINAL LOGIC (UNCHANGED) =====================
MODULES = [
    "Python",
    "SQL",
    "Power BI",
    "EDA",
    "Machine Learning",
    "Deep Learning",
    "Generative AI",
    "Agentic AI"
]

selection = st.pills(
    "📚 Choose Your Learning Path",
    MODULES,
    selection_mode="single"
)

exp = st.number_input(
    "🎓 Your Experience (Years)",
    min_value=1,
    max_value=50,
    value=1,
    step=1
)

btn = st.button("🚀 Start AI Mentorship")

if btn:
    st.session_state["selection"] = selection
    st.session_state["exp"] = exp
    st.switch_page("pages/mentor.py")



