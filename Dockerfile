# Use a base image with Python
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your application code into the container
COPY . /app

# Install Streamlit and any other required dependencies directly
RUN pip install streamlit

# Expose the port Streamlit will use
EXPOSE 8080

# Command to run your app
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.enableCORS=false"]