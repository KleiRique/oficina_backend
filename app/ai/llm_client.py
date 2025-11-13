import openai
from ..core.config import settings

openai.api_key = settings.OPENAI_API_KEY

async def chat_completion(messages: list, model="gpt-4o-mini"):
    resp = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=800
    )
    return resp.choices[0].message['content']
