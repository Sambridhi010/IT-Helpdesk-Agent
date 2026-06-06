🖥️ IT Helpdesk AI Agent
A locally-running AI helpdesk agent built with Python and Ollama. No API costs, no token limits, runs 100% on your own PC.
📌 Project Status

Day 1 of 5 — Core agent loop working. RAG, tool use, and escalation coming in the next days.


🚀 What it does (so far)

Answers common IT questions (Wi-Fi, passwords, printers, software)
Remembers the full conversation history
Asks clarifying questions like a real helpdesk person
Runs locally using Ollama + Llama 3.2 — completely free


🛠️ Tech Stack
ToolPurposePython 3.12Core languageOllamaRun AI model locallyLlama 3.2The AI modelopenai (package)API client (pointed at Ollama)

⚙️ Setup & Installation
1. Install Ollama
Download from ollama.com and install it.
Then pull the model:
bashollama pull llama3.2
2. Clone this repo
bashgit clone https://github.com/your-username/it-helpdesk-agent.git
cd it-helpdesk-agent
3. Create virtual environment
bashpython -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
4. Install dependencies
bashpip install openai
5. Run the agent
bashpython agent.py

💬 Example conversation
You: My laptop won't connect to the company Wi-Fi

Agent: I'm happy to help you get connected. Can you tell me 
more about what's happening? Are you able to see the company 
Wi-Fi network in your list of available networks?

🗺️ Roadmap

 Day 1 — Core agent loop + basic Q&A
 Day 2 — RAG: connect internal IT documentation
 Day 3 — Tools: password reset, ticket creation, system status
 Day 4 — Escalation logic + conversation memory
 Day 5 — Streamlit UI + full deployment


📁 Project Structure
it-helpdesk-agent/
│
├── agent.py        # Main agent code
├── README.md       # This file
└── venv/           # Virtual environment (not committed)

🙋 Author
Built as a 5-day learning project to understand AI agents from scratch.
