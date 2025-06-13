# Use an official Python image as the base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container (including secret.txt)
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application's port (5001)
EXPOSE 5001

# Command to run the application
CMD ["python", "app.py"]
