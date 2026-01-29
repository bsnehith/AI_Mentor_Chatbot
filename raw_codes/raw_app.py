import streamlit as st 
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["HF_TOKEN"]=os.getenv("hf")

st.set_page_config(page_title="AI Mentor Chatbot", page_icon="🤖")
st.title("AI Mentor Chatbot")

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

selection = st.pills("Modules", MODULES, selection_mode="single")

exp=st.number_input("Experience(in years)", min_value=1, max_value=50, value=1, step=1)

btn=st.button("Submit")

if btn:
    st.session_state['selection'] = selection
    st.session_state['exp'] = exp
    st.switch_page("pages/mentor.py")
