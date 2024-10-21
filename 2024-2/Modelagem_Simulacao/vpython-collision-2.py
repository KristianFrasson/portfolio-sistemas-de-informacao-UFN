from vpython import canvas, box, sphere, vector, color, rate, mag
#Web VPython 3.2

import random  #biblioteca ale

# cena
scene = canvas(title="Simulação Criativa de Colisões", width=800, height=600, background=color.black)

# caixa 
tamanho_caixa = 10
caixa = box(pos=vector(0, 0, 0), size=vector(tamanho_caixa, tamanho_caixa, tamanho_caixa), opacity=0.1, color=color.white)

# esferas com formatacoes aleatorias da biblioteca
esferas = []
for i in range(10): #quantidade
    esfera = sphere(
        pos=vector(random.uniform(-4, 4), random.uniform(-4, 4), random.uniform(-4, 4)),
        radius=0.4,
        color=color.hsv_to_rgb(vector(random.uniform(0, 1), 0.8, 0.8)),  
        velocity=vector(random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2)),
        mass=1
    )
    esferas.append(esfera)

# Função para criar partículas de impacto
def criar_particulas(pos):
    particulas = []
    for _ in range(10):
        color_particula = color.hsv_to_rgb(vector(random.uniform(0, 1), 0.8, 1))
        esfera_particula = sphere(
            pos=pos,
            radius=0.05,
            color=color_particula,
            velocity=vector(random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1))
        )
        particulas.append(esfera_particula)
    
    # Desaparecer gradualmente
    for t in range(20):
        rate(50)
        for particula in particulas:
            particula.opacity -= 0.05
            particula.pos += particula.velocity * 0.1
        if particula.opacity <= 0:
            particula.visible = False
            particulas.remove(particula)

# Função de animação com colisões e limites da caixa
def animar_colisoes():
    while True:
        rate(50)  # Controla a taxa de atualização
        for esfera in esferas:
            # Atualiza a posição com base na velocidade
            esfera.pos += esfera.velocity * 0.1
            
            # Verifica colisões com as paredes da caixa
            if abs(esfera.pos.x) + esfera.radius > tamanho_caixa / 2:
                esfera.velocity.x *= -1
            if abs(esfera.pos.y) + esfera.radius > tamanho_caixa / 2:
                esfera.velocity.y *= -1
            if abs(esfera.pos.z) + esfera.radius > tamanho_caixa / 2:
                esfera.velocity.z *= -1

            # Verifica colisões entre esferas
            for outra_esfera in esferas:
                if esfera != outra_esfera and mag(esfera.pos - outra_esfera.pos) < (esfera.radius + outra_esfera.radius):
                    criar_particulas((esfera.pos + outra_esfera.pos) / 2)
                    # Troca de velocidades simples (modelo de colisão elástica)
                    esfera.velocity, outra_esfera.velocity = outra_esfera.velocity, esfera.velocity
                    
                    nova_cor_esfera = color.hsv_to_rgb(vector(random.uniform(0, 1), 0.8, 0.8))
                    nova_cor_outra_esfera = color.hsv_to_rgb(vector(random.uniform(0, 1), 0.8, 0.8))
                    esfera.color = nova_cor_esfera
                    outra_esfera.color = nova_cor_outra_esfera
                    
                    # Separar as esferas para evitar múltiplas colisões instantâneas
                    distancia = mag(esfera.pos - outra_esfera.pos)
                    normal = (esfera.pos - outra_esfera.pos).norm()
                    overlap = (esfera.radius + outra_esfera.radius) - distancia
                    esfera.pos += normal * (overlap / 2)
                    outra_esfera.pos -= normal * (overlap / 2)

# chamar animacoes 
animar_colisoes()
