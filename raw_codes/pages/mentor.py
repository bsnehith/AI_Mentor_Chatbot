import streamlit as st 
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import SystemMessagePromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["HF_TOKEN"]=os.getenv("hf")

st.set_page_config(page_title="Mentor Chatbot")

selection = st.session_state.get('selection', 'No topic selected')
exp= st.session_state.get('exp', 'No experience value set')

st.title("{} Mentor".format(selection))

sm=SystemMessagePromptTemplate.from_template("""You are a senior technical mentor with **{YEARS} years of real-world industry experience**.

Your responsibility is to mentor learners **ONLY in the selected module: {MODULE}**.

AVAILABLE MODULES (FIXED):
- Python
- SQL
- Power BI
- EDA
- Machine Learning
- Deep Learning
- Generative AI
- Agentic AI

MODULE ENFORCEMENT RULES (NON-NEGOTIABLE):
- You MUST answer questions **only if they strictly belong to {MODULE}**.
- If a question involves concepts from ANY other module, you MUST REFUSE.
- You must NOT combine, bridge, or reference other modules in your answers.
- You must NOT provide background knowledge from other domains, even if related.
- You must NOT infer intent — judge strictly by the question content.

REFUSAL RESPONSE (EXACT FORMAT):
This question is outside the selected module ({MODULE}).  
Please ask a question related only to {MODULE}.

ANSWERING GUIDELINES:
- Respond like a mentor with {YEARS} years of practical experience.
- Be precise, concise, and technically accurate.
- Use examples ONLY if they belong strictly to {MODULE}.
- Avoid generic explanations or cross-domain references.
- No assumptions, no extrapolation, no deviation.

You must follow these rules **without exception**.
""")

system_message = sm.format(YEARS=exp, MODULE=selection)

if "last_module" not in st.session_state:
    st.session_state["last_module"]=selection
    
    if "conv" not in st.session_state:
        st.session_state["conv"] = []
        st.session_state["memory"] = [("system", system_message.content)]

if st.session_state["last_module"] != selection:
    st.session_state["conv"]=[]
    st.session_state["memory"].append(("system",system_message.content))
    st.session_state["last_module"]=selection
    

# if "conv" not in st.session_state:
#         st.session_state["conv"] = []
#         st.session_state["memory"] = [("system", system_message.content)]

# st.write(system_message.content)

for y in st.session_state["conv"]:
    with st.chat_message(y["role"]):
        st.write(y["content"])

prompt=st.chat_input("Type Question")

if prompt:
    st.session_state["conv"].append({"role":"user","content":prompt})
    st.session_state["memory"].append(("user",prompt))
    
    with st.chat_message("user"):
        st.write(prompt)
    
    chat_model=True
    if selection  in ["Python","EDA"]:
        model=HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V3.2")
        # chat_model=False
        # llm=ChatHuggingFace(llm=model)
    elif selection  in ["SQL","Power BI"]:
        model=HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.2-1B-Instruct")
        # llm=ChatHuggingFace(llm=model)
    elif selection  in ["Machine Learning","Deep Learning"]:
        model=HuggingFaceEndpoint(repo_id="Qwen/Qwen2-7B")
        # llm=ChatHuggingFace(llm=model)
    elif selection  in ["Generative AI","Agentic AI"]:
        model=HuggingFaceEndpoint(repo_id="XiaomiMiMo/MiMo-V2-Flash")
        # llm=ChatHuggingFace(llm=model)
        
    if chat_model:
        llm=ChatHuggingFace(llm=model)
        response_llm=llm.invoke(st.session_state["memory"])
        response=response_llm.content
    else:
        response=model.invoke(prompt)
        
    with st.chat_message("ai"):
        st.write(response)
    
    st.session_state["conv"].append({"role":"ai","content":response})
    st.session_state["memory"].append(("ai",response))
    

            
    conversation_text=""
    for message in st.session_state["conv"]:
        conversation_text += f"{message['role'].capitalize()} : {message['content']}\n\n"
    
    if conversation_text:
      st.download_button(
          label="📥 Download Chat History",
          data=conversation_text,
          file_name="chat_history.txt",
          mime="text/plain"
          )

