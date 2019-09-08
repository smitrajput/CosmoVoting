# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
VOLUME election
WORKDIR /election

# Copy the current directory contents into the container at /app
#COPY . /election
ADD requirements.txt .
# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["python3", "-u","vote/manage.py", "runserver", "0.0.0.0:8000"]
