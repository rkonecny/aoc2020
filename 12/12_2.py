import numpy as np

with open('input', "r") as fo:
    list = fo.readlines()

for i in range(len(list)):
    list[i] = list[i].replace("\n", "")


navigationList = [(x[0], int(x[1:])) for x in list]
directions = ['E', 'S', 'W', 'N']
direction = 'E'
shipEastSouth = [0, 0]
waypointEastSouth = [10, -1]


def moveShip(times):
    shipEastSouth[0] += waypointEastSouth[0] * times
    shipEastSouth[1] += waypointEastSouth[1] * times


def rotateWaypoint(input):
    degrees = input[1] if input[0] == 'R' else 360-input[1]
    theta = np.radians(degrees)

    rotationMatrix = np.array(((np.cos(theta), -np.sin(theta)),
                               (np.sin(theta),  np.cos(theta))))

    waypoint = np.array((waypointEastSouth[0], waypointEastSouth[1]))
    rotation = rotationMatrix.dot(waypoint)

    waypointEastSouth[0] = round(rotation[0])
    waypointEastSouth[1] = round(rotation[1])


def moveWaypoint(input):
    if input[0] == 'E':
        waypointEastSouth[0] += input[1]
        return
    if input[0] == 'W':
        waypointEastSouth[0] -= input[1]
        return
    if input[0] == 'S':
        waypointEastSouth[1] += input[1]
        return
    if input[0] == 'N':
        waypointEastSouth[1] -= input[1]
        return

    rotateWaypoint(input)


def move(input):
    if input[0] == 'F':
        moveShip(input[1])
        return
    moveWaypoint(input)


for i in navigationList:
    move(i)

print(shipEastSouth)
print(abs(shipEastSouth[0]) + abs(shipEastSouth[1]))
