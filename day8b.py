import re

# Opening file
file = open('day8.txt', 'r')

# instructions
commands=file.readline().strip('\n')
# map
input={}
for line in file:
    r=re.findall("(\w+)", line)
    if len(r)==3:
        input[r[0]]= ( r[1], r[2] )
file.close()

starts = list(filter(lambda x: x.endswith('A'), input))
dests = list(filter(lambda x: x.endswith('Z'), input))

# calc steps
steps = 0
pos=starts[0]
while pos not in dests:
    com=commands[steps % len(commands)]
    if com=="L":
        pos=input[pos][0]
    else:
        pos=input[pos][1]
    steps+=1

print(steps)
