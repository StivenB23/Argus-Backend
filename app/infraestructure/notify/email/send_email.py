import emails
from jinja2 import Environment, FileSystemLoader
import os

def send_welcome_email():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    template_folder = os.path.join(BASE_DIR, "templates")
    # Configurar Jinja2 para cargar tu plantilla HTML
    env = Environment(loader=FileSystemLoader(template_folder))  # Carpeta 'templates/' donde tienes tu archivo HTML
    template = env.get_template('welcome.html')  # Nombre de tu plantilla

    # Variables para la plantilla
    html_content = template.render(full_name="Stiven Ospina", message="¡Bienvenido a nuestra plataforma!")

    # Crear el correo
    message = emails.html(
        subject="Correo de Bienvenida ✨",
        html=html_content,
        mail_from=("Mi Proyecto", "tu_email@example.com"),
    )

    response = message.send(
        to="stiven23ospina@gmail.com",
        smtp={
            "host": "sandbox.smtp.mailtrap.io",
            "port": 2525,
            "tls": True,
            "user": "27a62cd81a91c6",
            "password": "29a4362e495ff5"
        }
    )

    print("Correo enviado:", response.status_code == 250)

    # Verificar si el correo fue enviado correctamente
    return response.status_code == 250
