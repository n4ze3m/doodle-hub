import os
import time
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
import mimetypes
from routes.v1 import auth, doodle
from db.supa import SupaDB


supabase = SupaDB()

mimetypes.init()
mimetypes.add_type("application/javascript", ".js")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers
)



@app.get("/login", response_class=HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "isLogin": False})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    access_token = request.cookies.get("supabase_access_token")

    if access_token is None:
        return RedirectResponse(url="/login")

    user = supabase.get_user(access_token)
    if user is None:
        return RedirectResponse(url="/login")
    

    user_id = user.user.id
    user = user.user.user_metadata
    other_user_info = supabase.get_user_info(user_id)
    other_user_info = other_user_info.data[0]
    user["other"] = other_user_info

    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user, "isLogin": True})


@app.get("/draw/{id}", response_class=HTMLResponse)
async def index_page(request: Request, id: str):
    return templates.TemplateResponse("draw.html", {"request": request, "isLogin": False})

app.include_router(auth.router)
app.include_router(doodle.router)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    run(app, host="0.0.0.0", port=port)