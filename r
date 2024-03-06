curl -X POST http://your-flask-app-url:5000/ \
  -H "Content-Type: application/json" \
  -d '{
    "alerts": [
      {
        "labels": {
          "alertname": "HighErrorRate",
          "severity": "critical"
        },
        "annotations": {
          "summary": "High error rate detected",
          "description": "The API server is experiencing a high error rate. Investigate immediately."
        }
      }
    ]
  }'
