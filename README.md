# Práctica 4: Generación de Datos Sintéticos con Faker y División Stratified Train-Test

Este repositorio contiene la solución e implementación avanzada para la **Práctica 4**, enfocada en la simulación controlada de datos estructurados, preservación de la privacidad informática corporativa y balanceo probabilístico de subconjuntos de datos para Machine Learning.

## 📌 Objetivos de la Práctica
* **Generar programáticamente** un conjunto de datos sintéticos estructurados de 1,000 registros de clientes empleando localización mexicana (`es_MX`).
* **Asegurar la reproducibilidad** matemática de los experimentos mediante la fijación estricta de semillas aleatorias (`seed=42`).
* **Implementar ingeniería de características** convirtiendo variables cualitativas categóricas a vectores numéricos binarios utilizando codificación *One-Hot Encoding*.
* **Mitigar el sesgo de selección** mediante una partición probabilística estratificada (*Stratified Train-Test Split*) para mantener proporciones idénticas en variables objetivo desbalanceadas.

---

## 🛠️ Tecnologías y Librerías Utilizadas
El proyecto ha sido desarrollado en el entorno integrado **Visual Studio Code** sobre un entorno virtual aislado (`venv`) utilizando:
* **Faker (es_MX):** Para la creación y anonimización de identidades sintéticas regionales (Nombres, correos, teléfonos de México y fechas de nacimiento).
* **Pandas:** Para la estructuración tabular y codificación matricial mediante sub-columnas binarias (`pd.get_dummies`).
* **NumPy:** Para la selección probabilística controlada y manipulación vectorial.
* **Scikit-Learn:** Específicamente el módulo `sklearn.model_selection.train_test_split` configurado con preservación de clase objetivo.

---

## 🚀 Instrucciones de Configuración y Ejecución

### 1. Clonar e ingresar al Repositorio
```bash
git clone <URL_DE_TU_REPOSITORIO>
cd <NOMBRE_DE_TU_REPOSITORIO>
```

### 2. Activar el Entorno Virtual Aislado
En sistemas operativos Linux / Ubuntu / macOS:
```bash
source venv/bin/activate
```
En sistemas operativos Windows:
```bash
.\venv\Scripts\activate
```

### 3. Instalar Dependencias Congeladas
Instala los paquetes core requeridos ejecutando el manifiesto del proyecto:
```bash
pip install -r requirements.txt
```

### 4. Lanzar el Script de Datos
Para compilar y validar las particiones directamente en tu terminal de comandos, ejecuta:
```bash
python generacion_datos.py
```

---

## 📊 Matriz Comparativa de Distribución (Resultados Reales)
Gracias al bloqueo de aleatoriedad y al parámetro `stratify=y`, las muestras se segmentaron sin sesgar el modelo:

| Segmento del Dataset | Registros Totales (\(N\)) | Proporción de la Clase Churn (Abandono) | Estado de Sesgo de Selección |
| :--- | :--- | :--- | :--- |
| **Dataset Completo Original** | 1,000 | **19.10%** | Distribución base poblacional original. |
| **Conjunto de Entrenamiento (Train)** | 800 (80%) | **19.12%** | **Muestreo Perfecto** (Sin sesgo). |
| **Conjunto de Prueba (Test)** | 200 (20%) | **19.00%** | **Muestreo Perfecto** (Sin sesgo). |

---

## 📁 Estructura del Repositorio
```text
├── .gitignore          # Archivo para la exclusión de artefactos locales y entornos
├── README.md           # Documentación técnica general (este archivo)
├── requirements.txt    # Manifiesto de dependencias instaladas en el venv
└── generacion_datos.py # Código fuente principal extendido en Python
```
