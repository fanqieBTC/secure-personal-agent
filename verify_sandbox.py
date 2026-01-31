import os
import sys
from secure_agent.sandbox.docker_manager import DockerSandbox
from secure_agent.core.agent import SecureAgent

def verify_system():
    print("=== Step 1: Building Sandbox Image ===")
    sandbox = DockerSandbox()
    try:
        # Point to the directory containing the Dockerfile
        # Assuming we are running this from the root of the project
        dockerfile_dir = os.path.join(os.getcwd(), "secure_agent/sandbox")
        sandbox.build_image(dockerfile_dir)
        print("Image built successfully.")
    except Exception as e:
        print(f"Failed to build image: {e}")
        return

    print("\n=== Step 2: Testing Agent Execution (Safe) ===")
    agent = SecureAgent()
    agent.run("print hello")

    print("\n=== Step 3: Testing Sandbox Isolation ===")
    # Attempting to list root directory - should show container's root, not host's
    agent.run("read file")
    
    print("\n=== Verification Complete ===")

if __name__ == "__main__":
    # Add current directory to path so imports work
    sys.path.append(os.getcwd())
    verify_system()
