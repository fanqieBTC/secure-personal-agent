# Secure Personal Agent - Design & Implementation Plan

## Goal
To design and implement a personal AI assistant similar to Clawdbot but with a "Security First" architecture. The goal is to provide helpful automation while preventing Prompt Injection, accidental data loss, and unauthorized system access.

## Core Philosophy: "Zero Trust" Agent
Unlike Clawdbot, which often runs with full user permissions, this agent will assume:
1.  **Input is Untrusted**: Any data from the web or emails is treated as potentially adversarial (Prompt Injection).
2.  **Tools are Sandboxed**: The agent cannot directly execute shell commands on the host machine.
3.  **Human is the Gatekeeper**: Critical actions (spending money, sending emails, deleting files) require explicit confirmation.

---

## User Review Required
> [!IMPORTANT]
> **Architecture Decision**: We will use **Docker** to sandbox the execution environment. This requires Docker to be installed on the host machine.
>
> **Model Choice**: We will default to a robust model (e.g., Claude 3.5 Sonnet or GPT-4o) for the "Brain", as smaller local models may be more susceptible to social engineering/jailbreaks.

---

## Proposed Architecture

### 1. The "Brain" (Core Agent)
- **Role**: Reasoning, planning, and deciding which tools to use.
- **Safety**:
    - **System Prompt Hardening**: Instructions explicitly forbidding revealing internal state or overriding safety protocols.
    - **Separation of Concerns**: The "Reader" agent (for parsing untrusted content) is separate from the "Executor" agent.

### 2. The "Sandbox" (Tool Execution Environment)
- **Role**: Where the actual work happens.
- **Technology**: Docker Container.
- **Constraint**: The agent generates code (Python/Shell) which is executed *inside* an ephemeral Docker container. It has NO access to the host filesystem unless a specific folder is mounted as a volume.
- **FileSystem**:
    - `/workspace`: A safe, isolated directory for the agent to work in.
    - Host files are *copied* in/out only via explicit user permission, not mounted directly if possible.

### 3. The "Gatekeeper" (Permission Manager)
- **Role**: Intercepts tool calls before execution.
- **Levels**:
    - **Safe (Auto-Approve)**: Searching documentation, reading public web pages (via safe browser), analyzing provided text.
    - **Sensitive (Notify)**: Reading personal files, browsing new URLs.
    - **Critical (Require Approval)**: Writing files, sending emails/messages, executing shell commands, API calls that mutate state.

---

## Proposed Changes / File Structure

### Project Structure `secure_agent/`
#### [NEW] `core/`
- `agent.py`: Main LangGraph/LangChain logic.
- `security.py`: Permission logic and rigorous input validation.

#### [NEW] `sandbox/`
- `docker_manager.py`: Manages the lifecycle of the execution container.
- `Dockerfile`: minimal secure image (e.g., based on Alpine or Slim Python).

#### [NEW] `interfaces/`
- `cli.py`: A simple command-line interface for interaction.
- `web_ui/`: (Optional) A local web dashboard.

#### [NEW] `config/`
- `monitoring.yaml`: Whitelist of allowed domains/tools.
- `permissions.yaml`: User-defined policy (e.g., "Always allow reading ./notes").

## Verification Plan

### Automated Tests
- **Jailbreak Suites**: Run common prompt injection attacks against the agent to see if it leaks secrets or bypasses the sandbox.
- **Sandbox Escape Tests**: Attempt to read `/etc/shadow` or access host network from within the generated tool code.

### Manual Verification
- **"The Malicious Email" Scenario**: Feed the agent a text mimicking a prompt-injection email and verify it does NOT execute the payload.
- **Confirmation Flow**: Verify that trying to "delete a file" triggers a user confirmation prompt.
