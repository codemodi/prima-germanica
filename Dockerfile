
FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv install --system

COPY ./ /app

ENV PORT 8080

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 primagermanica.wsgi:application

