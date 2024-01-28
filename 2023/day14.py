# 2023 day 14: tilted reflector dish / moving rocks

# create grid, access tile (x,y) as grid[y][x]
grid=[]
file = open("day14.txt")
for line in file:
    grid.append(line.strip())
file.close()

dimx=len(grid[0])
dimy=len(grid)
max_load=dimy

total=0
for x in range(dimx):
    y_free=-1
    for y in range(dimy):
        cell = grid[y][x]
        if cell=='O':
            if y_free>=0:
                # roll to y_free
                load=max_load-y_free
                y_free+=1
            else:
                load=max_load-y
            total+=load
        elif cell=='.':
            if y_free<0:
                # mark free slot
                y_free=y
        elif cell=='#':
            # reset free slot
            y_free=-1

print(total)