# CodePilot AI

> AI-powered multi-agent code review platform for GitHub Pull Requests.

CodePilot AI is an intelligent GitHub Pull Request review platform that uses a **planner-driven multi-agent AI architecture** to analyze code changes, identify potential issues, assess risk, and provide actionable recommendations to developers.

Instead of relying on a single AI agent to review an entire Pull Request, CodePilot uses specialized agents for different review responsibilities such as **bug detection, security, performance, and engineering best practices**.

The system fetches Pull Requests directly from GitHub, analyzes changed files and diffs, intelligently routes review tasks to specialized AI agents, aggregates duplicate findings, evaluates the overall risk, generates an executive summary, and presents everything through an interactive React dashboard.

---

## 🚀 Why CodePilot AI?

Code reviews often produce a large number of individual comments without providing a clear understanding of the overall Pull Request.

CodePilot focuses on answering three important questions:

> **What changed?**

> **What problems should I care about?**

> **Can this Pull Request be merged?**

The complete workflow is:

```text
Understand the PR
       ↓
Plan the Review
       ↓
Analyze with Specialized AI Agents
       ↓
Aggregate Findings
       ↓
Evaluate Risk
       ↓
Generate Recommendation
       ↓
Generate Executive Summary
       ↓
Human Review / Approval