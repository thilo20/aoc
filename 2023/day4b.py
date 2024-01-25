import re

# Opening file
file = open('day4.txt', 'r')
total = 0

deck = {}

def add_cards(deck, number, copies):
    if deck.get(number) is None:
        deck[number]=copies
    else:
        deck[number]+=copies

# init map
for line in file:
    parts=re.split(":|\|", line)

    number=int(re.search("Card[ ]+(\d+)", parts[0]).group(1))
    add_cards(deck, number, 1)

    cards = set()
    for card in re.findall("\d+", parts[1]):
        cards.add(int(card))
    
    hits=0
    for card in re.findall("\d+", parts[2]):
        if int(card) in cards:
            hits+=1
            add_cards(deck, number+hits, deck[number])


total = sum(deck.values())
print(total)
file.close()
