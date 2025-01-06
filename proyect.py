from transformers import pipeline
classifier = pipeline("sentiment-analysis")
print("¡Bienvenido al analizador de sentimientos! 😊")
print("Escribe un texto y te diré si el sentimiento es POSITIVO o NEGATIVO.")
print("Para salir, escribe 'salir'.\n")
while True:

    texto = input("Ingresa un texto: ")
    if texto.lower() == "salir":
        print("¡Gracias por usar el analizador de sentimientos! 🌟")
        break
    resultado = classifier(texto)
    sentimiento = resultado[0]['label']
    confianza = resultado[0]['score']
    print(f"\nResultado: {sentimiento} (confianza: {confianza:.2f})\n")
