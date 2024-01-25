import re
from itertools import product


def test_arrangement(test, nums):
    ok=True
    i=0
    for match in re.finditer("[#]+", test):
        if i >= len(nums): # too many matches
            ok=False
            break
        if len(match[0])!=nums[i]:
            ok=False
            break
        i+=1
    if i!=len(nums):
        ok=False

    return ok


def create_candidates(broken):
    candidates=[]
    q=broken.count('?')

    for letters in product('.#', repeat = q):
        arr = list(letters)
        cand = "".join( arr.pop() if broken[x]=='?' else broken[x] for x in range(len(broken)) )
        candidates.append(cand)

    return candidates


total=0

file = open("day12.txt")
for line in file:
    springs, nums = line.split()
    nums = list(map(lambda x:int(x), nums.split(',') ))

    # each unknown (?) spring can be operational (.) or damaged (#)
    # create variations and match pattern / runlength encoding
    arrangements=0

    for test in create_candidates(springs):
        if test_arrangement(test, nums):
            # print(test)
            arrangements+=1

    # print(springs, arrangements)
    total+=arrangements
file.close()

print(total)