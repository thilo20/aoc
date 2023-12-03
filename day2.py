import re

# Opening file
file = open('day2.txt', 'r')
sum = 0

# Game (\d+): (((?'count'\d+) (?'color'\w+)[, ;]*)*)?;
# (Game (?P<game>\d+): )?((?P<count>\d) (?P<color>\w+))(?P<token>[,;]?)

bag={'red':12, 'green':13, 'blue':14}

def is_not_enough(color, count):
    return bag[color]<count

for line in file:
    #print("Line{}: {}".format(count, line.strip()))
    add=int(re.findall("Game (?P<game>\d+): ", line)[0])

    r1=re.findall("((?P<count>\d+) (?P<color>\w+))(?P<token>[,;]?)", line)

    for draw in r1:
        if is_not_enough(draw[2], int(draw[1])):
            add=0
            break

    sum+=add

    #print(r1)

print(sum)
file.close()