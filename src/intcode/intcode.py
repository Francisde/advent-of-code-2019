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