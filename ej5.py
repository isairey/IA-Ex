import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Lista de palabras vacías en español (puedes ampliarla si lo deseas)
stop_words_spanish = [
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'de', 'y', 'o', 'que', 'es', 'muy', 'no', 'para'
]

# 1. Definir el conjunto de datos con reseñas de productos
data = {
    'text': [
        'Me encanta este producto, es excelente',
        'No me gustó, es muy malo',
        'Es muy útil, lo recomiendo totalmente',
        'Horrible, me decepcionó por completo',
        'Gran calidad, vale la pena comprarlo',
        'No sirve para nada, pésima experiencia',
        'Funciona de maravilla, me encantó',
        'No lo volvería a comprar, mal producto',
        'Increíble, lo uso todos los días',
        'Es peor de lo que esperaba, muy malo',
        'Buena compra, muy recomendable',
        'Producto defectuoso, no lo compren'
    ],
    'label': [
        'positivo', 'negativo', 'positivo', 'negativo',
        'positivo', 'negativo', 'positivo', 'negativo',
        'positivo', 'negativo', 'positivo', 'negativo'
    ]
}

# 2. Convertir datos a un DataFrame
df = pd.DataFrame(data)

# 3. Contar la cantidad de palabras en cada texto
df['word_count'] = df['text'].apply(lambda x: len(x.split()))

# 4. Mostrar el conteo de palabras
print("\nConteo de palabras por reseña:")
print(df[['text', 'word_count']])

# 5. Calcular la frecuencia de términos en el corpus
vectorizer_count = CountVectorizer(stop_words=stop_words_spanish)  # ✅ Aquí usamos la lista en español
word_matrix = vectorizer_count.fit_transform(df['text'])
word_freq = pd.DataFrame(word_matrix.toarray(), columns=vectorizer_count.get_feature_names_out())

# 6. Mostrar las palabras más frecuentes
print("\nFrecuencia de términos en el corpus:")
print(word_freq.sum().sort_values(ascending=False).head(10))

# 7. Separar características (X) y etiquetas (y)
X = df['text']
y = df['label']

# 8. Dividir datos en entrenamiento (70%) y prueba (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 9. Convertir texto en vectores numéricos con TF-IDF
vectorizer_tfidf = TfidfVectorizer(stop_words=stop_words_spanish)
X_train_vect = vectorizer_tfidf.fit_transform(X_train)
X_test_vect = vectorizer_tfidf.transform(X_test)

# 10. Entrenar el modelo con SVM
classifier = SVC(kernel='linear')
classifier.fit(X_train_vect, y_train)

# 11. Realizar predicciones
y_pred = classifier.predict(X_test_vect)

# 12. Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# 13. Mostrar resultados
print(f'\nPrecisión del modelo: {accuracy * 100:.2f}%')
print(f'\nReporte de clasificación:\n{report}')
