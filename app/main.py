import json
from typing import Any, Dict
from pydantic import BaseModel
from fastapi import FastAPI
from app.pandasAi import PandasAi

class Body(BaseModel):
    content: Dict[str, Any]

app = FastAPI()

@app.post("/generate")
async def generate_content(prompt: str, body: Body):
    pandas = PandasAi()

    json_object = body.content
    print(json_object)
    res = pandas.chat(json_object, prompt)

    print(res)

    if isinstance(res, str):
        response = res
    elif isinstance(res, float):
        response = str(res)
    elif isinstance(res, int):
        response = str(res)
    elif isinstance(res, list):
        response = json.dumps(set(res))
    else:
        response = res.to_json()

    return {"message": response}