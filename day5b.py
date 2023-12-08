import re

# Opening file
file = open('day5.txt', 'r')
total = 0

to_int = lambda a : int(a)
seeds=[]
mappings=[]

x=list(range(0, 3))

def resolve_destination(source, mapping):
    if mapping.get(source):
        return mapping[source][0]
    # find keys below+above source
    below=-1
    above=-1
    for key in mapping.keys():
        if key<source:
            below=key
        if key>source:
            above=key
            break
    # print(below, above)
    
    if below >= 0:
        # check if source is within range
        if source <= below + mapping[below][1]:
            # return destination with offset
            return mapping[below][0] + source-below
    # default noop
    return source

# init map
for line in file:
    if line.startswith("seeds: "):
        seeds=list(map(to_int, re.findall("\d+", line)))
    elif line.endswith(" map:\n"):
        # init new mapping
        conv={}
        mappings.append({'name': line, 'map': conv})
    else:
        # add mapping: source -> destination, range
        # 50 98 2
        # file has destination range start of 50, a source range start of 98, and a range length
        values=list(map(to_int, re.findall("\d+", line)))
        if len(values)==3:
            conv[values[1]]=[values[0], values[2]]
file.close()

print("initialized mappings:", len(mappings))
# sort maps by key
# since Python 3.7, dictionaries preserve insertion order!
for item in mappings:
    item["map"]=dict(sorted(item["map"].items()))

destination=resolve_destination(0, mappings[0]["map"])
print(destination)
destination=resolve_destination(50, mappings[0]["map"])
print(destination)
destination=resolve_destination(79, mappings[0]["map"])
print(destination)
destination=resolve_destination(98, mappings[0]["map"])
print(destination)

def resolve_location(seed, mappings):
    number=seed
    for item in mappings:
        destination=resolve_destination(number, item["map"])
        # msg="{} {}->{}"
        # print(msg.format(item["name"], number, destination))
        number=destination
    return number

# apply seed range
best=8375662680
best_seed=0

# 2:override seeds
# seeds=[3151642679, 224376393]
for i in range(1, len(seeds), 2):
    if i!=5:
        continue
    # seeds2=list(range(seeds[i-1], seeds[i-1]+seeds[i]))
    # seeds2=list(range(seeds[i-1], seeds[i-1]+seeds[i], 1000)) # 1:sample seeds
    seeds2=list(range(seeds[i-1], seeds[i-1]+seeds[i], 100)) # 1:sample seeds

    print("len seeds ranged: ", i, len(seeds2), seeds2[0])
    # loc = min(map(lambda x: resolve_location(x, mappings), seeds2))
    loc=best
    s2=0
    for seed in seeds2:
        temp=resolve_location(seed, mappings)
        if temp<loc:
            loc=temp
            s2=seed
    print("loc:", loc, s2)
    if loc < best:
        best=loc
        best_seed=s2
        print("best i", i)


# seed2location =dict()
# for seed in seeds:
#     t=resolve_location(seed, mappings)
#     seed2location[seed]=t
# loc=min(seed2location, key=seed2location.get)

print(best, best_seed)
