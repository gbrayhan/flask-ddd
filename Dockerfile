# Use a base image of Python
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the port that Flask will use
EXPOSE 5001

# Command to start the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
