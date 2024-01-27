# Original list of numbers
numbers = [1, 2, 3, 4, 5]

# List comprehension to create a list of squares
squares = [number ** 2 for number in numbers]
print(squares)

# Filtering lines where Romeo speaks
lines = ["ROMEO: loves JUOEIT", "ROMEO: works at cafe", "JULIET: likes ROMEO"]
romeo_lines = [line for line in lines if line.startswith("ROMEO:")]
print(romeo_lines)

# Replacing "ROMEO" with "BUD" in each line
modified_lines = [line.replace("ROMEO:", "BUD:") for line in romeo_lines]
print(modified_lines)

# Creating a list of the lengths of Romeo's lines
line_lengths = [len(line) for line in romeo_lines]
print(line_lengths)