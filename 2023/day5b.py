import re

# Opening file
file = open('day5.txt', 'r')
total = 0

to_int = lambda a : int(a)
seeds=[]
mappings=[]

def resolve_source(source, mapping):
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
        if source < below + mapping[below][1]:
            # return destination with offset
            return mapping[below][0] + source-below
    # default noop
    return source

def in_range(source, mapping):
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
        if source < below + mapping[below]:
            return True
    return False


# init map
for line in file:
    if line.startswith("seeds: "):
        seeds=list(map(to_int, re.findall("\d+", line)))
    elif line.endswith(" map:\n"):
        # init new mapping
        conv={}
        mappings.append({'name': line, 'map': conv})
    else:
        # add mapping: destination -> source, range
        # 50 98 2
        # The first line has a destination range start of 50, a source range start of 98, and a range length of 2
        values=list(map(to_int, re.findall("\d+", line)))
        if len(values)==3:
            conv[values[0]]=[values[1], values[2]]
file.close()

print("initialized mappings:", len(mappings))
# sort maps by key
# since Python 3.7, dictionaries preserve insertion order!
for item in mappings:
    item["map"]=dict(sorted(item["map"].items()))

# init map for ranges of seeds
seedranges={}
for i in range(0,len(seeds)//2,1):
    seedranges[seeds[2*i]]=seeds[2*i+1]
seedranges=dict(sorted(seedranges.items()))

source=resolve_source(0, mappings[0]["map"])
print(source)
source=resolve_source(50, mappings[0]["map"])
print(source)
source=resolve_source(79, mappings[0]["map"])
print(source)
source=resolve_source(98, mappings[0]["map"])
print(source)
source=resolve_source(100, mappings[0]["map"])
print(source)

msg="Seed number {} corresponds to soil number {}."
print(msg.format(resolve_source(81, mappings[0]["map"]), 81))
print(msg.format(resolve_source(14, mappings[0]["map"]), 14))
print(msg.format(resolve_source(57, mappings[0]["map"]), 57))
print(msg.format(resolve_source(13, mappings[0]["map"]), 13))


def resolve_seed(location, mappings):
    number=location
    for item in reversed(mappings):
        source=resolve_source(number, item["map"])
        # msg="{} {}->{}"
        # print(msg.format(item["name"], number, source))
        number=source
    return number

resolve_seed(35, mappings)

loc=0
while True:
    seed=resolve_seed(loc, mappings)
    if in_range(seed, seedranges): break
    loc+=1

print(loc)
