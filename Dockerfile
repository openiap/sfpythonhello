FROM python:latest
LABEL anonymous="true"
LABEL name="sfpythonhello"
LABEL description="Python serverless hello world function"
COPY . /app
WORKDIR /app
RUN pip install -t . -r requirements.txt
ENV PYTHONPATH=/app
EXPOSE 3000
ENTRYPOINT ["python", "/app/main.py"]