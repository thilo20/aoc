import re

file = open("day6.txt")
times= list(map(lambda x:int(x), re.findall("\d+", file.readline().replace(" ", ""))))
records= list(map(lambda x:int(x), re.findall("\d+", file.readline().replace(" ", ""))))
file.close()

total=1
for race in range(len(times)):
    wins =0
    # determine first t1 to beat the record: via sampling
    t_race=times[race]
    for t1 in range(1,t_race):
        s=t1*(t_race-t1)
        if s > records[race]:
            wins += 1
    total*=wins

print(total)

# runtime comparison:
#
# thilo@Thilos-MBP aoc2023 % time python3 day6b.py
# 40087680
# python3 day6b.py  0.89s user 0.01s system 99% cpu 0.899 total
# thilo@Thilos-MBP aoc2023 % time python3 day6bNadine.py 
# 40087680
# python3 day6bNadine.py  10.39s user 0.01s system 99% cpu 10.405 total
# thilo@Thilos-MBP aoc2023 % 