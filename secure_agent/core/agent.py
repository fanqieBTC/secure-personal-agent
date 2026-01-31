from secure_agent.sandbox.docker_manager import DockerSandbox
import sys
import os

class SecureAgent:
    def __init__(self):
        self.sandbox = DockerSandbox()
        self.sandbox = DockerSandbox()
    
    def run(self, command: str):
        print(f"Agent received: {command}")
        

        
        if "print hello" in command.lower():
            code = "print('Hello from the Secure Sandbox!')"
        elif "calculate" in command.lower():
            code = "print(12345 * 67890)"
        elif "read file" in command.lower():
            code = "import os; print(os.listdir('/'))"
        else:
            print("Unknown command.")
            return

        print(f"Generated Code:\n{code}")
        
        # TODO: Implement actual UI prompt
        print("Requesting permission... GRANTED")

        print("Executing in Docker...")
        try:
            stdout, stderr = self.sandbox.run_python_code(code)
            
            if stdout:
                print(f"Result:\n{stdout}")
            if stderr:
                print(f"Error:\n{stderr}")
        except Exception as e:
            print(f"Execution failed: {e}")

if __name__ == "__main__":
    agent = SecureAgent()
    agent = SecureAgent()
    
    if len(sys.argv) > 1:
        agent.run(sys.argv[1])
    else:
        print("Please provide a command string.")
