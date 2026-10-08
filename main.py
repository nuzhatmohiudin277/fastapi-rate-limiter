from fastapi import FastAPI, Request, HTTPException
import time
import uvicorn

app = FastAPI(title="Rate Limiter Microservice")

# In-memory store for tracking IP timestamps
clients = {}

@app.middleware("http")
async def rate_limit(request: Request, call_next):
    ip = request.client.host
    now = time.time()
    
    # Check if IP has made a request within the last 1.0 seconds
    if ip in clients and now - clients[ip] < 1.0:
        raise HTTPException(status_code=429, detail="Too Many Requests: Please slow down.")
    
    # Update the timestamp for the IP
    clients[ip] = now
    
    # Process the request
    response = await call_next(request)
    return response

@app.get("/")
def read_root():
    return {
        "status": "healthy",
        "message": "Rate limiter is active. Refresh quickly to trigger a 429 error."
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
