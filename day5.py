import re

# Opening file
file = open('day5-test.txt', 'r')
total = 0

d = {320: 1, 321: 0, 322: 3}
x=min(d, key=d.get)

to_int = lambda a : int(a)
seeds=[]
mappings=[]

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
    print(below, above)
    
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
        msg="{} {}->{}"
        print(msg.format(item["name"], number, destination))
        number=destination
    return number

# seed2location =dict()
# for seed in seeds:
#     t=resolve_location(seed, mappings)
#     seed2location[seed]=t
# loc=min(seed2location, key=seed2location.get)
loc = min(map(lambda x: resolve_location(x, mappings), seeds))

print(loc)
