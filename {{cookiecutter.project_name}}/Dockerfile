# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    gcc \
    g++ \
    make \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
# We separate this from the source code to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set up Jupyter configuration
RUN jupyter notebook --generate-config
RUN echo "c.NotebookApp.ip = '0.0.0.0'" >> ~/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.allow_root = True" >> ~/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.open_browser = False" >> ~/.jupyter/jupyter_notebook_config.py

# Create necessary directories
RUN mkdir -p /workspace/notebooks /workspace/scripts /workspace/data /workspace/models

# Set environment variables
ENV PYTHONPATH=/workspace
ENV MLFLOW_TRACKING_URI=http://mlflow:5000

# The container will run Jupyter by default
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]