import cv2
import os

def cut_out_image(name_image:str = ""):
    # Cargar clasificador de rostros
    face_classif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Leer la imagen
    image = cv2.imread(f'uploads/{name_image}')
    image_aux = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detectar rostros
    faces = face_classif.detectMultiScale(gray, 1.1, 5)

    # Crear la carpeta 'rostro' si no existe
    os.makedirs('rostro', exist_ok=True)

    count = 0

    for (x, y, w, h) in faces:
        # Dibujar el rectángulo en la imagen
        cv2.rectangle(image, (x, y), (x + w, y + h), (128, 0, 255), 2)

        # Extraer y redimensionar el rostro
        rostro = image_aux[y:y + h, x:x + w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)

        # Guardar el rostro en la carpeta 'rostro'
        cv2.imwrite(f'rostro/rostro_{name_image}', rostro)
        count += 1

    # Cerrar todas las ventanas
    cv2.destroyAllWindows()

def delete_image_upload(name_image):
    file_path = f'uploads/{name_image}'

    # Verificar si el archivo existe antes de eliminarlo
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Archivo eliminado: {file_path}")
    else:
        print(f"Error: El archivo {file_path} no existe")
