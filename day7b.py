import re

# Opening file
file = open('day7.txt', 'r')
total = 0

def getType(hand):
    a={}
    for c in hand:
        if a.get(c) is None:
            a[c]=1
        else:
            a[c]=a[c]+1

    # jokers
    j=0
    if a.get('J') and len(a)>1: 
        j=a.pop("J")
        b=max(a, key=a.get)
        a[b] += j

    match len(a):
        case 1: return 1
        case 4: return 6
        case 5: return 7
        case 2: 
            if 4 in a.values():
                return 2
            else:
                return 3
        case 3:
            if 3 in a.values():
                return 4
            else:
                return 5
    return None

def strength(a):
    # order highest=A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J=lowest
    match a:
        case 'A': return 14
        case 'K': return 13
        case 'Q': return 12
        case 'J': return  1
        case 'T': return 10
        case '9': return  9
        case '8': return  8
        case '7': return  7
        case '6': return  6
        case '5': return  5
        case '4': return  4
        case '3': return  3
        case '2': return  2
    return 0

def hashcode(hand):
    sum=0
    for a in hand:
        sum = sum*14 +strength(a)
    return sum

# hold hands and bids
input=list()
for line in file:
    r1=re.match("([\w\d]+) (\d+)", line)
    input.append( {'hand':r1.group(1), 'bid':int(r1.group(2))} )
file.close()

# sort by type
b=getType('AAAAA') # 1 5     -> 1
b=getType('AAAAK') # 2 4,1   -> 2
b=getType('AAAKK') # 2 3,2   -> 3
b=getType('AAAKQ') # 3 3,1,1 -> 4
b=getType('AAKKQ') # 3 2,2,1 -> 5
b=getType('AAKQJ') # 4       -> 6
b=getType('AKQJT') # 5       -> 7
# b=getType('AAKQJ')

input2=sorted(input, key=lambda x:hashcode(x['hand'])) # sort on secondary key
input2=sorted(input2, key=lambda x:getType(x['hand']), reverse=True) # sort on primary key

msg="{} {} type:{} hash:{}"
# calc winnings
for i in range(len(input2)):
    h=input2[i]
    print(msg.format(h['hand'], h['bid'], getType(h['hand']), hashcode(h['hand'])))
    total += (i+1)* input2[i]['bid']

print(total)
