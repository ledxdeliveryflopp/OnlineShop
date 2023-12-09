FROM python:3.10

COPY . .
RUN pip install --no-cache-dir poetry==1.7.1 && poetry config virtualenvs.create false && poetry update


