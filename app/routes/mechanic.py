from fastapi import APIRouter
from pydantic import BaseModel
from ..ai.agent import handle_mechanic_message

router = APIRouter(prefix="/api/mechanic")

class NewOrder(BaseModel):
    mechanic_id: str
    text: str

@router.post("/orders")
async def create(order: NewOrder):
    summary = await handle_mechanic_message(order.mechanic_id, order.text)
    return {"summary": summary}
