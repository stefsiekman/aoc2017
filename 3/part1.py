visited = {}
location = (0,0)
direction = 0

n = 289326

def neighbours(l):
    return {
        0: (l[0] + 1, l[1]    ),
        1: (l[0]    , l[1] + 1),
        2: (l[0] - 1, l[1]    ),
        3: (l[0]    , l[1] - 1)
    }

def sumAround(l):
    r = [-1,0,1]
    s = sum([visited[(l[0]+i,l[1]+j)] for i in r for j in r if (i != 0 or j != 0) and (l[0]+i,l[1]+j) in visited])

    if s > 0:
        return s
    else:
        return 1

for i in range(2, n + 1):
    # Visit current
    s = sumAround(location)
    if s > n:
        print(s)
        exit()
    visited[location] = s

    # Travel in direction
    location = neighbours(location)[direction]

    # Can we turn left?
    locationToLeft = neighbours(location)[(direction + 1) % 4]

    if not locationToLeft in visited:
        direction = (direction + 1) % 4

print(f"{n} is at {abs(location[0]) + abs(location[1])}")
