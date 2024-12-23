import networkx as nx

with open('day_23.in') as f:
    connections = [line.split('-') for line in f.read().splitlines()]
    
G = nx.Graph()
for start,end in connections:
    G.add_edge(start,end)
cliques = list(nx.find_cliques(G))
cliques = sorted(cliques,key=lambda item:len(item),reverse=True)
biggest_clique = cliques[0]
answer = ','.join(sorted(biggest_clique))
print(answer)