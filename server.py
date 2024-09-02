from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
import dotenv
import os
import facedetect

dotenv.load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    allow_origins=['*']
)

MONGODB_URL = os.getenv("MONGODB_URL")
UPLOAD_FOLDER = './static/uploads'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

client = MongoClient(MONGODB_URL)

db_name = MONGODB_URL.split('/')[-1].split('?')[0]
db = client[db_name]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/uploader")
async def upload_file(file: UploadFile = File(...)):
    try:
        filename = file.filename
        filepath = UPLOAD_FOLDER + '/' + filename
        file_extension = os.path.splitext(filepath)[1]
        # save face in uploads folder
        with open(filepath, "wb") as buffer:
            buffer.write(file.file.read())

        result = facedetect.identify_faces(filepath)

        # delete uploaded files
        os.remove(filepath)

        return JSONResponse(status_code=200, content={"result": result})
    
    except Exception as e:

        return JSONResponse(status_code=500, content={"error": str(e)})

