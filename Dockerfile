FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install

COPY . /app

EXPOSE 3000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=3000

CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
