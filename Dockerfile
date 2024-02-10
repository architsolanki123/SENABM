# Use the official python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install all the required python dependencies
RUN pip install -r requirements.txt

# Run the python script
CMD ["python", "SleepDetection.py"]