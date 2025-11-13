from fastapi import FastAPI
from .routes.mechanic import router as mechanic_router
from .routes.webhook import router as webhook_router

app = FastAPI(title="Oficina Inteligente Backend")

app.include_router(mechanic_router)
app.include_router(webhook_router)

@app.get('/health')
async def health():
    return {"status": "ok"}
