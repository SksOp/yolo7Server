# Use an official Python runtime as a parent image
FROM python:3.10.9

# Set working directory in container
WORKDIR /app

# Copy the application's code into the container
COPY . /app


# Install any necessary dependencies
# RUN pip install --no-index --find-links=/app/wheelhouse -r requirements.txt
RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt
ENV FLASK_APP=/app/server.py

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["flask", "run"]
