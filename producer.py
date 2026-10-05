import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Starting Order Producer Service...")
for i in range(1, 25):
    order = {
        "order_id": 1000 + i,
        "customer_id": f"CUST_{random.randint(100, 999)}",
        "amount": round(random.uniform(250.0, 5000.0), 2),
        "status": "CREATED",
        "timestamp": time.time()
    }
    producer.send('order-events', value=order)
    print(f"[Sent] Event: {order}")
    time.sleep(1)

producer.flush()
