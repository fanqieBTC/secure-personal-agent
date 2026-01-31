FROM python:3.9-slim

# Create a non-root user to restrict permissions
RUN useradd -m -u 1000 agentuser

# Set working directory to the safe workspace
WORKDIR /workspace

# Switch to non-root user
USER agentuser

# Prevent python from writing pyc files to avoid clutter
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python3"]
