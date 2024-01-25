import re

galaxies=[]

file = open("day11.txt")
y=0
for line in file:
    x=0
    for char in line:
        if char=='#': galaxies.append([x, y])
        x+=1
    y+=1
file.close()

# space to expand
void_rows=[]
void_cols=[]
void_expansion=1000000-1

# galaxies are initially sorted by row
max_row=galaxies[-1][1]
for y in range(max_row):
    n=any(map(lambda p: p[1]==y, galaxies))
    if not n:
        void_rows.append(y)
# expand galaxy rows
for gal in galaxies:
    cnt=sum(map(lambda p: p<gal[1], void_rows))
    gal[1]+=cnt*void_expansion

# sort galaxies by col
galaxies=sorted(galaxies, key=lambda g:g[0])
max_col=galaxies[-1][0]
for x in range(max_col):
    n=any(map(lambda p: p[0]==x, galaxies))
    if not n:
        void_cols.append(x)
# expand galaxy cols
for gal in galaxies:
    cnt=sum(map(lambda p: p<gal[0], void_cols))
    gal[0]+=cnt*void_expansion

# sum up Manhattan distances between galaxy pairs
total=0
for i in range(len(galaxies)-1):
    g1 = galaxies[i]
    for g2 in galaxies[i+1:]:
        dist = abs(g2[0]-g1[0])+abs(g2[1]-g1[1])
        total += dist
print(total)