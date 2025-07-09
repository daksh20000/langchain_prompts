from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

st.header("Research Helper Tool")

paper_input = st.selectbox("Select research paper name", ["Attention is all you need",
"BERT: Pre-training of deep bidirectional transformers", "GPT-3: Language models are fewshot learners",
"Diffusion models beat GAN on image synthesis"])

style_input = st.selectbox("Select explanation style", ["Beginner-friendly","Technical", "Code oriented", "Mathematical"])

length_input = st.selectbox("Select explanation length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (Detailed explanation)"])

template = load_prompt("template.json")



if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
    })
    st.write(result.content)