# uvicorn - use to run webserver
# django doesn't require additional libraries to run it on the webserver, but fastapi (a very light library), needs uvicorn to run it on the webserver

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

# async option works too.
# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# http://127.0.0.1:8000/items/5?q=somequery
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    '''
    Pass in either path paramter or query parameter in the endpoint
    Union[X, Y] means either X or Y datatype- so you can take multiple datatypes
    The path /items/{item_id} has a 
    - path parameter item_id that should be an int.
    - has an optional str query parameter q. (it is optional cause it is defined as None by default)
    wtf the docstring will show up in the auto-generated backend doc

    '''
    return {"item_id": item_id, "q": q}

# see the automatically generated docs
# SwaggerUI: http://127.0.0.1:8000/docs#/default/read_item_items__item_id__get
# ReDoc: http://127.0.0.1:8000/redoc#operation/read_root__get


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    '''
    You can pass in objects in FastAPI
    '''
    return {"item_name": item.name, "item_id": item_id}

# additional things to learn
# cookies, form fields, file, headers
# other validation constraints like maximum length
# oauth, deeply nested JSON models
# websockets, CORS, and more


# Terminology


# run the program (--reload: make the server restart after code changes. Only use for development)
# uvicorn <file basename>:<app variable> --reload
# uvicorn main:app --reload