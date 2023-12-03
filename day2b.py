import re

# Opening file
file = open('day2.txt', 'r')
sum = 0

def enlarge_bag(bag, color, count):
    bag[color]=max(bag[color], count)

for line in file:
    r1=re.findall("((?P<count>\d+) (?P<color>\w+))(?P<token>[,;]?)", line)

    bag={'red':0, 'green':0, 'blue':0}

    for draw in r1:
        enlarge_bag(bag, draw[2], int(draw[1]))

    sum+= bag['red']*bag['green']*bag['blue']

    #print(r1)

print(sum)
file.close()