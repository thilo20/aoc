import re

total=0
hail=[] # store hail (px py pz vx vy vz)
rock=(24, 13, 10, -3, 1, 2)

# Opening file
file = open('day24-test.txt', 'r')
for line in file:
    hail.append(tuple(map(lambda x: int(x), re.findall('[-\d]+', line))))
file.close()

# test area
# min=7
# max=27
# min=200000000000000
# max=400000000000000

# compare hail stones with rock
for i in range(len(hail)):
        s1=hail[i]
        s2=rock
        a=s1[0]
        b=s1[3]
        c=s1[1]
        d=s1[4]
        e=s2[0]
        f=s2[3]
        g=s2[1]
        h=s2[4]

        div = d*f-b*h
        if div != 0:
            u = a*d-e*d+b*g-b*c
            u /= div
            # calc intersection point
            x = e + f*u
            y = g + h*u
            # is (x,y) inside test area?
            # if min<x<max and min<y<max:

            # check hail forward direction
            if u>=0:
                t = g-c+h*u
                t /= d
                if t>=0:
                    total += 1
                    msg="time:{} position:({},{})"
                    print(msg.format(u, x, y))

print(total)