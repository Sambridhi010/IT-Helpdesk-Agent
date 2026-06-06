from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

SYSTEM_PROMPT = """You are an IT helpdesk assistant. 
You help employees with common IT issues like Wi-Fi problems, 
password resets, software installation, and printer issues.
Be friendly, clear, and ask clarifying questions when needed."""

conversation_history = []

print("🖥️  IT Helpdesk Agent ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        break
    
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    response = client.chat.completions.create(
        model="llama3.2",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            *conversation_history
        ]
    )
    
    reply = response.choices[0].message.content
    
    conversation_history.append({
        "role": "assistant",
        "content": reply
    })
    
    print(f"\nAgent: {reply}\n")