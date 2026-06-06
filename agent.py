from openai import OpenAI
from rag import search_docs

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

conversation_history = []

print("🖥️  IT Helpdesk Agent ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        break

    # Step 1: Search the IT docs for relevant info
    relevant_docs = search_docs(user_input)
    
    # Step 2: Build a system prompt that includes the relevant docs
    SYSTEM_PROMPT = f"""You are an IT helpdesk assistant for our company.
Use ONLY the information below to answer the user's question.
If the answer is not in the information below, say you don't know 
and suggest they contact IT at it@company.com.

RELEVANT IT DOCUMENTATION:
{relevant_docs}
"""

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