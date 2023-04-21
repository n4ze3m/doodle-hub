import supabase
import os                                                                                                               


class SupaDB:
    def __init__(self):
        self.supabase_url = os.environ.get('SUPABASE_URL')
        self.supabase_key = os.environ.get('SUPABASE_KEY')
        self.supabase = supabase.create_client(self.supabase_url, self.supabase_key)

    def google_login(self):
        return self.supabase.auth.sign_in_with_oauth({
            'provider': 'google',
            'options': {
            'redirect_to': 'http://localhost:5000/v1/auth/google/callback'
            }
        })

