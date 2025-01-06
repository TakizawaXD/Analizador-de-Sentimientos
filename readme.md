# **Analizador de Sentimientos con Transformers**

## **Descripción**

Este proyecto es un analizador de sentimientos basado en el modelo de lenguaje de **Hugging Face**, que utiliza el pipeline de `sentiment-analysis` para clasificar un texto como **POSITIVO** o **NEGATIVO**. El programa interactúa con el usuario en la consola, donde puede ingresar cualquier texto y recibir el resultado del análisis junto con un nivel de confianza.

El objetivo de este proyecto es ayudar a identificar y clasificar el sentimiento detrás de cualquier entrada textual de manera sencilla y rápida.

## **Funcionalidades**

- **Análisis de Sentimientos:** El programa utiliza el modelo de Hugging Face para clasificar textos como positivos o negativos.
- **Interactividad:** El usuario puede ingresar textos de manera repetida y obtener los resultados en tiempo real.
- **Salida:** El análisis se realiza en la consola, y el resultado incluye la clasificación de sentimiento y el nivel de confianza.
- **Opción de Salir:** El usuario puede escribir `salir` para terminar el análisis y cerrar el programa.

## **Requisitos**

Este proyecto utiliza Python y la librería `transformers` de Hugging Face. Asegúrate de tener Python 3.6 o superior instalado. 

### **Instalación de dependencias**

1. **Instalar Python:** Si no tienes Python instalado, puedes descargarlo desde [aquí](https://www.python.org/downloads/).
2. **Instalar las dependencias:**

   Abre tu terminal o consola y ejecuta el siguiente comando para instalar la librería `transformers`:

   ```bash
   pip install transformers
   ```
    3. Instalar torch (si no está instalado automáticamente): 
    ```bash
    pip install torch
    ```
    Ejecuta el script:

    4.Después de instalar las dependencias, guarda el código en un archivo llamado analizador_sentimientos.py. Para ejecutar el script, usa el siguiente comando en tu terminal:

    5.Ejecuta el script:
    ```bash
    python proyect.py
    ```
    Interactúa con el programa:

    El programa te pedirá que ingreses un texto para analizar su sentimiento. Escribe cualquier texto y presiona Enter para ver el resultado.

    Si el sentimiento es positivo, verás algo como:
    ```	
    Resultado: POSITIVO (confianza: 0.98)
    ```

    Si el sentimiento es negativo, verás algo como:
    ```	
    Resultado: NEGATIVO (confianza: 0.98)
    ```

## **Ejemplo de uso**

```python
from transformers import pipeline    
classifier = pipeline("sentiment-analysis")
resultado = classifier("Este texto es muy positivo")
sentimiento = resultado[0]['label']
confianza = resultado[0]['score']
print(f"Sentimiento: {sentimiento} (Confianza: {confianza:.2f})")
```

## **Ejemplo de salida**

```bash
Ingresa un texto: Este texto es muy positivo
Resultado: POSITIVO (confianza: 0.98)
```

## **Ejemplo de salida con sentimientos negativos**

```bash
Ingresa un texto: Este texto es muy negativo
Resultado: NEGATIVO (confianza: 0.98)
```
ejemplo de ejecucion 

```bash
¡Bienvenido al analizador de sentimientos! 😊
Escribe un texto y te diré si el sentimiento es POSITIVO o NEGATIVO.
Para salir, escribe 'salir'.

Ingresa un texto: Me siento muy feliz hoy
Resultado: POSITIVE (confianza: 0.99)

Ingresa un texto: Estoy muy triste
Resultado: NEGATIVE (confianza: 0.95)

Ingresa un texto: salir
¡Gracias por usar el analizador de sentimientos! 🌟
```

```El script utiliza el pipeline de transformers de Hugging Face para realizar el análisis de sentimientos.
El modelo devuelve una etiqueta (POSITIVE o NEGATIVE) junto con un valor de confianza, que indica la certeza del modelo sobre la clasificación.
El usuario puede ingresar varios textos y obtener análisis para cada uno.```
