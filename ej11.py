# Importar las librerías necesarias
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt

# Cargar el conjunto de datos 20 Newsgroups
newsgroups = fetch_20newsgroups(subset='all')

# Obtener los datos y las etiquetas
texts = newsgroups.data
labels = newsgroups.target
target_names = newsgroups.target_names

# Preprocesamiento: Convertir el texto en características numéricas usando TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.95, min_df=2)
X = vectorizer.fit_transform(texts)

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# Crear el clasificador Naive Bayes
naive_bayes_classifier = MultinomialNB()

# Entrenar el clasificador con los datos de entrenamiento
naive_bayes_classifier.fit(X_train, y_train)

# Hacer predicciones con el conjunto de prueba
y_pred = naive_bayes_classifier.predict(X_test)

# Evaluar el modelo
print("Exactitud:", accuracy_score(y_test, y_pred))
print("\nInforme de clasificación:")
print(classification_report(y_test, y_pred, target_names=target_names))

# Mostrar una muestra de predicciones
for i in range(5):
    print(f"\nNoticia {i+1}:")
    print(f"Texto: {newsgroups.data[i]}")
    print(f"Categoría real: {newsgroups.target_names[y_test[i]]}")
    print(f"Categoría predicha: {target_names[y_pred[i]]}")

