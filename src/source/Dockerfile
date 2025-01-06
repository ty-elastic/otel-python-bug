FROM python:3.12.6-slim-bookworm

ARG OTEL_VERSION
ARG OTEL_VERSION_OTLP

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /python-docker

COPY requirements.txt .
RUN pip3 install --root-user-action=ignore -r requirements.txt

# add OTel libs
RUN pip3 install --root-user-action=ignore opentelemetry-distro==${OTEL_VERSION} opentelemetry-instrumentation==${OTEL_VERSION} opentelemetry-exporter-otlp==${OTEL_VERSION_OTLP}

COPY app.py .

# add OTel auto-instrumentation libs matching installed Python modules
RUN opentelemetry-bootstrap -a install

ENV PYTHONUNBUFFERED=1
ENV OTEL_SERVICE_NAME="source"

CMD [ "opentelemetry-instrument", "flask", "run"]