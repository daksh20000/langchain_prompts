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


# if not load_prompt then
# template = PromptTemplate(
#     template="""
#         Please summarize the research paper titled \"{paper_input}\" with the following specifications: 
#         Explanation Style: {style_input}
#         Explanation Length: {length_input}.
#         Mathematical Details:  
#             - Include relevant mathematical equations if present in the paper.  
#             - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
#         2. Analogies:
#             - Use relatable analogies to simplify complex ideas.  
#         If certain information is not available in the paper, respond with: \"Insufficient information available\" instead of guessing.  
#         Ensure the summary is clear, accurate, and aligned with the provided style and length.
#     """,
#     input_variables=[
#         "paper_input",
#         "style_input",
#         "length_input"
#     ],
#     validate_template=True
# ) 
# ----------------then----------------
# prompt = template.invoke({
#     "paper_input":paper_input,
#     "style_input":style_input,
#     "length_input":length_input
# })

template = load_prompt("template.json")

prompt = template.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
})

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)