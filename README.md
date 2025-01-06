A simple test harness to demonstrate that python `requests` auto-instrumentation appears to be regenerating the same `Trace ID`.

# Break

Edit `docker-compose.yml` / `source` to expose the following build args:
```
        #broken
        OTEL_VERSION: 0.50b0
        OTEL_VERSION_OTLP: 1.29.0
```

# Fix

Edit `docker-compose.yml` / `source` to expose the following build args:
```
        #works
        # OTEL_VERSION: 0.49b2
        # OTEL_VERSION_OTLP: 1.28.2
```

# Test

`docker compose build`
`docker compose up`

Observe `Trace ID`
