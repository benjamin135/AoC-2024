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


# ktest1 = list_of_lists[0][0]
# test2 = list_of_lists[1][1]
# test3 = list_of_lists[1][0]
# test4 = list_of_lists[0][1]
# test5 = list_of_lists[4][4]

xmas_count = 0
xmas_list = []

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == "X":

            # Now do 8 individual cases:

            # Horizontal forwards
            try:
                if mat[i][j+1] == "M" and mat[i][j+2] == "A" and mat[i][j+3] == "S":
                    xmas_count += 1
                    xmas_list.append(str(i)+","+str(j)+" "+"horizontal-forward")
            except IndexError:
                pass
            
            # Horizontal backwards
            try:
                if mat[i][j-1] == "M" and mat[i][j-2] == "A" and mat[i][j-3] == "S" and j-3 >= 0:
                    xmas_count += 1
                    xmas_list.append(str(i)+","+str(j)+" "+"horizontal-backwards")
            except IndexError:
                pass

            # Vertical downwards
            try:
                if mat[i+1][j] == "M" and mat[i+2][j] == "A" and mat[i+3][j] == "S":
                    xmas_count += 1
                    xmas_list.append(str(i)+","+str(j)+" "+"vertical-downwards")
            except IndexError:
                pass

            # Vertical upwards
            try:
                if mat[i-1][j] == "M" and mat[i-2][j] == "A" and mat[i-3][j] == "S" and i-3 >= 0:
                    xmas_count += 1
                    xmas_list.append(str(i)+","+str(j)+" "+"vertical-upwards")
            except IndexError:
                pass

            # Diagonal down-right
            try:
                if mat[i+1][j+1] == "M" and mat[i+2][j+2] == "A" and mat[i+3][j+3] == "S":
                    xmas_count += 1
                    xmas_list.append(str(i)+","+str(j)+" "+"diagonal-down-right")
            except IndexError:
                pass

            # Diagonal up-right
            try:
                if mat[i-1][j+1] == "M" and mat[i-2][j+2] == "A" and mat[i-3][j+3] == "S"  and i-3 >= 0:
                    xmas_count += 1
                    xmas_list.append(str(i)+","+str(j)+" "+"diagonal-up-right")
            except IndexError:
                pass

            # Diagonal down-left
            try:
                if mat[i+1][j-1] == "M" and mat[i+2][j-2] == "A" and mat[i+3][j-3] == "S" and j-3 >= 0:
                    xmas_count += 1
                    xmas_list.append(str(i)+","+str(j)+" "+"diagonal-down-left")
            except IndexError:
                pass

            # Diagonal up-left
            try:
                if mat[i-1][j-1] == "M" and mat[i-2][j-2] == "A" and mat[i-3][j-3] == "S" and i-3 >= 0 and j-3 >= 0:
                    xmas_count += 1
                    xmas_list.append(str(i)+","+str(j)+" "+"diagonal-up-left")
            except IndexError:
                pass

pass