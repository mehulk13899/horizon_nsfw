from functions import download_image
from config import PORT
import os
import uvicorn
from fastapi import FastAPI
import opennsfw2 as n2

from nsfw_detector import predict
app = FastAPI()

model = predict.load_model('nsfw_detector/nsfw_model.h5')


@app.get("/")
async def detect_nsfw(url: str):
    if not url:
        return {"ERROR": "URL PARAMETER EMPTY"}
    image = await download_image(url)
    if not image:
        return {"ERROR": "IMAGE SIZE TOO LARGE OR INCORRECT URL"}
    results = predict.classify(model, image)
    os.remove(image)
    hentai = results['data']['hentai']
    sexy = results['data']['sexy']
    porn = results['data']['porn']
    drawings = results['data']['drawings']
    neutral = results['data']['neutral']
    if neutral >= 25:
        results['data']['is_nsfw'] = False
        return results
    elif (sexy + porn + hentai) >= 70:
        results['data']['is_nsfw'] = True
        return results
    elif drawings >= 40:
        results['data']['is_nsfw'] = False
        return results
    else:
        results['data']['is_nsfw'] = False
        return results

@app.get("/image")
async def opennsfw2image(url: str):
        image_path = "path/to/your/image.jpg"
        if not url:
            return {"ERROR": "URL PARAMETER EMPTY"}
        image = await download_image(url)
        print("image",image)
        # if not image:
        #     return {"ERROR": "IMAGE SIZE TOO LARGE OR INCORRECT URL"}
        # nsfw_probability = n2.predict_image(image_path)
        return []


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")