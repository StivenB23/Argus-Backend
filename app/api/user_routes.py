from app.application.encrypt import decrypt_text
from app.application.user_service import create_user_service, get_user_by_id
from app.domain.user import User
from app.application.file_service import cut_out_image, delete_image_upload
from app.domain.schemas.user import UserCreate
from fastapi import APIRouter, Depends, UploadFile, File, Form
from fastapi.responses import JSONResponse
import shutil
import os
from sqlalchemy.orm import Session
from app.adapters.database.mysql import SessionLocal
from app.api.auth_routes import decode_token
from typing import Annotated
from fastapi.responses import JSONResponse

router = APIRouter(tags=["users"], prefix="/users")
key_encrypt = os.getenv("ENCRYPTION_KEY")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/message")
def show_message(user:Annotated[dict, Depends(decode_token)]):
    return {"message":"Hello"}

@router.get("/auth")
async def get_information_user(user:Annotated[dict, Depends(decode_token)], db: Session = Depends(get_db)):
    user_code = decrypt_text(user["id"], key_encrypt.encode('utf-8'))
    user_data = await get_user_by_id(db, int(user_code))
    return user_data

@router.post("/upload-photo")
async def create_user(file: UploadFile = File(...)):
    
    # Definir el directorio de destino
    save_path = "uploads/"
    os.makedirs(save_path, exist_ok=True)

    # Guardar el archivo en el directorio
    file_location = os.path.join(save_path, file.filename)
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    cut_out_image(file.filename)

    # delete_image_upload(file.filename)

    # Devolver la respuesta con los datos y la ubicación del archivo
    return JSONResponse(
        content={
            "info": f"Archivo guardado en {file_location}"
        }
    )


async def create_user(file: UploadFile = File(...), name: str = Form(...), surname: str = Form(...)):
    # Definir el directorio de destino
    save_path = "uploads/"
    os.makedirs(save_path, exist_ok=True)

    # Guardar el archivo en el directorio
    file_location = os.path.join(save_path, file.filename)
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)


    imagesPath = "uploads"
    imagesPathList = os.listdir(imagesPath)

    if not os.path.exists('Rostros encontrados'):
        print('Carpeta creada: Rostros encontrados')
        os.makedirs('Rostros encontrados')

    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

    count = 0
    for imageName in imagesPathList:
        image = cv2.imread(imagesPath+'/'+imageName)
        imageAux = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        faces = faceClassif.detectMultiScale(gray, 1.1, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(image, (x,y),(x+w,y+h),(128,0,255),2)
        cv2.rectangle(image,(10,5),(450,25),(255,255,255),-1)
        cv2.putText(image,'Presione s, para almacenar los rostros encontrados',(10,20), 2, 0.5,(128,0,255),1,cv2.LINE_AA)
        cv2.imshow('image',image)
        k = cv2.waitKey(0)
        if  k == ord('s'):
            for (x,y,w,h) in faces:
                rostro = imageAux[y:y+h,x:x+w]
                rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
                #cv2.imshow('rostro',rostro)
                #cv2.waitKey(0)
                cv2.imwrite('Rostros encontrados/rostro_{}.jpg'.format(count),rostro)
                count = count +1
        elif k == 27:
            break

    cv2.destroyAllWindows()    


    # Devolver la respuesta con los datos y la ubicación del archivo
    return JSONResponse(
        content={
            "info": f"Archivo guardado en {file_location}",
            "name": name,
            "surname": surname,})

@router.post("/register")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        await create_user_service(db, user)
        return JSONResponse(
            content={"info": "Archivo guardado en ..."},
            status_code=201  # Código 201 indica creación exitosa
        )
    except Exception as e:
        return JSONResponse(
            content={"error": f"Ocurrió un error: {str(e)}"},
            status_code=500  # Código 500 indica error interno del servidor
        )
