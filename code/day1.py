import pathlib

def calculate_calories():
    with open(pathlib.Path(__file__).parent.joinpath("../files/day1.txt")) as file:
        input =  file.read()

    elfes = [0]

    for line in iter(input.splitlines()):
        if line.strip() == "":
            elfes.append(0)
        else:
            elfes[len(elfes)-1] += int(line)
    return elfes

def part1():
    elfes = calculate_calories()
    print("Part 1: ", max(elfes))

def part2():
    elfes = calculate_calories()
    elfes.sort()
    print("Part 2: ", elfes.pop() + elfes.pop() + elfes.pop())

part1()
part2()