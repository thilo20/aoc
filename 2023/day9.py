import re

# test automatic data download..
from aocd import data
# print(data)
# works! :)

def reduce(sequence):
    tree=[]
    seq=sequence
#    if(sum(sequence)==0): print(sequence)
    # while sum(seq)!=0:
    while not all(v == 0 for v in seq):
        tree.append(seq)
        seq=list(map(lambda x,y: y-x, seq, seq[1:len(seq)]))
    # print(sum(seq), seq)
    return tree

def solve(tree):
    n=len(tree)-1
    sum=tree[n].pop()
    n-=1
    while n>=0:
        sum+=tree[n].pop()
        n-=1
    return sum

# Opening file
file = open('day9.txt', 'r')

total=0
lines=[]
for line in file:
    r=re.findall("(-?\d+)", line)
    nums=list(map(lambda x:int(x), r))
    lines.append(nums)

    tree=reduce(nums)
    predict=solve(tree)

    total+=predict
file.close()

print(total)