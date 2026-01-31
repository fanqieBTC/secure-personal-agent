# Secure Personal Agent - Walkthrough

I have implemented a **Proof of Concept (PoC)** for a secure, sandboxed personal AI assistant. This system addresses the major security risks found in tools like Clawdbot by isolating code execution.

## 🛡️ Key Security Features

1.  **Strict Sandboxing**:
    - All AI-generated code runs inside a **Docker container** (`secure-agent-sandbox`).
    - The container has **no network access** (default) and **no access to your host files** (unless explicitly granted).
2.  **Permission Gating**:
    - The agent simulates a "User Confirmation" step before executing any code.
    - In the PoC code, you will see explicit checks: `Requesting permission to run...`.
3.  **Minimal Base Image**:
    - Uses a stripped-down `python:3.9-slim` image to reduce attack surface.
    - Non-root user execution prevents privilege escalation.

## 📂 Project Structure

- **`secure_agent/core/agent.py`**: The main brain. It mocks an LLM to generate code based on your commands ("print hello", "calculate").
- **`secure_agent/sandbox/docker_manager.py`**: The security enforcement layer. It manages the Docker container lifecycle and executes code safely.
- **`verify_sandbox.py`**: A script to verify that the sandbox works and is isolated.

## 🚀 How to Run

> [!IMPORTANT]
> **Prerequisite**: You must have **Docker Desktop** installed and **running**.

1.  **Install Dependencies**:
    ```bash
    python3 -m pip install -r requirements.txt
    ```
2.  **Run the Verification**:
    ```bash
    python3 verify_sandbox.py
    ```

### ✅ Verification Results (Success)
We successfully verified the system on your machine:
- **Build**: The Docker image `secure-agent-sandbox` was built successfully.
- **Execution**: The agent ran Python code inside the container.
- **Isolation Confirmed**: When asked to `read file`, the agent listed the *container's* file system (Linux) instead of your Mac's file system.

```text
=== Step 3: Testing Sandbox Isolation ===
Agent received: read file
...
Result:
['dev', 'mnt', 'var', 'sys', 'tmp', ... 'workspace']
```
*Note: The absence of 'Users' or 'Applications' directories confirms the agent cannot see your files.*

## 📦 GitHub Repository
The project is now hosted at: [secure-personal-agent](https://github.com/linxiping2/secure-personal-agent)

## 🔮 Next Steps
To turn this into a full "Clawdbot replacement":
1.  **Connect an LLM**: Replace the mock logic in `agent.py` with `LangChain` + `Anthropic/OpenAI` API.
2.  **Expand Tools**: Add safe tools for "Clicking Browsers" (using a headless browser in the container) or "Reading Email".
3.  **UI**: Build a simple Streamlit or React frontend.
