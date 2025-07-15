import os
from rss_ia import obtener_articulos
from resumidor import resumir
from generador_post import generar_post
from generador_imagen import crear_imagen_post
import json

# Crear carpeta de salida
os.makedirs("output", exist_ok=True)

# Configuración
config = json.load(open("config.json"))
cantidad = config["cantidad_post"]

# Ejecutar flujo
articulos = obtener_articulos()

for i, art in enumerate(articulos[:cantidad]):
    resumen = resumir(art["contenido"])
    texto_post = generar_post(art["titulo"], resumen)
    nombre_imagen = f"output/post_{i+1}.png"
    crear_imagen_post(art["titulo"], resumen, art["link"], nombre_archivo=nombre_imagen)

    with open(f"output/post_{i+1}.txt", "w") as f:
        f.write(texto_post)

    print(f"✅ Post visual generado: {nombre_imagen}")
