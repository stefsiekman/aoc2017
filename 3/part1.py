visited = {}
location = (0,0)
direction = "r" # l u d

n = 289326

def neighbours(l):
    return {
        "r": (l[0] + 1, l[1]    ),
        "u": (l[0]    , l[1] + 1),
        "l": (l[0] - 1, l[1]    ),
        "d": (l[0]    , l[1] - 1)
    }

def sumAround(l):
    locations = [
        (l[0] - 1, l[1] - 1),
        (l[0]    , l[1] - 1),
        (l[0] + 1, l[1] - 1),

        (l[0] - 1, l[1]    ),
        (l[0] + 1, l[1]    ),

        (l[0] - 1, l[1] + 1),
        (l[0]    , l[1] + 1),
        (l[0] + 1, l[1] + 1),
    ]

    sum = 0
    for loc in locations:
        if loc in visited:
            sum += visited[loc]

    if sum > 0:
        return sum
    else:
        return 1

for i in range(2, n + 1):
    # Visit current
    sum = sumAround(location)
    if sum > n:
        print(sum)
        exit()
    else:
        print(sum)
    visited[location] = sum

    # Travel in direction
    location = neighbours(location)[direction]

    # Can we turn left?
    toLeft = {
        "r": "u",
        "u": "l",
        "l": "d",
        "d": "r"
    }
    locationToLeft = neighbours(location)[toLeft[direction]]

    if not locationToLeft in visited:
        direction = toLeft[direction]

print(f"{n} is at {abs(location[0]) + abs(location[1])}")
