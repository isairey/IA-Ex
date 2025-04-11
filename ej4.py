
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


data = {
    'text': [
        'Este producto es excelente, muy útil',
        'No me gusta, es muy malo',
        'Me encanta, lo recomiendo mucho',
        'Horrible, no cumple lo prometido',
        'Gran producto, vale cada centavo',
        'No sirve para nada, totalmente decepcionado',
        'Muy bueno, funciona de maravilla',
        'Pésima compra, no lo volvería a comprar',
        'Excelente, lo uso todos los días',
        'No es lo que esperaba, muy malo',
        'Muy recomendable, excelente calidad',
        'Producto defectuoso, no lo compren'
    ],
    'label': ['positivo', 'negativo', 'positivo', 'negativo', 'positivo', 'negativo', 'positivo', 'negativo', 'positivo', 'negativo', 'positivo', 'negativo']
}


df = pd.DataFrame(data)


X = df['text']
y = df['label']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


vectorizer = TfidfVectorizer(stop_words='english')  
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)


classifier = SVC(kernel='linear')


classifier.fit(X_train_vect, y_train)


y_pred = classifier.predict(X_test_vect)


accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)


print(f'Precisión del modelo: {accuracy * 100:.2f}%')
print(f'Reporte de clasificación:\n{report}')
