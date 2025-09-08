from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world", "schema": "builds"}

@app.get("/ping")
def ping():
    return {"ok": True}
