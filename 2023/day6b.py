import re

file = open("day6.txt")
times= list(map(lambda x:int(x), re.findall("\d+", file.readline().replace(" ", ""))))
records= list(map(lambda x:int(x), re.findall("\d+", file.readline().replace(" ", ""))))
file.close()

total=1
for race in range(len(times)):
    wins =1
    # determine first t1 to beat the record: via sampling
    t_race=times[race]
    for t1 in range(1,t_race):
        s=t1*(t_race-t1)
        if s > records[race]:
            wins = t_race - 2*t1 + 1
            break
    total*=wins

print(total)