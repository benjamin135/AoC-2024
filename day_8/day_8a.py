"""
Tested using:
    python3 version 3.9.6


Plan of attack:
    1) Identify list of all frequencies.
    2) For each frequency, identify all instances.
    3) For each frequency, identify all pairs of instances.
    4) For each pair, identify the indexes of the two antinodes.
    5) For each antinode, confirm that it doesn't lie out of bounds (disregard it otherwise).
    6) Count all antinodes which have not been disregarded.




"""

# input_string_name = "./day_8/day_8_input.txt"
input_string_name = "./day_8/day_8_input_test.txt"


# First read the contents of the input file into a list.

# input_file is type "file"
input_file = open(input_string_name, "r")

# input_string is type "string"
input_string = input_file.read()

# input_list is type "list"
input_list = input_string.replace('\n', ';').split(";")


# mat is a list of lists
mat = [list(row) for row in input_list]







pass


