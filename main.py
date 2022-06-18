from typing import Optional, Union
from fastapi import FastAPI, Header, Response, Cookie
from pydantic import BaseModel

""" CRUD API """

class Item(BaseModel):
    id: int
    descricao: str
    valor: float

app = FastAPI()

@app.get("/")
def read_root(user_agent: Optional[str] = Header(None)):
    return {"user_agent": user_agent}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items")
def create_item(novo_item: Item, outro_item: Item):
    return [novo_item, outro_item]

@app.get("/cookies")
def cookies(response: Response):
    response.set_cookie (key ="meucookie",value="123456")
    return {"cookie":True}

@app.get("get-cookie")
def get_cookie(meucookie: Optional[str] = Cookie(None)):  
    return {"Cookie":meucookie}