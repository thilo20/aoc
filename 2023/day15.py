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

steps=file.readline().split(",")
file.close()

for step in steps:
    total+=hashcode(step)

print(total)