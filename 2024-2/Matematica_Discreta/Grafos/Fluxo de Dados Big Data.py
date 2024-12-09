import networkx as nx
import matplotlib.pyplot as plt

# Criar grafo direcionado
G = nx.DiGraph()

# Adicionar nós
componentes = ['Dados Brutos', 'ETL', 'Data Lake', 'Processamento', 
               'Analytics', 'Visualização']
G.add_nodes_from(componentes)

# Adicionar arestas com direção
fluxo = [
    ('Dados Brutos', 'ETL'), ('ETL', 'Data Lake'),
    ('Data Lake', 'Processamento'), ('Processamento', 'Analytics'),
    ('Analytics', 'Visualização'), ('Data Lake', 'Visualização')
]
G.add_edges_from(fluxo)

# Visualizar
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightgreen',
        node_size=2000, font_size=10, font_weight='bold',
        arrows=True, edge_color='gray')
plt.title("Fluxo de Dados em Sistema Big Data")
plt.show()