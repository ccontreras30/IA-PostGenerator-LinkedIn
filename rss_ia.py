import feedparser

RSS_FEEDS = [
    "https://venturebeat.com/category/ai/feed/",
    "https://www.analyticsvidhya.com/blog/feed/",
    "https://www.artificialintelligence-news.com/feed/"
]

def obtener_articulos():
    articulos = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:2]:
            articulos.append({
                "titulo": entry.title,
                "contenido": entry.summary,
                "link": entry.link
            })
    return articulos
