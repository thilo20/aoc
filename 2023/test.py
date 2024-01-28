from shapely.geometry import Polygon, Point

x=[0, 1, 1, 0, 0]
y=[0, 0, 1, 1, 1]
pgon = Polygon(zip(x, y)) # Assuming the OP's x,y coordinates

print(pgon.area)
f=pgon.contains(Point(2,0))
t=pgon.contains(Point(0.5,0.5))

thislist = ["apple", "banana", "cherry"]
{print(x) for x in thislist}
