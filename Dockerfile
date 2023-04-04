FROM python:3.11-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD . /code
RUN apk update && \
    apk add --no-cache gcc musl-dev postgresql-libs postgresql-dev glib-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip cache purge && \
    apk del postgresql-dev gcc musl-dev

EXPOSE 8001
