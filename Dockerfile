FROM python:3.11.0-slim-buster


WORKDIR /app


COPY requirements.txt .

COPY . /app


RUN pip install -r requirements.txt





EXPOSE 5001

# Start the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5001"]

