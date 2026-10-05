# Distributed Order Processing Pipeline

A distributed, event-driven microservices architecture built with **Apache Kafka** and **Docker** for real-time asynchronous transaction processing.

## Tech Stack
- **Message Broker:** Apache Kafka & Zookeeper (Confluent Platform)
- **Containerization:** Docker Compose
- **Service Layer:** Python (kafka-python)

## System Overview
- **Producer Service (`producer.py`):** Emits streaming e-commerce order transactions to the `order-events` Kafka topic.
- **Consumer Service (`consumer.py`):** Asynchronously ingests, validates, and processes incoming orders from the topic partition.
- **Orchestration (`docker-compose.yml`):** Multi-container setup isolating Kafka broker instances and coordination layers.
