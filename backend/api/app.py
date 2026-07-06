from fastapi import FastAPI
from pydantic import BaseModel

from backend.core.orchestrator import Orchestrator


app = FastAPI(title="AI Orchestrator API")

orch = Orchestrator()


# ---------------- REQUEST MODEL ----------------
class ChatRequest(BaseModel):
    input: str


# ---------------- RESPONSE ----------------
@app.post("/chat")
def chat(req: ChatRequest):

    result = orch.run(req.input)

    return {
        "status": "ok",
        "data": result
    }


# ---------------- HEALTH CHECK ----------------
@app.get("/health")
def health():
    return {"status": "running"}

