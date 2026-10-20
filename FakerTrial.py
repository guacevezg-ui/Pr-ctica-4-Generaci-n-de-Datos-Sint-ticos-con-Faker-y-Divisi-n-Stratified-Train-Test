import pandas as pd
import numpy as np
from faker import Faker
from sklearn.model_selection import train_test_split

# Configuración de localización para México y fijación de semillas (Reproducibilidad)
fake = Faker('es_MX')
Faker.seed(42)
np.random.seed(42)

print("=== 1. GENERACIÓN PROGRAMÁTICA DE DATASET EXTENDIDO ===")
registros = []
for i in range(1000):
    registros.append({
        'id_cliente': i + 1,
        'nombre': fake.name(),
        'email': fake.email(),
        'estado_civil': np.random.choice(['Soltero', 'Casado', 'Divorciado'], p=[0.5, 0.4, 0.1]),
        'ingreso_anual': round(np.random.uniform(100000, 1000000), 2),
        # Adecuación obligatoria: Inclusión de dos campos sintéticos adicionales
        'telefono': fake.phone_number(),

        'fecha_nacimiento': fake.date_of_birth(minimum_age=18, maximum_age=75).strftime('%Y-%m-%d'),
        'churn': np.random.choice([0, 1], p=[0.8, 0.2])  # 20% tasa de abandono objetivo
    })

df_sintetico = pd.DataFrame(registros)

print("\nMuestra del DataFrame Sintético Original (Primeros 3 registros):")
print(df_sintetico[['id_cliente', 'nombre', 'estado_civil', 'telefono', 'fecha_nacimiento', 'churn']].head(3))

print("\n=== 2. ADECUACIÓN: CODIFICACIÓN NUMÉRICA (ONE-HOT ENCODING) ===")
# Convertir variable categórica 'estado_civil' a columnas numéricas (0 o 1)
df_encoded = pd.get_dummies(df_sintetico, columns=['estado_civil'], dtype=int)

print("Columnas resultantes tras la codificación:")
print(df_encoded.columns.tolist())

print("\n=== 3. SELECCIÓN DE CARACTERÍSTICAS Y PARTICIÓN ESTRATIFICADA ===")
# Remover identificadores personales, strings de texto y la variable objetivo
X = df_encoded.drop(columns=['id_cliente', 'nombre', 'email', 'telefono', 'fecha_nacimiento', 'churn'])
y = df_encoded['churn']

# Partición Estratificada manteniendo la proporción de clases desbalanceadas (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print(f"\nDimensiones Train Set: {X_train.shape} | Proporción Churn: {y_train.mean():.2f}")
print(f"Dimensiones Test Set: {X_test.shape}  | Proporción Churn: {y_test.mean():.2f}")
