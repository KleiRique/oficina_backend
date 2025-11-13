from .llm_client import chat_completion
from ..core.supabase_client import insert_order, insert_message, get_mechanic_shops
from ..whatsapp.waha_client import send_text_to_shop

async def handle_mechanic_message(mechanic_id: str, text: str, message_id=None):
    order = {'mechanic_id': mechanic_id, 'raw_text': text, 'status': 'draft'}
    insert_order(order)

    extract = await chat_completion([
        {"role":"system","content":"Extraia informações estruturadas de pedidos de peças."},
        {"role":"user","content": text}
    ])

    insert_message({'mechanic_id': mechanic_id, 'content': extract, 'source':'agent-extraction'})

    shops = get_mechanic_shops(mechanic_id)
    responses = []
    for shop in shops[:3]:
        shop_response = await send_text_to_shop(shop, extract)
        responses.append(shop_response)

    summary = await chat_completion([
        {"role":"system","content":"Resuma respostas das lojas para o mecânico."},
        {"role":"user","content": str(responses)}
    ])

    insert_message({'mechanic_id': mechanic_id, 'content': summary, 'source':'agent-summary'})
    return summary
