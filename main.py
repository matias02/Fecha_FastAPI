from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Contador para las llamadas a los endpoints
call_counter = 0

class Item(BaseModel):
    boolean_param: bool

@app.post("/date/")
async def get_date(item: Item):
    global call_counter
    call_counter += 1
    current_datetime = datetime.now()
    if item.boolean_param:
        return {"date": current_datetime.strftime("%Y-%m-%d %H:%M:%S")}
    else:
        return {"date": current_datetime.strftime("%Y-%d-%m")}

@app.get("/counter/")
async def get_counter():
    return {"counter": call_counter}