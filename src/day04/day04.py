def solve_part_one(lower, upper):
    result = []
    for number in range(lower, upper + 1):
        if has_same_adjacent_digits(number):
            if number_increase(number):
                result.append(number)
    return len(result)

def solve_part_two(lower, upper):
    result = []
    for number in range(lower, upper + 1):
        if has_same_adjacent_digits(number):
            if number_increase(number):
                if has_same_exact_adjacent_digits(number):
                    result.append(number)
    return len(result)

def has_same_adjacent_digits(number):
    for index in range(1, len(str(number))):
        if str(number)[index - 1] == str(number)[index]:
            return True
    return False

def has_same_exact_adjacent_digits(number):
    for index in range(1, len(str(number))):
        if str(number)[index - 1] == str(number)[index]:
            if index - 2 >= 0 and index + 1 < len(str(number)):
                # middle case
                if str(number)[index - 2] != str(number)[index] and str(number)[index + 1] != str(number)[index]:
                    return True
            if index - 2 < 0:
                # left edge case
                if str(number)[index + 1] != str(number)[index]:
                    return True
            if index + 1 >= len(str(number)):
                # right edge case
                if str(number)[index - 2] != str(number)[index]:
                    return True
    return False

def number_increase(number):
    str_number = str(number)
    increase = True
    for index in range(1, len(str_number)):
        if int(str_number[index - 1]) < int(str_number[index]):
            increase = False
    return increase



lower_bound = 231832
upper_bound = 767346

print("TASK 1 - sol: {}".format(solve_part_one(lower_bound, upper_bound)))

print("TASK 2 - sol: {}".format(solve_part_two(lower_bound, upper_bound)))
