from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

domain_input = input("Enter Domain: ")
topic_input= input("Enter Topic: ")

chat_template = ChatPromptTemplate([
    ("system", "You are a {domain} expert "),
    ("human", "Explain in simple terms, what is {topic} ")
])

prompt = chat_template.invoke({
    "domain":domain_input,
    "topic":topic_input
})

print(prompt)