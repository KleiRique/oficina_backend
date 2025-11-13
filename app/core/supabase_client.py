from supabase import create_client
from .config import settings

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_KEY)

def get_mechanic_shops(mechanic_id: str):
    return supabase.table('shops').select('*').eq('mechanic_id', mechanic_id).execute().data

def insert_order(order: dict):
    return supabase.table('pedidos').insert(order).execute()

def insert_message(msg: dict):
    return supabase.table('messages').insert(msg).execute()
