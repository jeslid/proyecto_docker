from flask import Flask

# Crear una instancia de la aplicación flask siendo el app.py el punto de entrada del programa
app = Flask(__name__)

# Ruta principal 
@app.route('/')
def hello_joseluis():
    return "¡Hola Sherif, soy Jesus y esta es mi prueba de que he conseguido hacer mi proyecto con éxito, gracias por tu ayuda y tu esfuerzo de soportar a la clase de ASIR 2025!" 
    # Comentario que aparecerá en el navegador como respuesta


# Inicio de la aplicación si el archivo se esta ejecutando directamente
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)