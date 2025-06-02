import feedparser
import os

# URL del feed RSS
RSS_URL = "http://feeds.bbci.co.uk/news/world/rss.xml"

def obtener_noticias(url):
    """Obtiene las noticias de un feed RSS."""
    feed = feedparser.parse(url)
    noticias = []
    for entrada in feed.entries:
        noticias.append({
            "titulo": entrada.title,
            "resumen": entrada.summary,
            "link": entrada.link
        })
    return noticias

def actualizar_html(noticias):
    """Actualiza el archivo HTML con las nuevas noticias."""
    html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InfoTal 24</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="logo">InfoTal 24</div>
        <nav>
            <ul>
                <li><a href="#">Inicio</a></li>
                <li><a href="#">Mundo</a></li>
                <li><a href="#">Tecnología</a></li>
                <li><a href="#">Deportes</a></li>
                <li><a href="#">Contacto</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="noticias">
            <h2>Últimas Noticias</h2>
    """
    for noticia in noticias:
        html += f"""
            <div class="noticia">
                <h3><a href="{noticia['link']}">{noticia['titulo']}</a></h3>
                <p>{noticia['resumen']}</p>
                <a href="{noticia['link']}">Leer más</a>
            </div>
        """
    html += """
        </section>
    </main>
    <footer>
        <div class="redes-sociales">
            <a href="#">Facebook</a>
            <a href="#">Twitter</a>
            <a href="#">Instagram</a>
        </div>
        <p>© 2025 InfoTal 24. Todos los derechos reservados.</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    noticias = obtener_noticias(RSS_URL)
    actualizar_html(noticias)
    print("Archivo HTML actualizado con las últimas noticias.")
