FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copiar el archivo de dependencias
COPY requirements.txt ./

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos al contenedor
COPY . .

# Se Expone el puerto 5000
EXPOSE 5000

# Comando por defecto para ejecutar la aplicación
CMD ["python", "app.py"]