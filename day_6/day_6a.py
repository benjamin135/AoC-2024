"""
Tested using:
    python3 version 3.9.6


Plan of attack:
    1) Find the guard's starting position.
    2) For each iteration of walking loop, determine if stepping or turning
    3) If stepping, increment the count. If turning, keep track of direction facing.
    4) After reaching out of bounds, tally up the count total.




"""

input_string_name = "./day_6/day_6_input.txt"
# input_string_name = "./day_6/day_6_input_test.txt"


# First read the contents of the input file into a list.

# input_file is type "file"
input_file = open(input_string_name, "r")

# input_string is type "string"
input_string = input_file.read()

# input_list is type "list"
input_list = input_string.replace('\n', ';').split(";")


# mat is a list of lists
mat = [list(row) for row in input_list]


# (1) Find the guard's starting position.
break_flag = False
for r in range(len(mat)):
    for c in range(len(mat[r])):
        if mat[r][c] == "^":
            guard_position = [r,c]
            break_flag = True
            break
    if break_flag is True:
        break

compass = {
    0: [-1,0],  # Facing up
    1: [0,1],  # Facing right
    2: [1,0],  # Facing down
    3: [0,-1]   # Facing left
}

guard_turn_counter = 0
guard_direction = compass[0]    # Guard always starts facing up
visited_positions = [guard_position]    # Starting position is included in step_count


while True:

    # Identify target coordinates for upcoming step
    upcoming_position = [guard_position[0] + guard_direction[0], guard_position[1] + guard_direction[1]]
    
    # Determine if upcoming position is out of bounds. Exit loop if so.
    if upcoming_position[0] not in range(len(mat)) or upcoming_position[1] not in range(len(mat[0])):
        # Upcoming position is out of bounds.
        break

    # Upcoming position is not out of bounds.
    # Determine if upcoming position contains a barrier
    if mat[upcoming_position[0]][upcoming_position[1]] == "#":
        # Upcoming position contains a barrier!
        # Guard needs to turn right, and step_count does not increment.
        guard_turn_counter += 1
        guard_direction = compass[guard_turn_counter % 4]

    else:
        # Upcoming position is open.
        # Move guard forward and increment step_count
        guard_position = upcoming_position
        if guard_position not in visited_positions:
            visited_positions.append(guard_position)


count_of_visited_positions = len(visited_positions)
print(count_of_visited_positions)


pass
