import httpx
from ..core.config import settings

async def send_text_to_shop(shop: dict, content: str):
    url = f"{settings.WAHA_API_BASE}/sendMessage"
    payload = {'to': shop['phone'], 'type': 'text', 'text': {'body': content}}
    headers = {'Authorization': f'Bearer {settings.WAHA_API_KEY}'}
    async with httpx.AsyncClient() as c:
        r = await c.post(url, json=payload, headers=headers)
        return r.json()
