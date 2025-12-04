FROM python:3.10-slim

# Workdir inside container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Flask port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]

