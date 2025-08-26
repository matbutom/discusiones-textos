# scripts/analisis_texto.py

from collections import Counter
import re
import unicodedata

# Lista de palabras comunes (stopwords) básicas en español
STOPWORDS = {
    "el", "la", "los", "las", "de", "y", "a", "en", "que", "un", "una",
    "del", "se", "por", "con", "para", "es", "al", "como", "su", "lo"
}

def limpiar_texto(texto):
    """
    Limpia un texto:
    - Convierte a minúsculas
    - Quita acentos
    - Elimina puntuación
    - Elimina stopwords
    """
    texto = texto.lower()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    texto = re.sub(r'[^a-z0-9\s]', '', texto)
    palabras = [palabra for palabra in texto.split() if palabra not in STOPWORDS]
    return palabras

def palabras_mas_comunes(texto, n=10):
    """
    Devuelve las n palabras más frecuentes de un texto.
    """
    palabras = limpiar_texto(texto)
    conteo = Counter(palabras)
    return conteo.most_common(n)

# Ejemplo de uso cuando se ejecuta directamente
if __name__ == "__main__":
    texto_ejemplo = "Este es un ejemplo de texto. Este texto sirve para probar el script."
    print(palabras_mas_comunes(texto_ejemplo, n=5))
