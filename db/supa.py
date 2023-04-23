import supabase
import os                                                                                                               
import base64
import time
import uuid

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
    

    def get_user(self, access_token):
        try:
            return self.supabase.auth.get_user(access_token)
        except:
            return None
        

    def get_user_info(self, id):
        return self.supabase.from_("User").select("*, Submissions(*)").eq("id", id).execute()
    


    def find_user_by_public_id(self, public_id):
        try:
            return self.supabase.from_("User").select("*").eq("public_id", public_id).execute()
        except:
            return None
    

    def save_submissions(self, base64Img:str, user_id: str):
        base64Img = base64Img.replace("data:image/png;base64,", "")
        img_bytes = base64.b64decode(base64Img)

        timestamp = int(time.time()) * 0.001
        file_name = f"{user_id}/{timestamp}-{uuid.uuid4()}.png"
            
        self.supabase.storage.from_("images").upload(file_name, img_bytes, {
         "content-type": "image/png" 
        })

        url = f"{self.supabase_url}/storage/v1/object/public/images/{file_name}"
        return self.supabase.from_("Submissions").insert(
            {"user_id": user_id, "img": url}
        ).execute()



    def get_user_submissions(self, user_id: str):
        
        return self.supabase.from_("Submissions").select("*").eq("user_id", user_id).order("created_at", ascending=False).execute()