from fastapi import APIRouter, Header
from db.supa import SupaDB
from fastapi.responses import RedirectResponse, HTMLResponse

router = APIRouter(prefix="/api/v1")

supabase = SupaDB()

@router.get("/auth")
async def auth():
    redirect = supabase.google_login()
    url = redirect.url
    return RedirectResponse(url)