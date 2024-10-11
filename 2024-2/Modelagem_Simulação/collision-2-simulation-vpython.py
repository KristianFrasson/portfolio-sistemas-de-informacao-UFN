from vpython import *
#Web VPython 3.2

import random # biblioteca de valroes aleatorios

# cena
scene = canvas(title="Simulação Criativa de Colisões", width=800, height=600, background=color.black)

# chao
chao = box(pos=vector(0,-0.1,0), size=vector(10,0.2,10), color=color.gray(0.5))

# Cria as esferas com propriedades diferentes
esferas = []
for i in range(5):
    esfera = sphere(
        pos=vector(random.uniform(-4, 4), random.uniform(0, 2), random.uniform(-4, 4)),
        radius=0.2,
        color=color.hsv_to_rgb(vector(random.uniform(0, 1), 0.8, 0.8)),  # Cor aleatória
        velocity=vector(random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2)),
        mass=1
    )
    esferas.append(esfera)

# Função para criar partículas de impacto
def criar_particulas(pos):
    for _ in range(10):
        color_particula = color.hsv_to_rgb(vector(random.uniform(0, 1), 0.8, 1))
        esfera_particula = sphere(
            pos=pos,
            radius=0.05,
            color=color_particula,
            velocity=vector(random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1))
        )
        # Partículas desaparecem após um curto período
        sphere(pos=pos, radius=0.05, color=color_particula, visible=False, delay=0.2)

# Função de animação com colisões e gravidade
def animar_colisoes():
    while True:
        rate(50)  # Controla a taxa de atualização
        for esfera in esferas:
            # Atualiza a posição com base na velocidade
            esfera.pos += esfera.velocity * 0.1
            
            # Aplicar gravidade
            esfera.velocity.y -= 0.01
            
            # Verifica colisão com o chão
            if esfera.pos.y < esfera.radius:
                esfera.pos.y = esfera.radius
                esfera.velocity.y *= -0.8  # Colisão elástica com o chão

            # Verifica colisões entre esferas
            for outra_esfera in esferas:
                if esfera != outra_esfera and mag(esfera.pos - outra_esfera.pos) < (esfera.radius + outra_esfera.radius):
                    criar_particulas((esfera.pos + outra_esfera.pos) / 2)
                    # Troca de velocidades simples (modelo de colisão elástica)
                    esfera.velocity, outra_esfera.velocity = outra_esfera.velocity, esfera.velocity
                    
                    # Separar as esferas para evitar múltiplas colisões instantâneas
                    distancia = mag(esfera.pos - outra_esfera.pos)
                    normal = (esfera.pos - outra_esfera.pos).norm()
                    overlap = (esfera.radius + outra_esfera.radius) - distancia
                    esfera.pos += normal * (overlap / 2)
                    outra_esfera.pos -= normal * (overlap / 2)

# Inicia a animação
animar_colisoes()
