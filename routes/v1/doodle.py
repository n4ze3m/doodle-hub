from db.supa import SupaDB
from fastapi import APIRouter, HTTPException, Header, Request
from fastapi.responses import RedirectResponse, HTMLResponse

supabase = SupaDB()

router = APIRouter(prefix="/api/v1")


@router.get("/doodles")
async def doodles(request: Request):
    access_token = request.cookies.get("supabase_access_token")

    if access_token is None:
        status_code = 401
        return  HTTPException(status_code=status_code, detail="Unauthorized")

    user = supabase.get_user(access_token)
    if user is None:
        status_code = 401
        return  HTTPException(status_code=status_code, detail="Unauthorized")
    return []