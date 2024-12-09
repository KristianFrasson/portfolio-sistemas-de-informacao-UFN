import networkx as nx
import matplotlib.pyplot as plt

# Criar grafo
G = nx.Graph()

# Adicionar nós (usuários)
usuarios = ['Ana', 'Bruno', 'Carol', 'Daniel', 'Elena', 'Felipe']
G.add_nodes_from(usuarios)

# Adicionar arestas (conexões/amizades)
conexoes = [
    ('Ana', 'Bruno'), ('Ana', 'Carol'), ('Bruno', 'Daniel'),
    ('Carol', 'Elena'), ('Daniel', 'Felipe'), ('Elena', 'Felipe'),
    ('Bruno', 'Elena')
]
G.add_edges_from(conexoes)

# Visualizar
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color='lightblue', 
        node_size=1500, font_size=16, font_weight='bold')
plt.title("Rede Social - Conexões entre Usuários")
plt.show()