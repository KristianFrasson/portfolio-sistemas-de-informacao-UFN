import networkx as nx
import matplotlib.pyplot as plt

# Criar grafo direcionado
G = nx.DiGraph()

# Adicionar nós
usuarios = ['User1', 'User2', 'User3']
posts = ['Post A', 'Post B', 'Post C']
G.add_nodes_from(usuarios + posts)

# Adicionar arestas com peso (interações)
interacoes = [
    ('User1', 'Post A', 5), ('User1', 'Post B', 3),
    ('User2', 'Post B', 4), ('User2', 'Post C', 5),
    ('User3', 'Post A', 2), ('User3', 'Post C', 4)
]

for (u, v, w) in interacoes:
    G.add_edge(u, v, weight=w)

# Visualizar
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='pink',
        node_size=1500, font_size=12, font_weight='bold',
        arrows=True)
nx.draw_networkx_edge_labels(G, pos, 
                            edge_labels=nx.get_edge_attributes(G,'weight'))
plt.title("Sistema de Recomendação - Interações Usuário-Post")
plt.show()