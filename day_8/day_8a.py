"""
Tested using:
    python3 version 3.9.6


Plan of attack:
    1) For each frequency, identify all instances.
    2) For each frequency, identify all pairs of instances.
    3) For each pair, identify the indexes of the two antinodes.
    4) Count the number of antinodes which do not lie out of bounds




"""

input_string_name = "./day_8/day_8_input.txt"
# input_string_name = "./day_8/day_8_input_test.txt"


# First read the contents of the input file into a list.

# input_file is type "file"
input_file = open(input_string_name, "r")

# input_string is type "string"
input_string = input_file.read()

# input_list is type "list"
input_list = input_string.replace('\n', ';').split(";")


# mat is a list of lists
mat = [list(row) for row in input_list]




# (1) For each frequency, identify all instances.

dict_of_frequencies = {}

for r in range(len(mat)):
    for c in range(len(mat[r])):
        if mat[r][c] != ".":
            dict_of_frequencies.setdefault(mat[r][c], []).append([r,c])


# (2) For each frequency, identify all pairs of instances.

pairs = []

for frequency in dict_of_frequencies:
    for i in range(len(dict_of_frequencies[frequency])):
        for j in range(i+1, len(dict_of_frequencies[frequency])):
            pairs.append([dict_of_frequencies[frequency][i],dict_of_frequencies[frequency][j]])


# (3) For each pair, identify the indexes of the two antinodes.

diffs = []


for pair in pairs:
    diffs.append([pair[0][0] - pair[1][0], pair[0][1] - pair[1][1]])



antinodes = []

for k in range(len(diffs)):
    antinodes.append([pairs[k][0][0] + diffs[k][0], pairs[k][0][1] + diffs[k][1]])
    antinodes.append([pairs[k][1][0] - diffs[k][0], pairs[k][1][1] - diffs[k][1]])




# (4) Count the number of antinodes which do not lie out of bounds

antinode_count = 0

# Remove duplciates from our list of antinodes:
antinodes_deduplicated = []
for antinode in antinodes:
    if antinode not in antinodes_deduplicated:
        antinodes_deduplicated.append(antinode)



for x in antinodes_deduplicated:
    if x[0] in range(len(mat)) and x[1] in range(len(mat[1])):
        antinode_count += 1



print(antinode_count)

pass
