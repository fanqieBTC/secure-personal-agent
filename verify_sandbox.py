import os
import sys
from secure_agent.sandbox.docker_manager import DockerSandbox
from secure_agent.core.agent import SecureAgent

def verify_system():
    print("[Building Sandbox Image]")
    sandbox = DockerSandbox()
    try:
        dockerfile_dir = os.path.join(os.getcwd(), "secure_agent/sandbox")
        sandbox.build_image(dockerfile_dir)
    except Exception as e:
        print(f"Failed to build image: {e}")
        return

    print("\n[Testing Sandbox Isolation]")
    agent = SecureAgent()
    agent.run("read file")
    
    print("\n=== Verification Complete ===")

if __name__ == "__main__":
    # Add current directory to path so imports work
    sys.path.append(os.getcwd())
    verify_system()
