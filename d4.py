from aoc import get_input

data = get_input(4).splitlines()

cool_list = [" "]
second_cool_list = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]

for line in data:
    if line != '':
        cool_list[len(cool_list) -1] = cool_list[len(cool_list) -1] + line
    else:
        cool_list.append(line)

print(len(cool_list))

for i, line in enumerate(cool_list):
    for word in second_cool_list: 
        if word not in line:
            cool_list.pop(i)

print(len(cool_list))


#dela in varje passport i en lista, kolla om varje lista inehåller följande greher sen skjuta mig själv
