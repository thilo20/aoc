from heapq import heappop, heappush

# i=y, k=x
G = {i + k*1j: int(c) for i,r in enumerate(open('2023/day17.txt'))
                      for k,c in enumerate(r.strip())}

def f(min, max, end=[*G][-1], x=0):
    todo = [(0,0,0,1)]#, (0,0,0,1j)]
    seen = set()

    while todo:
        val, _, pos, dir = heappop(todo) # val=cost

        if (pos==end): return val
        if (pos, dir) in seen: continue
        seen.add((pos,dir))

        for d in 1j/dir, -1j/dir: # 1.Drehung nach rechts/links an pos 0,0 bzw. 0+0j; d=j entspricht 'nach rechts' (x-Richtung)
            for i in range(min, max+1):
                if pos+d*i in G: # kompaktes ongrid
                    v = sum(G[pos+d*n] for n in range(1,i+1)) # Kosten fuer Abschnitt Geradeausfahrt
                    heappush(todo, (val+v, (x:=x+1), pos+d*i, d)) # x:= ist ein inline counter

print(f(1, 3), f(4, 10))