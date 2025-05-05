import json
from flask import jsonify, render_template
from .data import get_random_pokenea

def register_routes(app): 
    @app.route("/")
    def html_pokenea():
        p = get_random_pokenea()
        data = {
            "id": p["id"],
            "nombre": p["nombre"],
            "altura": p["altura"],
            "habilidad": p["habilidad"],
            "container_id": p["container_id"]
        }
        json_str = json.dumps(data, indent=2, ensure_ascii=False)
        return render_template("neadex.html", json_data=json_str)

    @app.route("/frase")
    def display_pokenea():
        p = get_random_pokenea()
        bucket = app.config["S3_BUCKET"]
        url = f"https://{bucket}.s3.amazonaws.com/{p['imagen_key']}"
        return render_template("frase.html",
                               nombre=p["nombre"],
                               frase=p["frase"],
                               altura=p["altura"],
                               habilidad=p["habilidad"],
                               imagen=url,
                               container_id=p["container_id"])
