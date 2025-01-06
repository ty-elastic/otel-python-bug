from flask import Flask
import logging
import requests
import time
from threading import Thread

from opentelemetry import trace

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.route('/health')
def health():
    return f"KERNEL OK"

@app.post('/request')
def request():
    return f"OK"

tracer = trace.get_tracer("source")

def generate_request(*, request_id):
    try:
        response = requests.post(f"http://127.0.0.1:5000/request")
        response.raise_for_status()
    except Exception as inst:
        print(inst)

@tracer.start_as_current_span("manual_span")
def manual_span():
    return "OK"

def generate_requests():
    request_id = 0
    while True:
        request_id = request_id+1
        generate_request(request_id=request_id)
        time.sleep(1)
        manual_span()
        time.sleep(1)

Thread(target=generate_requests, daemon=False).start()
