import matplotlib.pyplot as plt

x = ["enero","febrero","marzo","abril","mayo"]
y = [1000, 700, 860, 1500, 1100]

plt.plot(x, y, marker='o')

plt.title("Gráfico de lineas ventas mensuales")
plt.xlabel("meses")
plt.ylabel("ventas($)")

plt.show()
