""" Este código analiza la trayectoria de varios proyectiles lanzados a diferentes velocidades y ángulos.
Vamos a calcular la distancia máxima de cada uno, encontrar el proyectil que alcanza más altura,
identificar los lanzamientos que que tuvieron un tiempo de vuelo superior a 5 segundos, 
analizaremos las trayectorias, guardando los datos en un archivo CSV y graficando las trayectorias,
por último, mostraremos una gráfica comparando todas las trayectorias."""
import json
import math
import csv
import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------
# Constante
# -----------------------------
g = 9.81  # gravedad (m/s^2)

# -----------------------------
# 1. Leer datos desde JSON
# -----------------------------
with open("proyectiles.json", "r", encoding="utf-8") as f:
    data = json.load(f)

resultados = []
trayectorias = {}

# Colores para cada proyectil
colores = {
    1: "blue",
    2: "red",
    3: "green",
    4: "orange",
    5: "purple"
}

# -----------------------------
# 2. Cálculos de cada proyectil
# -----------------------------
for p in data["proyectiles"]:
    pid = p["id"]
    v = p["velocidad"]
    angulo_rad = math.radians(p["angulo"])

    tiempo_vuelo = (2 * v * math.sin(angulo_rad)) / g
    alcance = (v ** 2 * math.sin(2 * angulo_rad)) / g
    altura_max = (v ** 2 * (math.sin(angulo_rad)) ** 2) / (2 * g)

    # Trayectoria
    t_vals = [i * tiempo_vuelo / 100 for i in range(101)]
    x_vals = [v * math.cos(angulo_rad) * t for t in t_vals]
    y_vals = [v * math.sin(angulo_rad) * t - 0.5 * g * t**2 for t in t_vals]

    trayectorias[pid] = (x_vals, y_vals)

    resultados.append({
        "id": pid,
        "velocidad": v,
        "angulo": p["angulo"],
        "alcance_maximo": alcance,
        "altura_maxima": altura_max,
        "tiempo_vuelo": tiempo_vuelo
    })

# -----------------------------
# 3. Guardar resultados en CSV
# -----------------------------
with open("resultados_proyectiles.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=resultados[0].keys())
    writer.writeheader()
    writer.writerows(resultados)

df = pd.DataFrame(resultados)

# -----------------------------
# 4. Análisis solicitado
# -----------------------------
print("Proyectil que alcanza mayor altura:")
print(df.loc[df["altura_maxima"].idxmax()])

print("\nProyectiles con tiempo de vuelo mayor a 5 segundos:")
print(df[df["tiempo_vuelo"] > 5])

# -----------------------------
# 5. Animación de trayectorias (un color por proyectil)
# -----------------------------
plt.figure()
plt.title("Animación de la trayectoria de los proyectiles")
plt.xlabel("Distancia (m)")
plt.ylabel("Altura (m)")
plt.grid(True)

for pid, (x, y) in trayectorias.items():
    color = colores.get(pid, "black")
    for i in range(len(x)):
        plt.plot(x[i], y[i], marker='o', color=color)
        plt.pause(0.01)

plt.show()

# -----------------------------
# 6. Gráfica comparativa final
# -----------------------------
plt.figure()
for pid, (x, y) in trayectorias.items():
    plt.plot(x, y, label=f"P{pid}", color=colores.get(pid, "black"))

plt.title("Comparación de Trayectorias de Proyectiles")
plt.xlabel("Distancia (m)")
plt.ylabel("Altura (m)")
plt.legend()
plt.grid(True)
plt.show()
