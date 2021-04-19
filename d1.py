
import aoc

data = {*map(int, aoc.get_input(1).splitlines())}

for x in data:
    for y in data:
        if (x + y == 2020):
            print(x*y)

for x in data:
    for y in data:
        for z in data:
            if (x + y + z== 2020):
                print(x*y*z)
