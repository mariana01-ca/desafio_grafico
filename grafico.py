import numpy as np
import matplotlib.pyplot as plt

# Definir la matriz AA y el vector bb
AA = np.array([[1.0001, 1.0000],
               [1.0000, 1.0000]])
bb = np.array([2, 2])

# Definir las ecuaciones de las líneas
# Ecuaciones: 1.0001*x + 1.0000*y = 2
#             1.0000*x + 1.0000*y = 2
x = np.linspace(0, 5, 100)  # Generar valores para x

# Resolver para y en las dos ecuaciones
y1 = (bb[0] - AA[0, 0]*x) / AA[0, 1]
y2 = (bb[1] - AA[1, 0]*x) / AA[1, 1]

# Crear la gráfica
plt.plot(x, y1, label="1.0001*x + 1.0000*y = 2")
plt.plot(x, y2, label="1.0000*x + 1.0000*y = 2")

# Etiquetas y leyenda
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de las ecuaciones del sistema')
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()