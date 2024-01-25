import re

# Opening file
file = open('day3.txt', 'r')
sum = 0

# init map
map = {}
y = 0
for line in file:
    map[y] = line
    y += 1
y_max = y-1
# access with map[y][x]

# collect numbers (value and spanned location)
numbers = {}
# access by line with numbers[y]
y = 0
for line in map:
    iter = re.finditer("\d+", map[line])
    for s in iter:
        num = {'value': int(s.group()), 'x_min': s.start(), 'x_max': s.end()}
        if numbers.get(y) is None:
            numbers[y] = [num]
        else:
            numbers[y].append(num)
    y = y+1


def get_parts(nums, s_min, s_max, parts):
    # adds up numbers that touch symbol neighborhood [min, max)
    if nums is None:
        return 0
    for num in nums:
        # test no overlap
        if num['x_max'] <= s_min:
            continue
        if num['x_min'] > s_max:
            continue
        print(num['value'])
        parts.append(num)


# iterate over * symbols only
y = 0
for line in map:
    iter = re.finditer("\*", map[line])
    for s in iter:
        x = s.start()

        print(s.group(0), y, x)
        parts=[]
        get_parts(numbers.get(y-1), x-1, x+1, parts)
        get_parts(numbers.get(y), x-1, x+1, parts)
        get_parts(numbers.get(y+1), x-1, x+1, parts)

        if len(parts)==2:
            sum += parts[0]['value']*parts[1]['value']

    # print(r1)
    y = y+1

print(sum)
file.close()
