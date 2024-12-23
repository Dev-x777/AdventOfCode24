from collections import defaultdict

with open('day_23.in') as f:
    connections = [line.split('-') for line in f.read().splitlines()]

links = defaultdict(lambda:set())
for start,end in connections:
    links[start].add(end)
    links[end].add(start)
    
possibilities = set()
for c1 in links:
    for c2 in links[c1]-{c1}:
        for c3 in links[c2]-{c1,c2}:
            if c1 in links[c3]:
                possibilities.add(frozenset({c1,c2,c3}))
                
answer = len({triplet for triplet in possibilities if any(item.startswith('t') for item in triplet)})
print(answer)