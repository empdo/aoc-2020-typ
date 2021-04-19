import aoc
import re

j = 0
alve = 0
alve2 = 0

data = aoc.get_input(2).splitlines()

for x in data:
    firstNumber, secondNumber, letter, _, passw = re.split(r"[- :]", x)
    for i in passw:
        j +=1
        if (j == int(firstNumber)):
            if (i == letter):
                alve += 1
        if (j == int(secondNumber)):
            if (i == letter):
                alve += 1
    if (alve == 1):
        alve2 += 1
    j = 0
    alve = 0
print(alve2)

