# Esto es una imagen base para instalar las librerias requeridas
FROM python:3.8.10 as builder

# Aqui definimos donde se va a copiar el proyecto
COPY requirements.txt .

# Aqui instalamos todos las librerias del proyecto
RUN pip install --user -r requirements.txt 
#Esto es un ejemplo de una instalacion lite de un programa Python

# Esta es la imagen final del programa
FROM python:3.8.10-alpine

# Aqui definimos la ruta de trabajo del proyecto
WORKDIR /app

# Copiamos las librerias ya instalads
COPY --from=builder /root/.local/ /root/.local/

# Copiamos el programa desde nuestro entorno de trabajo al servidor
COPY . .

# Por si acaso, Definimos la ruta de donde se instalaron las librerias
ENV PATH=/root/.local:$PATH
ENV DB_NAME=DB_SMD1
ENV SERVER_HOST=192.168.0.200
ENV SERVER_PORT=27017
# BOTS
ENV BOTS_DB=DB_BOTS1
# Aqui instalamos mongo

# Aqui definimos la entrada del aplicativo
CMD ["python", "-m" , "flask", "run", "--host=0.0.0.0"]