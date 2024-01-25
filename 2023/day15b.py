import re

def hashcode(step):
    val=0
    for char in step:
        val+=ord(char)
        val*=17
        val%=256
    return val

# Opening file
file = open('day15.txt', 'r')

total=0

steps=re.findall("(\w+)([-=])(\d+)?", file.readline())
file.close()

boxes=dict()

for step in steps:
    no=hashcode(step[0])
    if boxes.get(no) is None:
        boxes[no]={}
    if step[1]=="=":
        boxes[no][step[0]]=int(step[2])
    if step[1]=="-" and boxes[no].get(step[0]) is not None:
        boxes[no].pop(step[0])

for box in boxes:
    slot=1
    for lense in boxes[box].values():
        total += (box+1)*slot*lense
        slot+=1
print(total)