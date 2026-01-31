from secure_agent.sandbox.docker_manager import DockerSandbox
import sys
import os

class SecureAgent:
    def __init__(self):
        self.sandbox = DockerSandbox()
        # In a real app, we'd initialize the LLM here.
    
    def run(self, command: str):
        print(f"Agent received: {command}")
        
        # Simplified logic for PoC:
        # If the command asks to "calculate" or "print", generating python code.
        # This mocks the LLM part for the PoC to test infrastructure first.
        
        if "print hello" in command.lower():
            code = "print('Hello from the Secure Sandbox!')"
        elif "calculate" in command.lower():
            code = "print(12345 * 67890)"
        elif "read file" in command.lower():
            # Attempting to read a sensitive file to test isolation
            code = "import os; print(os.listdir('/'))" # Should only show container fs
        else:
            print("I didn't understand that command (Mock LLM limitation).")
            return

        print(f"Generated Code to Run:\n{code}")
        
        # Permission Check (Mock)
        # For this non-interactive run, we assume "y" if not specified, 
        # but in production, this would wait for user input.
        print("Local Agent: Requesting permission to run this code in sandbox...")
        print(">> Permission GRANTED (Simulated)")

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
    # We assume image is built by an external setup script or manual step
    
    if len(sys.argv) > 1:
        agent.run(sys.argv[1])
    else:
        print("Please provide a command string.")
