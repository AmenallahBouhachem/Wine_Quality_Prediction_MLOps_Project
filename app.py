from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
import uvicorn
import numpy as np
from MLOpsProject.pipeline.prediction import PredictionPipeline

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/train")
async def training():
    os.system("python main.py")
    return "Training Done"

@app.post("/predict")
async def predict(
    request: Request,
    fixed_acidity: float = Form(...),
    volatile_acidity: float = Form(...),
    citric_acid: float = Form(...),
    residual_sugar: float = Form(...),
    chlorides: float = Form(...),
    free_sulfur_dioxide: float = Form(...),
    total_sulfur_dioxide: float = Form(...),
    density: float = Form(...),
    pH: float = Form(...),
    sulphates: float = Form(...),
    alcohol: float = Form(...),
):
    try:
        data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
        data = np.array(data).reshape(1, 11)

        obj = PredictionPipeline()
        predict = obj.predict(data)

        return templates.TemplateResponse("results.html", {"request": request, "prediction": str(predict)})

    except Exception as e:
        print('The Exception message is: ', e)
        raise HTTPException(status_code=500, detail="Something went wrong")


if __name__ == "__main__":
    

    uvicorn.run(app, host="127.0.0.1", port=5001)
