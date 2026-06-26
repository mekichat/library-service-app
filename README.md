# 📚 Library Service App

A production-grade, cloud-native microservices system for managing books and orders in a distributed library platform. The system is designed using scalable microservice architecture, containerization, and Kubernetes orchestration.

---

## 📌 Project Overview

The Library Service App is composed of three main components:

- 🌐 Frontend (React)
- 📘 Book API (FastAPI + MySQL)
- 📦 Order API (Go + PostgreSQL)

Each service is independently deployable and communicates via REST APIs. The system is designed for scalability, maintainability, and cloud-native deployment.

---

## 🏗️ System Architecture (High-Level)

```text
                    ┌────────────────────┐
                    │   React Frontend   │
                    └─────────┬──────────┘
                              │ REST API Calls
          ┌───────────────────┼───────────────────┐
          │                                       │
┌────────────────────┐                ┌────────────────────┐
│    Book API        │                │    Order API       │
│ FastAPI + MySQL    │                │ Go + PostgreSQL    │
└─────────┬──────────┘                └─────────┬──────────┘
          │                                     │
          ▼                                     ▼
     ┌──────────┐                         ┌────────────┐
     │  MySQL   │                         │ PostgreSQL │
     └──────────┘                         └────────────┘

📁 Project Structure

library-service-app/
│
├── frontend/
│   ├── package.json
│   ├── public/
│   └── src/
│
├── book-api/
│   ├── app/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
│
├── order-api/
│   ├── handlers/
│   ├── models/
│   ├── main.go
│   └── Dockerfile
│
└── k8s/
    ├── mysql/
    │   ├── mysql-deployment.yaml
    │   ├── mysql-service.yaml
    │
    ├── postgres/
    │   ├── postgres-deployment.yaml
    │   ├── postgres-service.yaml
    │
    ├── book-api/
    │   ├── deployment.yaml
    │   ├── service.yaml
    │
    ├── order-api/
    │   ├── deployment.yaml
    │   ├── service.yaml
    │
    └── frontend/
        ├── deployment.yaml
        ├── service.yaml

☸️ Kubernetes Deployment

The system is fully containerized and deployed using Kubernetes manifests.

📦 Databases
    MySQL (for Book Service)
    PostgreSQL (for Order Service)
📦 Microservices
    Book API deployment + service
    Order API deployment + service
    Frontend deployment + service

📊 UML Diagram (Component Diagram)
+----------------------+
|     Frontend         |
|      React           |
+----------+-----------+
           |
           | REST API
           v
+----------------------+        +----------------------+
|     Book API         |        |     Order API        |
| FastAPI + MySQL      |        | Go + PostgreSQL      |
+----------+-----------+        +----------+-----------+
           |                               |
           v                               v
     +-----------+                  +-------------+
     |   MySQL   |                  | PostgreSQL  |
     +-----------+                  +-------------+