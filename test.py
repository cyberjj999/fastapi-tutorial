from fastapi import FastAPI

app = FastAPI()


# you can also specify the function to only accept a particular datatype
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}