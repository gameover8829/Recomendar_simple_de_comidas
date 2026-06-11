# RECOMENDADOR SIMPLE DE COMIDAS

## Descripción del proyecto
Este proyecto es un recomendador simple de comidas desarrollado en Python.  
El sistema recibe una lista de ingredientes disponibles y recomienda la comida más parecida dentro de un archivo CSV.
La recomendación se realiza usando una técnica sencilla de inteligencia artificial:
-TF-IDF
-Similitud coseno
El objetivo es comparar los ingredientes ingresados por el usuario contra los ingredientes de distintas comidas registradas en `meals.csv`.

## Estructura del proyecto
RECOMENDADOR_SIMPLE_DE_COMIDAS/
│
├── meals.csv
├── app.py
├── web_app.py
├── requirements.txt
└── README.md

## Archivos principales
### meals.csv
Contiene más de 100 comidas de ejemplo con los siguientes campos:
- nombre
- ingredientes
- tiempo_estimado
- tipo

Los tipos de comida disponibles son:
- Desayuno
- Comida
- Cena
- Snack

### app.py
Programa principal que se ejecuta desde la línea de comandos.

### web_app.py
Interfaz web sencilla creada con Streamlit.

### requirements.txt
Lista de dependencias necesarias para ejecutar el proyecto.

## Instalación de dependencias
Primero, abre una terminal dentro de la carpeta del proyecto:
-Ejemplo
cd RECOMENDADOR_SIMPLE_DE_COMIDAS

Después instala las dependencias:
Comando
pip install -r requirements.txt


## Cómo ejecutar el programa
Ejecuta el archivo app.py enviando los ingredientes entre comillas y separados por coma:
-Ejemplo
python app.py "huevo, tortilla, queso"


## Ejemplos de uso
### Ejemplo 1
python app.py "huevo, tortilla, queso"

Salida esperada:

Comida recomendada: quesadilla con huevo
Tipo: Desayuno
Tiempo estimado: 10 minutos
Coincidencia: 100.0%
Ingredientes relacionados: huevo, tortilla, queso
Ingredientes de la comida: huevo, tortilla, queso
```

### Ejemplo 2
python app.py "pollo, arroz, zanahoria"

Posible salida:

Comida recomendada: pollo con arroz
Tipo: Comida
Tiempo estimado: 35 minutos
Coincidencia: 77.53%
Ingredientes relacionados: pollo, arroz, zanahoria
Ingredientes de la comida: pollo, arroz, zanahoria, chícharo, ajo
```


## Ejecutar la interfaz web con Streamlit
Para abrir la versión web, ejecuta:
streamlit run web_app.py

Después se abrirá una página en el navegador donde podrás escribir los ingredientes y obtener la recomendación.

## Técnica utilizada
El programa convierte los ingredientes de cada comida y los ingredientes del usuario en vectores numéricos usando `TfidfVectorizer`.
Después calcula la similitud entre el vector del usuario y cada comida usando `cosine_similarity`.
La comida con mayor similitud es la recomendación final.