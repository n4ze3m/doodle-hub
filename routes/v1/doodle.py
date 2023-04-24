from db.supa import SupaDB
from fastapi import APIRouter, HTTPException, Header, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from pydantic import BaseModel
import os
from notifiy import CourierNotification

class Doodle(BaseModel):
    img: str

supabase = SupaDB()
courier = CourierNotification()

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
    
    user = data[0]
    user_id = user["id"]
    user_name = user["raw_user_meta_data"]["name"]
    img_url = supabase.save_submissions(body.img, user_id)


    if user["email_notification"]:
        courier.send_notification(username=user_name, email=user["email"], img=img_url)
        

    
    return {
        "status": "ok",
        "img_url": img_url
    }