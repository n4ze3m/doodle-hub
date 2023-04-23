from fastapi import APIRouter, Header, Request, Response
from db.supa import SupaDB
from fastapi.responses import RedirectResponse, HTMLResponse

router = APIRouter(prefix="/api/v1")

supabase = SupaDB()

@router.get("/auth", tags=["auth"])
async def auth():
    redirect = supabase.google_login()
    url = redirect.url
    return RedirectResponse(url)



@router.get("/logout", tags=["auth"])
async def logout():
    return RedirectResponse(url="/login", status_code=302,headers={"Set-Cookie": "supabase_access_token=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/"})