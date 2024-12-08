"""
Tested using:
    python3 version 3.9.6


Plan of attack:
    1) Find the guard's starting position.
    2) For each iteration of walking loop, determine if stepping or turning
    3) If stepping, increment the count. If turning, keep track of direction facing.
    4) After reaching out of bounds, tally up the count total.




"""

# input_string_name = "./day_6/day_6_input.txt"
input_string_name = "./day_6/day_6_input_test.txt"


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

guard_direction = [-1,0]    # Guard always starts facing up
step_count = 1              # Starting position is included in step_count

while True:

    # Identify target coordinates for upcoming step

    # Determine if target coordinates contain a barrier

    # If barrier, turn right (update guard_direction)

    # If empty, step forward (update guard_position) and increment step_count.






pass
