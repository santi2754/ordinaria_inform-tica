Análisis de Trayectorias de Proyectiles
Descripción

Este proyecto permite simular y analizar la trayectoria de proyectiles lanzados con diferentes velocidades y ángulos.
El programa calcula:

Alcance máximo

Altura máxima

Tiempo de vuelo

Además, genera:

Una animación del movimiento de los proyectiles

Una gráfica comparativa de todas las trayectorias

Un archivo CSV con todos los datos calculados

Una recapitulación final impresa en la terminal

Todo esto leyendo los datos desde un archivo JSON, sin necesidad de modificar el código.

Estructura del proyecto
proyectiles/
│
├── proyectiles.json          # Archivo de entrada con los datos de los proyectiles
├── resultados_proyectiles.csv # Archivo CSV generado con los resultados
├── main.py                   # Código principal en Python
└── README.md                 # Este archivo

Formato del JSON de entrada

El archivo proyectiles.json debe tener la siguiente estructura:

{
    "proyectiles": [
        {"id": 1, "velocidad": 50, "angulo": 30},
        {"id": 2, "velocidad": 55, "angulo": 45},
        {"id": 3, "velocidad": 40, "angulo": 60},
        {"id": 4, "velocidad": 70, "angulo": 35},
        {"id": 5, "velocidad": 60, "angulo": 50}
    ]
}


id: Identificador único del proyectil

velocidad: Velocidad inicial en m/s

angulo: Ángulo de lanzamiento en grados

Nota: Se pueden añadir más proyectiles simplemente agregando objetos dentro del array "proyectiles".

Requisitos

Python 3.7 o superior

Librerías:

matplotlib

pandas

math (incluida en Python)

json (incluida en Python)

csv (incluida en Python)

Instalación rápida de librerías necesarias:

pip install matplotlib pandas

Uso

Coloca el archivo proyectiles.json en la misma carpeta que el script main.py.

Ejecuta el programa:

python main.py


Se mostrarán en la terminal:

El proyectil que alcanza mayor altura

Los proyectiles con tiempo de vuelo mayor a 5 segundos

Una recapitulación completa de todos los proyectiles

Se abrirán las gráficas:

Animación de cada proyectil mostrando su trayectoria en tiempo real

Gráfica comparativa final de todas las trayectorias

El archivo resultados_proyectiles.csv se generará con todos los datos calculados.

Salida esperada

CSV: Contendrá id, velocidad, angulo, alcance_maximo, altura_maxima y tiempo_vuelo de cada proyectil

Gráfica animada: Cada proyectil en un color fijo durante la animación

Gráfica comparativa final: Todas las trayectorias en un mismo gráfico

Terminal: Recapitulación completa de los datos de cada proyectil
