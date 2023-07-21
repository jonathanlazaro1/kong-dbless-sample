FROM python:3.11-slim-bullseye

# Add demo app
WORKDIR /app
COPY . .

RUN pip install pip-tools
RUN python -m piptools sync requirements.txt

EXPOSE 5000

CMD ["uvicorn", "main:app", "--workers", "4", "--host", "0.0.0.0", "--port", "5000"]