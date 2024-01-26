import re
import numpy as np

def day03(filename):

    dat = inputlines(filename)

    part_numbers = []

    for i, x in enumerate(dat):

        # Find a symbol
        symbol_indices = [m.start() for m in re.finditer(r"[^\.\d]", x)]
        
        if len(symbol_indices) == 0:
            continue   
        
        # Look for part numbers 
        for index in symbol_indices:

            if i != 0:
                above = get_digit(dat, index, i-1)
                part_numbers.extend(above)

            if i != len(dat):
                below = get_digit(dat, index, i+1)
                part_numbers.extend(below)

            current = get_digit(dat, index, i)
            part_numbers.extend(current)

    part_numbers = list(map(int, part_numbers))

    return sum(part_numbers)


def day03b(filename):

    dat = inputlines(filename)

    results = []

    for i, x in enumerate(dat):

        # Find a * symbol
        symbol_indices = [m.start() for m in re.finditer(r"[\*]", x)]
        
        if len(symbol_indices) == 0:
            continue   
        
        # Look for part numbers 
        for index in symbol_indices:

            gear_check = []

            if i != 0:
                above = get_digit(dat, index, i-1)
                gear_check.extend(above)

            if i != len(dat):
                below = get_digit(dat, index, i+1)
                gear_check.extend(below)

            current = get_digit(dat, index, i)
            gear_check.extend(current)
        
            # A gear is a * symbol next to exactly two part numbers
            if len(gear_check) == 2:
                gear_ratio = np.prod(list(map(int, gear_check)), axis = 0)
                results.append(gear_ratio.item())

    return sum(results)



def get_digit(dat, symbol_index, row_index):
    # Look for part number in this row
    other_row = dat[row_index]
    # Look for part number in these columns
    symbol_index = set([symbol_index - 1, symbol_index, symbol_index + 1])
    
    # Find each part number and return start and end indices
    index_digits = [y.span() for y in re.finditer(r"\d+", other_row)]
    # Convert list of tuples to list of ranges
    index_digits = [set(range(*tup)) for tup in index_digits]
    # Check if `symbol_index` is in each range
    valid_digits = [len(symbol_index.intersection(z)) > 0 for z in index_digits]
    # Convert list of boolean to list of indices
    valid_digits = list(np.where(valid_digits)[0])
    # Find each part number
    digits = re.findall(r"\d+", other_row)
    # Extract part numbers that coincide with the `symbol_index` position
    digits = [digits[j] for j in valid_digits]

    return digits
