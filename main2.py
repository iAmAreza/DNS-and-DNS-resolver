from fastapi import FastAPI, HTTPException
import dns.resolver

app = FastAPI()

@app.get("/resolve/{domain}")
async def resolve_domain(domain: str):
    try:
        result = dns.resolver.resolve(domain, "A")  # "A" record (IPv4)
        ip_addresses = [ip.to_text() for ip in result]
        return {"domain": domain, "ip_addresses": ip_addresses}
    except dns.resolver.NXDOMAIN:
        raise HTTPException(status_code=400, detail="Domain does not exist")
    except dns.resolver.Timeout:
        raise HTTPException(status_code=504, detail="DNS query timed out")
    except dns.resolver.NoAnswer:
        raise HTTPException(status_code=500, detail="No valid DNS response")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
