# AI Agent + WordPress Demo

This is a small end-2-end demo showing how a simple AI agent can be integrated with a WordPress front end using a custom plugin and a FastAPI backend.
The goal of this project is not design or UI polish.  
It focuses on backend logic,authentication,AI workflow integration,and how WordPress can communicate with an external AI service in a clean,production oriented way.


## What this project does

- Users can register and log in via a backend API
- Authentication is handled using JWT
- Authenticated users can submit a question
- A simple LangChain-powered agent summarizes the question
- The summarized output is returned to the UI
- The summary is also “sent” to an email endpoint (simulated via logging)
- A WordPress plugin acts as the frontend and communicates with the backend via REST


## Tech stack

**Backend**
- Python
- FastAPI
- JWT authentication
- LangChain (simple summarization chain)
- OpenAI API
- Uvicorn

**Frontend**
- WordPress
- Custom WordPress plugin (PHP)
- REST API calls to the backend

## Project structure

ai-agent-wp-demo/
├── backend/
│ └── main.py
├── frontend-wordpress/
│ └── wp-ai-agent/
│ └── wp-ai-agent.php
├── README.md
└── .gitignore

## Final notes

This demo is intentionally simple but production-minded.
The focus is on ownership of the full flow: authentication,AI logic,integrations,and clean boundaries between systems.

It’s designed to be extended into more complex setups such as voice agents, multiagent orchestration,real email services, or production monitoring.





