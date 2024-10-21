import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('PS4.csv')
df6 = df.head(7)
juego = df6['Game']
año = df6['Year']

plt.plot(juego,año, color='green')
plt.xlabel('Juegos')
plt.ylabel('Año')
plt.title('año de salida de juegos PS4') 
plt.tight_layout()

plt.show()
