"""
Tested using:
    python3 version 3.9.6

    
PART ONE:

Plan of attack:
    1) 
        

PART TWO:

Plan of attack:
    1) 

    
"""

input_string_name = "day_4_input.txt"
# input_string_name = "day_4_input_test.txt"


# First read the contents of the input file into a list.

# input_file is type "file"
input_file = open(input_string_name, "r")

# input_string is type "string"
input_string = input_file.read()

# input_list is type "list"
input_list = input_string.replace('\n', '.').split(".")


# mat is a list of lists
mat = [list(row) for row in input_list]


xmas_count = 0

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == "A":

            # Now do 4 individual cases:


            try:
                if mat[i+1][j+1] == "M" and mat[i-1][j-1] == "S" and mat[i+1][j-1] == "M" and mat[i-1][j+1] == "S" and i-1 >= 0 and j-1 >= 0:
                    xmas_count += 1
            except IndexError:
                pass

            try:
                if mat[i+1][j+1] == "S" and mat[i-1][j-1] == "M" and mat[i+1][j-1] == "M" and mat[i-1][j+1] == "S" and i-1 >= 0 and j-1 >= 0:
                    xmas_count += 1
            except IndexError:
                pass

            try:
                if mat[i+1][j+1] == "M" and mat[i-1][j-1] == "S" and mat[i+1][j-1] == "S" and mat[i-1][j+1] == "M" and i-1 >= 0 and j-1 >= 0:
                    xmas_count += 1
            except IndexError:
                pass

            try:
                if mat[i+1][j+1] == "S" and mat[i-1][j-1] == "M" and mat[i+1][j-1] == "S" and mat[i-1][j+1] == "M" and i-1 >= 0 and j-1 >= 0:
                    xmas_count += 1
            except IndexError:
                pass

pass