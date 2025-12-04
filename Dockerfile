# --------------------------------------------------------------
#  Docker image for the freeproxy Flask API
# --------------------------------------------------------------
FROM python:3.11-slim

# Install system dependencies (curl, ca‑certificates, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc \
        libffi-dev \
        libssl-dev \
        && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy only the Python source (avoid copying __pycache__ etc.)
COPY freeproxy/ ./freeproxy/
COPY requirements.txt .

# Install Python dependencies (including Flask & redis)
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers and dependencies
# We set the PLAYWRIGHT_BROWSERS_PATH environment variable so browsers are installed
# in a predictable location that we can persist or cache.
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# Expose the Flask port
EXPOSE 5000

# Default command – run the API
CMD ["python", "-m", "freeproxy.api"]
