# FastAPI Rate Limiter Microservice

A lightweight backend microservice demonstrating custom middleware implementation in FastAPI. This project enforces a strict time-based rate limit on incoming HTTP requests to prevent API abuse and manage traffic loads.

## Architecture
- **Framework:** FastAPI
- **State Management:** In-memory dictionary tracking client IP timestamps.
- **Middleware:** Intercepts incoming requests before routing, evaluating the time delta against the designated threshold (1.0 seconds).
- **Error Handling:** Returns standard HTTP 429 (Too Many Requests) when limits are exceeded.
