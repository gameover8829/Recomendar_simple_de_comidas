import argparse
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

def normalizar_texto(texto: str) -> str:
    """
    Limpia el texto para mejorar la comparación.
    """
    return texto.lower().strip()

def obtener_matches(ingredientes_usuario: str, ingredientes_comida: str) -> list[str]:
    """
    Regresa los ingredientes del usuario que también aparecen
    en los ingredientes de la comida recomendada.
    """
    lista_usuario = [
        normalizar_texto(i)
        for i in ingredientes_usuario.split(",")
        if i.strip()
    ]
    comida_normalizada = normalizar_texto(ingredientes_comida)
    matches = []
    for ingrediente in lista_usuario:
        if ingrediente in comida_normalizada:
            matches.append(ingrediente)
    return matches

def recomendar_comida(ingredientes_usuario: str, archivo_csv: str = "meals.csv") -> dict:
    """
    Recomienda la comida más parecida usando TF-IDF + similitud coseno.
    """
    df = pd.read_csv(archivo_csv)
    if df.empty:
        raise ValueError("El archivo CSV no contiene comidas.")
    ingredientes_usuario = normalizar_texto(ingredientes_usuario)
    if not ingredientes_usuario:
        raise ValueError("Debes ingresar al menos un ingrediente.")

    # Se comparan los ingredientes del usuario contra los ingredientes de cada comida.
    documentos = df["ingredientes"].fillna("").apply(normalizar_texto).tolist()
    documentos.append(ingredientes_usuario)
    vectorizer = TfidfVectorizer()
    matriz_tfidf = vectorizer.fit_transform(documentos)
    vector_usuario = matriz_tfidf[-1]
    vectores_comidas = matriz_tfidf[:-1]
    similitudes = cosine_similarity(vector_usuario, vectores_comidas).flatten()
    indice_mejor = similitudes.argmax()
    score = similitudes[indice_mejor]
    comida = df.iloc[indice_mejor]
    matches = obtener_matches(ingredientes_usuario, comida["ingredientes"])
    return {
        "nombre": comida["nombre"],
        "tipo": comida["tipo"],
        "tiempo_estimado": comida["tiempo_estimado"],
        "score": round(score * 100, 2),
        "matches": matches,
        "ingredientes": comida["ingredientes"],
    }

def main():
    parser = argparse.ArgumentParser(
        description="Recomendador simple de comidas usando TF-IDF + similitud coseno."
    )
    parser.add_argument(
        "ingredientes",
        type=str,
        help='Lista de ingredientes separados por coma. Ejemplo: "huevo, tortilla, queso"',
    )
    args = parser.parse_args()
    try:
        resultado = recomendar_comida(args.ingredientes)

        print(f"Comida recomendada: {resultado['nombre']}")
        print(f"Tipo: {resultado['tipo']}")
        print(f"Tiempo estimado: {resultado['tiempo_estimado']}")
        print(f"Coincidencia: {resultado['score']}%")
        if resultado["matches"]:
            print(f"Ingredientes relacionados: {', '.join(resultado['matches'])}")
        else:
            print("Ingredientes relacionados: No hubo coincidencias exactas, se usó similitud de texto.")

        print(f"Ingredientes de la comida: {resultado['ingredientes']}")
    except FileNotFoundError:
        print("Error: No se encontró el archivo meals.csv.")
    except Exception as error:
        print(f"Error: {error}")
if __name__ == "__main__":
    main()