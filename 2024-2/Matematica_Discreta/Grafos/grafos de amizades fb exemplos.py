import networkx as nx
import matplotlib.pyplot as plt

# Criar grafo direcionado (para demonstrar fonte/sumidouro)
G = nx.DiGraph()

# Adicionar nós (usuários)
usuarios = ['Ana', 'Bruno', 'Carol', 'Daniel', 'Elena', 'Felipe']
G.add_nodes_from(usuarios)

# Adicionar arestas direcionadas
conexoes = [
    ('Ana', 'Bruno'),    # Ana é fonte (só envia solicitações)
    ('Ana', 'Carol'),
    ('Bruno', 'Daniel'),
    ('Carol', 'Elena'),
    ('Daniel', 'Felipe'),
    ('Elena', 'Felipe'), # Felipe é sumidouro (só recebe)
    ('Bruno', 'Elena'),
    ('Carol', 'Carol')   # Laço (auto-conexão, ex: curtir próprio post)
]
G.add_edges_from(conexoes)

# Visualizar
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        node_size=1500, font_size=16, font_weight='bold',
        arrows=True, arrowsize=20)

# Destacar fonte em verde, sumidouro em vermelho
nx.draw_networkx_nodes(G, pos, nodelist=['Ana'], node_color='lightgreen', node_size=1500)
nx.draw_networkx_nodes(G, pos, nodelist=['Felipe'], node_color='salmon', node_size=1500)

plt.title("Rede Social - Fonte, Sumidouro e Laço")
plt.show()

# Identificar fonte, sumidouro e laço
print("Fonte:", [n for n in G.nodes() if G.in_degree(n) == 0])
print("Sumidouro:", [n for n in G.nodes() if G.out_degree(n) == 0])
print("Laços:", list(nx.selfloop_edges(G)))