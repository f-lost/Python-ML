import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import matplotlib.pyplot as plt

# Caricamento del dataset "Diabetes" con dati standardizzati
diabetes = load_diabetes()
X = diabetes.data  # Caratteristiche (10 misurazioni cliniche)
y = diabetes.target  # Variabile target (progressione della malattia)

# Esplorazione iniziale del dataset
print("Feature Names:", diabetes.feature_names)
print("\nEsempio di dati:")
print(pd.DataFrame(X, columns=diabetes.feature_names).head())

# Suddivisione del dataset in set di training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Caricamento del dataset "Diabetes" con dati non standardizzati
diabetes_notstandardized = load_diabetes(scaled= False)
X = diabetes_notstandardized.data  # Caratteristiche (10 misurazioni cliniche)
y = diabetes_notstandardized.target  # Variabile target (progressione della malattia)

# Esplorazione iniziale del dataset
print("Feature Names:", diabetes_notstandardized.feature_names)
print("\nEsempio di dati:")
print(pd.DataFrame(X, columns=diabetes_notstandardized.feature_names).head())

# Suddivisione del dataset in set di training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creazione del modello di regressione lineare
model = LinearRegression()

# Addestramento del modello
model.fit(X_train, y_train)

# Predizione sui dati di test
y_pred = model.predict(X_test)

# Calcolo delle metriche di valutazione
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Stampa dei risultati
print("\nPrestazioni del modello:")
print(f"Errore Quadratico Medio (MSE): {mse:.2f}")
print(f"Coefficiente di Determinazione (R²): {r2:.2f}")


# Scatter plot delle predizioni rispetto ai valori reali
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color="blue")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', linewidth=2)
plt.title("Confronto tra Valori Reali e Predetti", fontsize=14)
plt.xlabel("Valori Reali", fontsize=12)
plt.ylabel("Valori Predetti", fontsize=12)
plt.grid(alpha=0.3)
plt.show()

# Residual plot
residuals = y_test - y_pred

plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals, alpha=0.7, color="purple")
plt.axhline(0, color='red', linestyle='--', linewidth=2)
plt.title("Grafico dei Residui", fontsize=14)
plt.xlabel("Valori Predetti", fontsize=12)
plt.ylabel("Residui (Valore Reale - Valore Predetto)", fontsize=12)
plt.grid(alpha=0.3)
plt.show()