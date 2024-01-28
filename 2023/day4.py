import re

# Opening file
file = open('day4.txt', 'r')
sum = 0

# init map
for line in file:
    parts=re.split(":|\|", line)
    cards = set()
    for card in re.findall("\d+", parts[1]):
        cards.add(int(card))
    
    hits=0
    for card in re.findall("\d+", parts[2]):
        if int(card) in cards:
            hits+=1

    if hits >0:
        sum += pow(2, hits-1)
print(sum)
file.close()
