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

# Reminder: Access the app on localhost:8501 
# let you build the image in this port below but after inster of 0s add local host and access my project cheers!!!!!!!!!!!
CMD streamlit run stream.py --server.port=8501 --server.address=0.0.0.0
