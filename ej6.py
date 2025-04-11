import pandas as pd
import joblib  # Para guardar y cargar el modelo
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 1. Base de datos con ejemplos de texto
data = {
    'text': [
        'Me encanta este producto, es excelente',  # Positivo
        'No me gustó, es muy malo',  # Negativo
        'Es muy útil, lo recomiendo totalmente',  # Positivo
        'Horrible, me decepcionó por completo',  # Negativo
        'Gran calidad, vale la pena comprarlo',  # Positivo
        'No sirve para nada, pésima experiencia',  # Negativo
        'Funciona de maravilla, me encantó',  # Positivo
        'No lo volvería a comprar, mal producto',  # Negativo
        'Increíble, lo uso todos los días',  # Positivo
        'Es peor de lo que esperaba, muy malo',  # Negativo
        'Buena compra, muy recomendable',  # Positivo
        'Producto defectuoso, no lo compren',  # Negativo
        'Excelente relación calidad-precio',  # Positivo
        'Me arrepiento de comprarlo, mala calidad',  # Negativo
        'Funciona bien, pero podría mejorar',  # Neutro
        'No me gustó nada, no lo recomiendo',  # Negativo
        'Es un buen producto, cumple su función',  # Positivo
        'No es lo que esperaba, muy decepcionado',  # Negativo
        'Muy bueno, lo volvería a comprar',  # Positivo
        'Horrible, me llegó roto',  # Negativo
    ],
    'label': [
        'positivo', 'negativo', 'positivo', 'negativo',
        'positivo', 'negativo', 'positivo', 'negativo',
        'positivo', 'negativo', 'positivo', 'negativo',
        'positivo', 'negativo', 'neutral', 'negativo',
        'positivo', 'negativo', 'positivo', 'negativo'
    ]
}

# 2. Convertir datos a DataFrame
df = pd.DataFrame(data)

# 3. Separar características (X) y etiquetas (y)
X = df['text']
y = df['label']

# 4. Dividir datos en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Convertir texto en vectores numéricos con TF-IDF
vectorizer = TfidfVectorizer(stop_words=None)
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

# 6. Entrenar modelo con Naive Bayes
classifier = MultinomialNB()
classifier.fit(X_train_vect, y_train)

# 7. Guardar el modelo y el vectorizador
joblib.dump(classifier, 'modelo_entrenado.pkl')  # Guarda el modelo
joblib.dump(vectorizer, 'vectorizer.pkl')  # Guarda el vectorizador

# 8. Realizar predicciones
y_pred = classifier.predict(X_test_vect)

# 9. Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# 10. Mostrar resultados
print(f'\nPrecisión del modelo: {accuracy * 100:.2f}%')
print(f'\nReporte de clasificación:\n{report}')
print("\n✅ Modelo guardado correctamente en 'modelo_entrenado.pkl' y 'vectorizer.pkl'.")
