from fastapi import FastAPI

# Vercel Python runtime detects an ASGI app named `app`
app = FastAPI(title="Vercel FastAPI Starter")

@app.get("/")
def root():
    return {"hello": "world", "via": "root /"}

@app.get("/ping")
def ping():
    return {"ok": True}

# Optional additional route to show something else
@app.get("/api-info")
def info():
    return {"app": "fastapi", "runtime": "python3.11 on vercel"}
