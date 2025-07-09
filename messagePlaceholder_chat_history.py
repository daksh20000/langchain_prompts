from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
import os

chat_template= ChatPromptTemplate([
    ("system", "You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{query}")
])

chat_history = []

file_path = 'chatHistory.txt'

if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        chat_history.extend(f.readlines())
else:
    print(f"'{file_path}' not found. Starting with empty chat history.")
    chat_history = []

print(chat_history)

prompt = chat_template.invoke({
    "chat_history":chat_history,
    "query":"what is my order number"
})
print(prompt)
