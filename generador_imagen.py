from PIL import Image, ImageDraw, ImageFont
import textwrap

def crear_imagen_post(titulo, resumen, link, nombre_archivo="output/post.png"):
    W, H = 1080, 1080
    fondo = Image.new("RGB", (W, H), color=(255,255,255))
    draw = ImageDraw.Draw(fondo)

    font_titulo = ImageFont.truetype("DejaVuSans-Bold.ttf", 40)
    font_texto = ImageFont.truetype("DejaVuSans.ttf", 30)

    titulo_txt = textwrap.fill("🤖 " + titulo.upper(), width=30)
    resumen_txt = textwrap.fill("💡 " + resumen, width=45)
    link_txt = f"🔗 Más en: {link}"

    draw.text((50, 60), titulo_txt, font=font_titulo, fill="black")
    draw.text((50, 300), resumen_txt, font=font_texto, fill="black")
    draw.text((50, 1000), link_txt, font=font_texto, fill="blue")

    fondo.save(nombre_archivo)
