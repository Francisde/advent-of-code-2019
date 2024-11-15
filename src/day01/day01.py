def solve_part_two(input_list):
    result = 0
    for mass in input_list:
        total_fuel_requirement = 0
        fuel_requirement = mass // 3
        fuel_requirement -= 2
        while fuel_requirement > 0:
            total_fuel_requirement += fuel_requirement
            fuel_requirement = fuel_requirement // 3
            fuel_requirement -= 2

        result += total_fuel_requirement
        print("mass: {}, fuel required: {}".format(mass, total_fuel_requirement))
    return result

def solve_part_one(input_list):
    result = 0
    for mass in input_list:
        fuel_requirement = mass // 3
        fuel_requirement -= 2
        result += fuel_requirement
        print("mass: {}, fuel required: {}".format(mass, fuel_requirement))
    return result


file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0
masses = []
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    masses.append(int(input_line))
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(masses)))

print("TASK 2 - sol: {}".format(solve_part_two(masses)))
