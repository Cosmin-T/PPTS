FROM python:3.11

# Use a base image that includes necessary libraries for Chrome
FROM selenium/standalone-chrome:latest

# Set the working directory in the container
WORKDIR /app

# Switch to root user for installations
USER root

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Switch back to non-root user
USER seluser

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
ENV ENV_NAME env

# Run Homepage.py when the container launches
CMD ["streamlit", "run", "--server.headless", "true", "Homepage.py"]
