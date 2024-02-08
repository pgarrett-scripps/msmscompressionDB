# Use an official Python runtime as a parent image
FROM python:3.11.7

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create a directory to hold the database file
RUN mkdir -p data

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable for the database file path
ENV DB_FILE_PATH=/usr/src/app/data/spectra.db

# Run uvicorn to start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]