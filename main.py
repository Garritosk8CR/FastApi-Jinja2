from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

DOGS = [
    {"name": "Fido", "breed": "Mixed"},
    {"name": "Rover", "breed": "Golden Retriever"},
    {"name": "Spot", "breed": "Chihuahua"},
]

@app.get("/")
async def name(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "name": "Emilio Garro Rangel", "dogs": DOGS})