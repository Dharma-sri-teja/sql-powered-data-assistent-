from langchain_ollama import ChatOllama

# Connect to the local Ollama model
llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0,
)

# Send a test question
response = llm.invoke("What is SQL? Explain in two simple sentences.")

# Display the response
print("AI RESPONSE:")
print(response.content)
