from vpython import canvas, sphere, vector, color, rate
from math import cos, sin
#Web VPython 3.2

# cena
scene = canvas(title="Sistema Solar", width=800, height=600, background=color.black)

sol = sphere(pos=vector(0,0,0), radius=0.7, color=color.yellow, emissive=True)

planetas = {
    'Mercúrio': {'pos': vector(1,0,0), 'radius': 0.1, 'color': color.gray(0.5)},
    'Vênus': {'pos': vector(1.5,0,0), 'radius': 0.2, 'color': color.orange},
    'Terra': {'pos': vector(2,0,0), 'radius': 0.2, 'color': color.blue},
    'Marte': {'pos': vector(3,0,0), 'radius': 0.15, 'color': color.red},
    'Júpiter': {'pos': vector(4,0,0), 'radius': 0.5, 'color': color.orange},
    'Saturno': {'pos': vector(5,0,0), 'radius': 0.4, 'color': color.yellow},
    'Urano': {'pos': vector(6,0,0), 'radius': 0.35, 'color': color.cyan},
    'Netuno': {'pos': vector(7,0,0), 'radius': 0.3, 'color': color.blue}
}

# esferas dos planetas
esferas_planetas = {}
for nome, dados in planetas.items():
    esfera = sphere(pos=dados['pos'], radius=dados['radius'], color=dados['color'])
    esferas_planetas[nome] = esfera

# Define parâmetros orbitais
orbita = {
    'Mercúrio': 1, 'Vênus': 1.5, 'Terra': 2, 'Marte': 3,
    'Júpiter': 4, 'Saturno': 5, 'Urano': 6, 'Netuno': 7
}

# Velocidades orbitais
velocidades = {
    'Mercúrio': 0.1, 'Vênus': 0.07, 'Terra': 0.05, 'Marte': 0.04,
    'Júpiter': 0.03, 'Saturno': 0.02, 'Urano': 0.015, 'Netuno': 0.01
}

def animar_sistema_solar():
    tempo = 0
    while True:
        rate(50)  # Controla a taxa de atualização da animação
        tempo += 0.01
        for nome, esfera in esferas_planetas.items():
            r = orbita[nome]
            angulo = velocidades[nome] * tempo
            esfera.pos = vector(r * cos(angulo), r * sin(angulo), 0)

animar_sistema_solar()
