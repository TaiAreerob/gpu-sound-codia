from fastapi import FastAPI, File, UploadFile
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# upload single file
@app.post("/sound")
async def up_sound(file: UploadFile = File(...)):
    size = await file.read()
    return  { 
        "sound_id" : file.filename,
        "size": len(size),
        "category_id": random.randint(0, 5),
        "score": random.random()
    }

@app.get("/users")
async def users():
    users = [
        {
            "name": "Mars Kule",
            "age": 25,
            "city": "Lagos, Nigeria"
        },

        {
            "name": "Mercury Lume",
            "age": 23,
            "city": "Abuja, Nigeria"
        },

         {
            "name": "Jupiter Dume",
            "age": 30,
            "city": "Kaduna, Nigeria"
        }
    ]

    return users