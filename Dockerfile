FROM python:3.11-slim
LABEL anonymous="true"
LABEL name="sfpythonhello"
LABEL description="Python serverless hello world function"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV PYTHONPATH=/app
EXPOSE 3000
ENTRYPOINT ["python", "/app/main.py"]