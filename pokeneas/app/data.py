# app/data.py
import socket
import random

POKENEAS = [
    {"id": 1, "nombre": "Pyquique",   "altura": 0.7, "habilidad": "Agua",     "imagen_key": "pyquique.png",   "frase": "Fluye con la corriente."},
    {"id": 2, "nombre": "Electrisa",  "altura": 0.5, "habilidad": "Eléctrico","imagen_key": "electrisa.png",  "frase": "Chispea con energía."},
    {"id": 3, "nombre": "Floreal",    "altura": 0.8, "habilidad": "Planta",   "imagen_key": "floreal.png",    "frase": "Florece en cualquier terreno."},
    {"id": 4, "nombre": "Terratina",  "altura": 1.2, "habilidad": "Tierra",   "imagen_key": "terratina.png",  "frase": "Firme como una roca."},
    {"id": 5, "nombre": "Aerofin",    "altura": 0.6, "habilidad": "Volador",  "imagen_key": "aerofin.png",    "frase": "Surca los cielos libres."},
    {"id": 6, "nombre": "Ignix",      "altura": 0.9, "habilidad": "Fuego",    "imagen_key": "ignix.png",      "frase": "Arde con pasión."},
    {"id": 7, "nombre": "Cristaloc",  "altura": 0.4, "habilidad": "Hielo",    "imagen_key": "cristaloc.png",  "frase": "Brilla con frialdad."},
    {"id": 8, "nombre": "Lunaviva",   "altura": 1.0, "habilidad": "Psíquico", "imagen_key": "lunaviva.png",   "frase": "Pensamientos profundos."},
    {"id": 9, "nombre": "Solterra",   "altura": 1.1, "habilidad": "Roca",     "imagen_key": "solterra.png",   "frase": "Fuerza de la montaña."},
    {"id": 10,"nombre": "Aquaflax",   "altura": 0.6, "habilidad": "Agua",     "imagen_key": "aquaflax.png",   "frase": "Ondas incesantes."}
]


def get_random_pokenea():
    p = random.choice(POKENEAS)
    p["container_id"] = socket.gethostname()
    return p
