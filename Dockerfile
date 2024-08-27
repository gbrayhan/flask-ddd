# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar las dependencias de Python
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . /app

# Exponer el puerto que Flask usará
EXPOSE 5001

# Comando para iniciar la aplicación
CMD ["flask", "run", "--host=0.0.0.0" , "--port=5001"]
