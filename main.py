from fastapi import FastAPI, HTTPException
import socket

app = FastAPI()

@app.get("/resolve/{domain}")
async def resolve_domain(domain: str):
    try:
        ip_address = socket.gethostbyname(domain) 
        return {"domain": domain, "ip_address": ip_address}
    except socket.gaierror:
        raise HTTPException(status_code=400, detail="Invalid domain name")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
