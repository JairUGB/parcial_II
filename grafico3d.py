import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Datos
condiciones = ['Hipertension', 'Cardiovascular', 'Cronica_renal', 'Obesidad', 'Gripa']
conteo_condiciones = [130, 90, 201, 604, 1000]

# Crear un gráfico de barras en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Definir posiciones de las barras
x = np.arange(len(condiciones))  # Posiciones en el eje X
y = np.zeros(len(condiciones))    # Todas las posiciones en Y son 0
z = np.zeros(len(condiciones))    # Comienzan desde 0 en el eje Z

# Ancho y profundidad de las barras
dx = 0.4  # Ancho de las barras
dy = 0.4  # Profundidad de las barras
dz = conteo_condiciones  # Altura de las barras

# Crear las barras
ax.bar3d(x, y, z, dx, dy, dz, color='skyblue')

# Añadir etiquetas
ax.set_title('Distribución de Condiciones de Salud en Pacientes (3D)')
ax.set_xlabel('Condiciones de Salud')
ax.set_ylabel('Y')  # Este eje puede ser utilizado para alguna otra dimensión si lo deseas
ax.set_zlabel('Número de Pacientes')
ax.set_xticks(x)
ax.set_xticklabels(condiciones, rotation=45)

# Mostrar el gráfico
plt.show()
