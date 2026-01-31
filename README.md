# Secure Personal Agent 🛡️🤖

**A "Security-First" Personal AI Assistant.**

This project is a Proof of Concept (PoC) for a personal AI agent designed to run locally with strict isolation. It serves as a secure alternative to tools like Clawdbot, focusing on preventing **Prompt Injection** and **Unauthorized System Access** through sandboxing.

## 🚀 Key Features

*   **Docker Sandboxing**: All AI-generated code runs inside an isolated, network-restricted Docker container.
*   **Permission Gating**: Critical actions require explicit user confirmation.
*   **Isolation**: The agent has NO access to your host filesystem unless explicitly granted.
*   **Minimal Attack Surface**: Uses a stripped-down Python image for the execution environment.

## 🛠️ Architecture

*   **`secure_agent/core`**: The "Brain". Handles logic and LLM interaction.
*   **`secure_agent/sandbox`**: The "Jail". Manages the Docker container lifecycle.
*   **`verify_sandbox.py`**: Verification script to prove isolation.

## 📦 Installation

### Prerequisites
*   Python 3.9+
*   **Docker Desktop** (Must be installed and running)

### Setup

1.  Clone the repository:
    ```bash
    git clone https://github.com/linxiping2/secure-personal-agent.git
    cd secure-personal-agent
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 🏁 Usage

### Verify Security (Demo)
Run the verification script to build the sandbox and test isolation:

```bash
python3 verify_sandbox.py
```

**What happens?**
1.  Builds the `secure-agent-sandbox` Docker image.
2.  Runs a safe "Hello World" command.
3.  **Security Test**: Attempts to read the root directory (`/`). You will see the *container's* file system, confirming the agent cannot access your Mac's files.

## ⚠️ Disclaimer

This is a **Proof of Concept**. While it mimics a secure architecture:
*   Real LLM integration (OpenAI/Anthropic) is currently mocked in `agent.py`.
*   It is not yet production-ready software.

## 🤝 Contributing

Pull requests are welcome! Please ensure any new tools added are properly sandboxed.

## 📜 License

MIT
