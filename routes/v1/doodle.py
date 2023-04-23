from db.supa import SupaDB
from fastapi import APIRouter, HTTPException, Header, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from pydantic import BaseModel
import os

class Doodle(BaseModel):
    img: str
supabase = SupaDB()

router = APIRouter(prefix="/api/v1")


@router.get("/doodles", tags=["doodles"])
async def doodles(request: Request):
    access_token = request.cookies.get("supabase_access_token")

    if access_token is None:
        status_code = 401
        return  HTTPException(status_code=status_code, detail="Unauthorized")

    user = supabase.get_user(access_token)
    if user is None:
        status_code = 401
        return  HTTPException(status_code=status_code, detail="Unauthorized")
    

    user_id = user.user.id

    user_submissions = supabase.get_user_submissions(user_id)
    data = user_submissions.data

    return data


@router.post("/doodle/{doodle_id}", tags=["doodles"])
async def doodle(request: Request, doodle_id: str, body: Doodle):

    user = supabase.find_user_by_public_id(doodle_id)
    data = user.data
    if  len(data) == 0:
        status_code = 404
        return  HTTPException(status_code=status_code, detail="Not found")
    
    user_id = data[0]["id"]
    supabase.save_submissions(body.img, user_id)

    
    return {
        "status": "ok"
    }