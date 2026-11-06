# Imagen base oficial de Python
FROM python:3.11-slim

# Evita la generación de archivos .pyc y fuerza la salida directa al terminal
ENV PYTHONUNBUFFERED=1

# Crear y establecer el directorio de trabajo
WORKDIR /app

# Copiar las dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY src/ ./src

# Exponer el puerto por el que correrá Flet web
EXPOSE 8502

# Comando para ejecutar la app Flet como servidor web en el puerto 8502
CMD ["python", "src/app.py", "--web", "--port", "8502"]