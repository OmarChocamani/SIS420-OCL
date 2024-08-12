import numpy as np
import pandas as pd

# Parámetros para los datos
np.random.seed(0)  # Semilla para reproducibilidad
nro_ejemplos = 100

# Definir rangos de peso y estatura razonables
altura_min, altura_max = 1.50, 2.0  # En metros
peso_min, peso_max = 50, 100  # En kg

# Generar estaturas y pesos aleatorios dentro de los rangos definidos
estaturas = np.random.uniform(altura_min, altura_max, nro_ejemplos)

# Ajustar pesos en función de la estatura para evitar combinaciones no plausibles
# Asumiremos una relación lineal aproximada: peso = a * estatura + b
a = 100  # kg/m
b = -100  # kg
pesos = a * estaturas + b

# Crear DataFrame con los datos generados
df = pd.DataFrame({
    'Estatura (m)': estaturas,
    'Peso (kg)': pesos
})

# Guardar el DataFrame en un archivo CSV
df.to_csv('tabla.csv', index=False)
