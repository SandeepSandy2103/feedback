# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy source files
COPY app.py .

# Install dependencies
RUN pip install streamlit

# Expose Streamlit port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
