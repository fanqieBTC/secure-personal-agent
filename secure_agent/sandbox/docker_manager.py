import docker
import tempfile
import os
import tarfile
import io
from typing import Tuple, Optional

class DockerSandbox:
    def __init__(self, image_name: str = "secure-agent-sandbox"):
        self.client = docker.from_env()
        self.image_name = image_name
        self.container = None

    def build_image(self, dockerfile_path: str):
        """Builds the sandbox image from the Dockerfile."""
        print(f"Building image {self.image_name}...")
        self.client.images.build(path=dockerfile_path, tag=self.image_name, rm=True)
        print("Build complete.")

    def run_python_code(self, code: str, timeout: int = 30) -> Tuple[str, str]:
        """
        Runs Python code inside a fresh container.
        Returns (stdout, stderr).
        """
        # Create a temporary file for the code
        with tempfile.TemporaryDirectory() as temp_dir:
            script_name = "script.py"
            local_path = os.path.join(temp_dir, script_name)
            with open(local_path, "w") as f:
                f.write(code)

            # Define volumes: map the temp dir to /workspace
            volumes = {
                temp_dir: {'bind': '/workspace', 'mode': 'rw'}
            }

            try:
                container = self.client.containers.run(
                    self.image_name,
                    command=f"python3 {script_name}",
                    volumes=volumes,
                    working_dir="/workspace",
                    network_mode="none",
                    mem_limit="512m",
                    detach=True,
                    user="1000:1000"
                )

                result = container.wait(timeout=timeout)
                stdout = container.logs(stdout=True, stderr=False).decode('utf-8')
                stderr = container.logs(stdout=False, stderr=True).decode('utf-8')
                return stdout, stderr

            except docker.errors.ContainerError as e:
                return "", str(e)
            except Exception as e:
                if 'container' in locals():
                    container.kill()
                return "", str(e)
            finally:
                if 'container' in locals():
                    try:
                        container.remove()
                    except:
                        pass

# Example usage (for testing)
if __name__ == "__main__":
    sandbox = DockerSandbox()
    # sandbox.build_image("./secure_agent/sandbox") # Run this once
    out, err = sandbox.run_python_code("print('Hello from Sandbox!')")
    print(f"STDOUT: {out}")
    print(f"STDERR: {err}")
