# Dockerfile
FROM python:3.10.12-slim

# Set working directory
WORKDIR /app

# Copy the app code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Expose Streamlit default port
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
