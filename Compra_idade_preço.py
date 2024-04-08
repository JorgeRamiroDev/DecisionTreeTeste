from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Dados de exemplo
X = np.array([
    [25, 40],
    [35, 60],
    [45, 50],
    [20, 30],
    [50, 80],
    [23, 25],
    [55, 120],
    [32, 55]
])

y = np.array(['Não', 'Sim', 'Sim', 'Não', 'Sim', 'Não', 'Sim', 'Sim'])

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Criando e treinando o modelo
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Fazendo previsões
predictions = model.predict(X_test)

# Avaliando o modelo
accuracy = accuracy_score(y_test, predictions)
print(f'Acurácia: {accuracy:.2f}')

# Para prever uma nova instância
new_data = np.array([[10, 20]])
new_prediction = model.predict(new_data)
print(f'Previsão para nova instância: {new_prediction[0]}')
