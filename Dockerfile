FROM python:3.10-slim
# Set the working directory
WORKDIR /user/src/app
# Copy the requirements file into the container
COPY requirements.txt .
# Install the dependencies

# Copy the rest of the application code into the container
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
# Expose the port the app runs on
EXPOSE 8501
# Command to run the application
CMD ["streamlit", "run", "app.py", "--server.port=8501"]
