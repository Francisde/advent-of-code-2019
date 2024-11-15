def run_intcode_program(memory):
    instruction_pointer = 0
    halt = False
    while not halt:
        opcode = memory[instruction_pointer]
        if opcode == 1:
            value1_index = memory[instruction_pointer + 1]
            value2_index = memory[instruction_pointer + 2]
            dest_index = memory[instruction_pointer + 3]
            if max(value1_index, value2_index, dest_index) >= len(memory):
                print("error")
                break
            result = memory[value1_index] + memory[value2_index]
            memory[dest_index] = result
        elif opcode == 2:

            value1_index = memory[instruction_pointer + 1]
            value2_index = memory[instruction_pointer + 2]
            dest_index = memory[instruction_pointer + 3]
            if max(value1_index, value2_index, dest_index) >= len(memory):
                print("error")
                break
            result = memory[value1_index] * memory[value2_index]
            memory[dest_index] = result
        elif opcode == 99:
            halt = True
        else:
            print("error")
        instruction_pointer += 4
    return memory

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
