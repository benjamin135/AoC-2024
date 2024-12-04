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



# First read the contents of the input file into a list.

# input_file is type "file"
input_file = open("day_1_input.txt", "r")

# input_string is type "string"
input_string = input_file.read()

# input_list is type "list"
input_list = input_string.replace('\n', '.').split(".")


# Initialize empty lists
left_numbers = []
right_numbers = []

# Process the list
for row in input_list:
    left, right = row.split('   ')  # Split by three spaces
    left_numbers.append(int(left))  # Append to the left numbers list
    right_numbers.append(int(right))  # Append to the right numbers list


left_numbers.sort()
right_numbers.sort()


diffs = [abs(value1 - value2) for index1, value1 in enumerate(left_numbers) for index2, value2 in enumerate(right_numbers) if index1 == index2]

answer = sum(diffs)

pass

similarity_score = 0

for left_item in left_numbers:
    frequency = 0
    for right_item in right_numbers:
        if left_item == right_item:
            frequency += 1
    similarity_score += frequency * left_item
        
print(similarity_score)
pass