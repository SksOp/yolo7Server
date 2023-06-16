# Use an official Python runtime as a parent image
FROM python:3.10.9

# Set working directory in container
WORKDIR /app

# Install required packages
RUN apt-get update && apt-get install -y libgl1-mesa-glx

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . /app

# RUN python -m venv venv
# # RUN /bin/bash -c "source venv/bin/activate"
# RUN pip install -r /app/requirements.txt

#install from wheel house just for local testing
# RUN pip install --no-index --find-links=/app/wheelhouse -r /app/requirements.txt
# RUN pip install gunicorn

# Make port 5000 available to the world outside this container
EXPOSE 5000

ENV FLASK_APP=/app/app.py

# Run gunicorn when the container launches
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
# gunicorn -b 0.0.0.0:5000 app:app
