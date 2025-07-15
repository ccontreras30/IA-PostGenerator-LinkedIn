import json

def generar_post(titulo, resumen):
    config = json.load(open("config.json"))
    hashtags = " ".join(config["hashtags"])
    firma = config["firma"]
    post = f"""🚀 {titulo}\n\n💡 {resumen}\n\n📌 ¿Cómo crees que este avance afectará la industria?\n{hashtags}\n{firma}"""
    return post
