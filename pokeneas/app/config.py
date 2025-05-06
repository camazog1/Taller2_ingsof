# pokeneas/app/config.py
import os

class Config:
    # Nombre del bucket en S3 donde están las imágenes
    S3_BUCKET = "pokenea-images"

    # Otros ejemplos de configuración (puedes agregarlos si los necesitas)
    DEBUG = False
    TESTING = False
    SECRET_KEY = "cambia-esto-por-una-clave-segura"
