
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

data = {
    'text': [
        'me encanta la programación',
        'odio los bugs',
        'la programación es divertida',
        'me gustan los videojuegos',
        'odio los errores',
        'programar es muy interesante'
    ],
    'label': ['negativo', 'positivo', 'positivo', 'neutral', 'negativo', 'positivo']
}

df = pd.DataFrame(data)


X = df['text']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


vectorizer = CountVectorizer()
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

classifier = MultinomialNB()
classifier.fit(X_train_vect, y_train)

y_pred = classifier.predict(X_test_vect)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Precisión del modelo: {accuracy * 100:.2f}%')
print(f'Reporte de clasificación:\n{report}')
