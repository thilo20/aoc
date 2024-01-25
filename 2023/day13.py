import re

# idea for simple flip of row and columns:
# transpose the input pattern! 
# https://stackoverflow.com/questions/44939583/i-want-to-transpose-a-list-of-strings-but-i-get-typeerror
li=['efh','opd','qst']
print( [''.join(s) for s in zip(*li)] )

def transpose(pattern):
    return [''.join(s) for s in zip(*pattern)]

def solve(pattern):
    """ detect a mirrored column """
    assert len(pattern[0])%2==1, "pattern column length should be odd"
    assert len(pattern)%2==1, "pattern row length should be odd"

    mid=int((len(pattern[0])-1)/2)
    # line of reflection: right of column index x
    # test largest mirror sizes first! (short circuit return)
    for x in range (mid, 0, -1):
        # mid to left, drop/ignore right
        if is_mirror(pattern, x, x): return x
    for x in range (mid, len(pattern[0])):
        # mid to right, drop/ignore left
        if is_mirror(pattern, x, len(pattern[0])-x): return x

    return -1

def is_mirror(pattern, x, n):
    for line in pattern:
        left=line[x-n:x]
        left=left[::-1]
        right=line[x:x+n]
        if left != right: 
            return False
    return True

# Opening file
file = open('day13.txt', 'r')

total=0
lines=[]

mirrors=[]
cols=0
rows=0

for line in file:
    if len(line)>1:
        lines.append(line.strip('\n'))
    else:
        # pattern complete
        col=solve(lines)
        if col>0:
            mirrors.append({'col', col})
            cols+=col
        else:
            # transpose
            lines2 = transpose(lines)
            # solve
            row=solve(lines2)
            if row>0:
                mirrors.append({'row', row})
                rows+=row
            else:
                for line in lines: print(line)
            assert row>0, "no row mirror found!"

        # reset
        lines=[]

file.close()

print(*mirrors)

total=100*rows+cols
print(total)