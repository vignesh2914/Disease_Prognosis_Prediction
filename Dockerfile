# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /stream

# Copy the current directory contents into the container at /stream
COPY . /stream

# Upgrade pip
RUN pip install --upgrade pip

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8501

# Command to run when container starts
CMD echo "🚀 Access the app at http://localhost:8501 (replace '0.0.0.0' with 'localhost' if accessing directly on your machine)" && \
    streamlit run stream.py --server.port=8501 --server.address=0.0.0.0
    