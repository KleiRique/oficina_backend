from fastapi import APIRouter, Request
from ..ai.agent import handle_mechanic_message

router = APIRouter()

@router.post("/webhook/waha")
async def whatsapp_webhook(req: Request):
    data = await req.json()
    mechanic_id = data.get("from")
    text = data.get("body")
    summary = await handle_mechanic_message(mechanic_id, text)
    return {"ok": True}
