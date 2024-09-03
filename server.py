from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import dotenv
import os
import facedetect
import backgroudanalze

dotenv.load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    allow_origins=['*']
)

UPLOAD_FOLDER = './static/uploads'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/uploader")
async def upload_file(file: UploadFile = File(...)):
    try:
        filename = file.filename
        filepath = UPLOAD_FOLDER + '/' + filename
        file_extension = os.path.splitext(filepath)[1]

        with open(filepath, "wb") as buffer:
            buffer.write(file.file.read())

        result = facedetect.identify_faces(filepath)

        if result == True:
            result = backgroudanalze.check_background(filepath)
            if result == True:
               os.remove(filepath)
               return JSONResponse(status_code=200, content={"result": "image is valid"})
            else:
                os.remove(filepath)
                return JSONResponse(status_code=400, content={"error": "image has a busy background"})

        else :
            os.remove(filepath)
            return JSONResponse(status_code=400, content={"error": "image has except one face or no face"})
        
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

