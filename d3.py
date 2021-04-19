from aoc import get_input

data = get_input(3).splitlines()

tree_count = 0
x = 0

for line in data:
    if line[x % len(line)] == "#":
        tree_count += 1
    x += 3

def function(slopex, slopey):
    x=0
    y=0
    function_tree_count = 0
    while y < len(data):
        if data[y][x % len(data[y])] == "#":
            function_tree_count += 1
        x += slopex
        y += slopey
    return function_tree_count
    
tree_count = 1
for i in range(1, 6):
    tree_count *= function(1 if i == 5 else ((i * 2) - 1), (2 if i == 5 else 1))

print(tree_count)
