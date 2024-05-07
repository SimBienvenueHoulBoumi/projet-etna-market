FROM python:3.11

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./marketplace /marketplace

WORKDIR /marketplace
EXPOSE 8000

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home marketplace

ENV PATH="/venv/bin:$PATH"

USER marketplace