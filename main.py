from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Contador para las llamadas a los endpoints
call_counter = 0

class Item(BaseModel):
    boolean_param: bool = True  # Valor por defecto True para solicitudes GET

@app.post("/date/")
async def post_date(item: Item):
    global call_counter
    call_counter += 1
    return format_date(item.boolean_param)

@app.get("/date/")
async def get_date():
    global call_counter
    call_counter += 1
    # Devuelve la fecha con el formato por defecto cuando se accede via GET
    return format_date(True)

def format_date(boolean_param: bool):
    current_datetime = datetime.now()
    if boolean_param:
        return {"date": current_datetime.strftime("%Y-%m-%d %H:%M:%S")}
    else:
        return {"date": current_datetime.strftime("%Y-%d-%m")}

@app.get("/counter/")
async def get_counter():
    return {"counter": call_counter}