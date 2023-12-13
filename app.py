import os
import sys
from fastapi import FastAPI
import uvicorn
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from document_classification.pipeline.prediction import PredictionPipeline


app = FastAPI()


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/api/v1/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training Sucessful !!")

    except Exception as e:
        return Response(f"Error Occured : {e}")


@app.get("/api/v1/predict")
async def prediction(text: str):
    try:
        predict_pipeline = PredictionPipeline()
        predicted_class = predict_pipeline.predict(text)
        return predicted_class

    except Exception as e:
        return Response(f"Error Occured {e}")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
