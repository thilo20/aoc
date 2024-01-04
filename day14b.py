# disclaimer: This file is a commented version of https://github.com/Domyy95/Challenges/blob/master/2023-12-Advent-of-code/14.py
# my comments are '#!' 

CYCLES = 1000000000

with open("day14.txt", "r") as file:
    input = tuple(file.read().splitlines())
#! just 2 lines to read data, I use 5

def slide_rocks_north(grid):
    # transpose
    grid = list(map("".join, zip(*grid))) #! use zip to get a column view
    new_grid = []

    for row in grid: #! operate on strings
        ordered_rows = []
        for group in row.split("#"): #! use fixed rocks (#) as movement separator
            ordered_rows.append("".join(sorted(group, reverse=True))) #! use sort to move rocks :)

        new_grid.append("#".join(ordered_rows)) #! use join to aggregate sorted sections
        #! nice: multiple separators get preserved, ordered_rows will contain "" (empty strings)

    return list(map("".join, zip(*new_grid))) #! transpose again (undo)


def print_grid(grid):
    for row in grid:
        print(row)
    print()


# 1 cycle = move rocks north, west, south, east
def cycle(grid):
    for _ in range(4):
        grid = slide_rocks_north(grid)
        # rotate 90 degrees
        grid = tuple(["".join(row[::-1]) for row in zip(*grid)]) #! note similarity to transpose, tweaked to reverse row items

    return grid


solution1 = 0
solution2 = 0

grid_slided = slide_rocks_north(input)
# print_grid(grid_slided)
solution1 = sum(
    row.count("O") * (len(grid_slided) - i) for i, row in enumerate(grid_slided)
    #! wow statement!
    # 1. enumerate() provides both index and value
    # 2. count() gives mass (rocks in whole row)
    # 3. len-i gives weight factor (lever)
    # 4. short hand for loop style, based on List Comprehension
    # debug line with locals and watches :)
)

print("Solution 1:", solution1)
# uncomment for sol.1 time comparison
# exit()

# seen = {input} #! set, unordered and unique
seen_list = [input] #! list, ordered

grid_cycle = input
for i in range(CYCLES):
    grid_cycle = cycle(grid_cycle)
    # print_grid(grid_cycle)

    if grid_cycle in seen_list:
        break
    # seen.add(grid_cycle)
    seen_list.append(grid_cycle)

first_cycle_grid_index = seen_list.index(grid_cycle)
final_grid = seen_list[
    (CYCLES - first_cycle_grid_index) % (i + 1 - first_cycle_grid_index)
    + first_cycle_grid_index
]
#! on input: i=117, first_cycle_grid_index=96
#! 999999904 % 22 + 96 = 2 + 96 = 98
solution2 = sum(
    row.count("O") * (len(final_grid) - i) for i, row in enumerate(final_grid)
)
print("Solution 2:", solution2)

# output:
# Solution 1: 112773
# Solution 2: 98894

# timings:
# python3 day14b.py  0.53s user 0.01s system 99% cpu 0.547 total
# wow: it looks like 'transpose grid' costs nothing!

#! tuple/list conversions don't change results, timings unaffected (lists only: cpu 0.534)
