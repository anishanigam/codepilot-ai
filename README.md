# CodePilot AI - AI Code Review Agent

An intelligent GitHub Pull Request review platform built with **React**, **FastAPI**, **LangChain**, and **Groq**.

Connect your GitHub account, select a repository and Pull Request, and let CodePilot analyze the changed code using multiple specialized AI agents. It identifies potential bugs, security issues, performance problems, and best-practice violations, then combines everything into a structured review dashboard.

---

## 🎯 Features

- 🔐 **GitHub OAuth** — Securely connect and access your GitHub repositories
- 📂 **Repository Explorer** — Browse repositories available to your GitHub account
- 🔀 **Pull Request Analysis** — View PR details, changed files, and code diffs
- 🤖 **Multi-Agent AI Review** — Multiple specialized agents analyze different aspects of the code
- 🧠 **AI Planner** — Intelligently decides which review agents should analyze each code chunk
- 🐞 **Bug Detection** — Identifies potential bugs and incorrect behavior
- 🔒 **Security Analysis** — Detects potential security vulnerabilities and unsafe practices
- ⚡ **Performance Review** — Finds inefficient implementations and performance issues
- 📖 **Best Practices Review** — Checks maintainability, readability, and engineering practices
- 🔄 **Agent Orchestration** — Coordinates multiple AI review tasks
- 🧩 **Finding Aggregation** — Combines duplicate findings reported by multiple agents
- 📊 **Risk Assessment** — Generates an overall LOW, MEDIUM, or HIGH risk level
- 🚦 **Merge Recommendation** — Recommends APPROVE, MERGE_AFTER_FIXES, or REQUEST_CHANGES
- 📝 **AI Executive Summary** — Generates a concise overview of the Pull Request
- 📈 **Review Dashboard** — Displays statistics, findings, risk, modules, and recommendations
- 👤 **Human-in-the-Loop** — AI-generated review results can be reviewed and approved by the user

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React.js + JavaScript |
| Build Tool | Vite |
| Styling | Tailwind CSS |
| Routing | React Router |
| Data Fetching | TanStack React Query |
| HTTP Client | Axios |
| Backend | Python + FastAPI |
| Server | Uvicorn |
| AI Framework | LangChain |
| LLM Provider | Groq |
| AI Model | Llama 3.3 70B |
| GitHub Integration | GitHub OAuth + REST API |
| HTTP Client (Backend) | HTTPX |

---

## 📁 Project Structure

```text
codepilot-ai/

├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── review/
│   │   │   └── ...
│   │   │
│   │   ├── pages/
│   │   │   ├── PullRequestDetails.jsx
│   │   │   ├── Review.jsx
│   │   │   └── ...
│   │   │
│   │   ├── services/
│   │   │   ├── api.js
│   │   │   ├── reviewService.js
│   │   │   └── ...
│   │   │
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   │   ├── agents/
│   │   │   ├── planner/
│   │   │   ├── orchestrator/
│   │   │   ├── preprocessor/
│   │   │   ├── postprocessor/
│   │   │   ├── summary/
│   │   │   ├── llm.py
│   │   │   ├── models.py
│   │   │   └── review_service.py
│   │   │
│   │   ├── github/
│   │   │   ├── github_client.py
│   │   │   └── github_service.py
│   │   │
│   │   ├── routers/
│   │   ├── core/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
└── README.md

```
---

## AI Review Architecture

> CodePilot uses a planner-driven multi-agent architecture.
``` bash
GitHub Pull Request
        ↓
Fetch Changed Files
        ↓
Preprocessor
        ↓
Split Code into Reviewable Chunks
        ↓
AI Planner
        ↓
┌───────────────┬───────────────┬──────────────────┐
↓               ↓               ↓                  ↓
Bug Agent   Security Agent  Performance Agent  Best Practices
└───────────────┴───────────────┴──────────────────┘
                        ↓
                 Orchestrator
                        ↓
               Finding Aggregator
                        ↓
              Recommendation Engine
                        ↓
                 Summary Agent
                        ↓
                Review Dashboard
                        ↓
                 Human Approval
```
---
## AI Decision
>CodePilot generates an overall risk level:
```bash
LOW
MEDIUM
HIGH
```

and a merge recommendation:
```bash
APPROVE
MERGE_AFTER_FIXES
REQUEST_CHANGES
```

Example:
```bash
Risk Level
MEDIUM

Recommendation
MERGE AFTER FIXES

Reason
High-severity findings should be addressed before merging.
```
---
## Environment Variables

>Create a .env file inside the backend directory
```bash
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret

GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.3-70b-versatile
```

---
## 🚀 Run Locally
1. Clone the repository
   ```bash
   git clone https://github.com/<anishanigam>/codepilot-ai.git
   cd codepilot-ai
   ```
2. Setup Backend
   ```bash
   cd backend
   ```
   Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
        
   Activate it on Windows:
   ```bash
   .venv\Scripts\activate
   ```
        
   For macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```
        
   Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Create your .env file and add the required credentials.
3. Start Backend

   Make sure you are inside the backend directory:
   ```bash
   uvicorn app.main:app --reload
   ```
        
   Backend will run at:
   ```bash
   http://localhost:8000
   ```
        
   FastAPI documentation:
   ```bash
   http://localhost:8000/docs
   ```

4. Setup Frontend

   Open another terminal:
   ```bash
   cd frontend
   ```

   Install dependencies:
   ```bash
   npm install
   ```
   Start the development server:
   ```bash
   npm run dev
   ```

   The frontend will normally be available at:
   ```bash
   http://localhost:5173
   ```

## 🔒 Security

CodePilot uses GitHub OAuth for authentication and does not require users to provide their GitHub password.

Sensitive credentials are stored through environment variables.

Never commit:
```bash
.env
GitHub Client Secret
GitHub Access Tokens
Groq API Keys
JWT Secrets
Database Credentials
```

Make sure .env is included in .gitignore.



