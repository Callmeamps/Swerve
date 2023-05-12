import os
from supabase import create_client, Client
import datetime
from client_user import Client as c_user

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class Subscribe:
    def __init__(self, client, subscription_date=datetime.date.today()):
        self.subscription_date = subscription_date

        if isinstance(client, c_user):
            self.client = client
        else:
            raise ValueError("Invalid Client...")

    def register_subscription(self, email, password):
        res = supabase.auth.sign_up({
        "email": email,
        "password": password,
        })
