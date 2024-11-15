def generate_points(path):
    points = []
    current_x = 0
    current_y = 0
    time = 0
    points.append((current_x, current_y, time))
    for instruction in path:
        if instruction.startswith("R"):
            distance = int(instruction[1:])
            for i in range(distance):
                current_x += 1
                time += 1
                points.append((current_x, current_y, time))
        if instruction.startswith("L"):
            distance = int(instruction[1:])
            for i in range(distance):
                current_x -= 1
                time += 1
                points.append((current_x, current_y, time))
        if instruction.startswith("U"):
            distance = int(instruction[1:])
            for i in range(distance):
                current_y += 1
                time += 1
                points.append((current_x, current_y, time))

        if instruction.startswith("D"):
            distance = int(instruction[1:])
            for i in range(distance):
                current_y -= 1
                time += 1
                points.append((current_x, current_y, time))

    return points

def solve_part_one(paths_list):
    min_distance = 999999999
    raw_points_1 = generate_points(paths_list[0])
    raw_points_2 = generate_points(paths_list[1])
    points_1 = set([(x[0], x[1]) for x in raw_points_1])
    points_2 = set([(x[0], x[1]) for x in raw_points_2])
    cut = points_1.intersection(points_2)
    for point in cut:
        if point != (0,0):
            min_distance = min(abs(point[0]) + abs(point[1]), min_distance )
    return min_distance

def solve_part_two(paths_list):
    min_distance = 999999999
    raw_points_1 = generate_points(paths_list[0])
    raw_points_2 = generate_points(paths_list[1])
    points_1 = set([(x[0], x[1]) for x in raw_points_1])
    points_2 = set([(x[0], x[1]) for x in raw_points_2])
    cut = points_1.intersection(points_2)
    for point in cut:
        if point != (0,0):
            min_time_1 = 99999999
            min_time_2 = 99999999
            for point_1 in raw_points_1:
                if point_1[0] == point[0] and point_1[1] == point[1]:
                    min_time_1 = min(min_time_1, point_1[2])
            for point_2 in raw_points_2:
                if point_2[0] == point[0] and point_2[1] == point[1]:
                    min_time_2 = min(min_time_2, point_2[2])

            min_distance = min(min_time_1 + min_time_2, min_distance )
    return min_distance

# def solve_part_one(paths_list):
#     min_distance = 999999999
#     points_1 = generate_points(paths_list[0])
#     points_2 = generate_points(paths_list[1])
#     for point in points_1:
#         for point2 in points_2:
#             if point == point2:
#                 if point != (0,0):
#                     min_distance = min(abs(point[0]) + abs(point[1]), min_distance )
#     return min_distance


file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0
paths = []

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    paths.append(input_line.split(","))
    count += 1

print("TASK 1 - sol: {}".format(solve_part_one(paths)))

print("TASK 2 - sol: {}".format(solve_part_two(paths)))
