import json
from typing import Annotated
from fastapi import FastAPI, Body
from pandasAi import PandasAi

app = FastAPI()


@app.post("/generate")
async def generate_content(prompt: str, body: Annotated[str, Body()]):
    pandas = PandasAi()

    json_object = json.loads(body)
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
