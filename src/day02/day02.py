from intcode.intcode import run_intcode_program


def solve_part_one(input_list):
    result = run_intcode_program(input_list)
    return result[0]

def solve_part_two(input_list):
    result_part_two = 0
    for i in range(99):
        for j in range(99):
            test_memory = input_list.copy()
            test_memory[1] = i
            test_memory[2] = j
            result = run_intcode_program(test_memory)
            if result[0] == 19690720:
                result_part_two = 100 * i + j

    return result_part_two

file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

input_list = []

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    input_split = input_line.split(",")
    for inp in input_split:
        input_list.append(int(inp))
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(input_list.copy())))

print("TASK 2 - sol: {}".format(solve_part_two(input_list.copy())))
# validate:
# TASK 1 - sol: 3516593
# TASK 2 - sol: 7749
