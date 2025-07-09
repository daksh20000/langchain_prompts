from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chat_history = [
    SystemMessage(content="You are an helpful AI assistant")
]

print("AI: How can I help you today")
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if(user_input =="exit"):
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)

print(chat_history)