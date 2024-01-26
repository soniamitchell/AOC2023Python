import re

def day04(filename):

    dat = inputlines(filename)

    results = []

    for i, x in enumerate(dat):

        # Find matches
        intersection = find_matches(x)
        num_matches = len(intersection)

        # Calculate score
        if num_matches == 0:
            score = 0
        else:
            score = 1
            for y in range(len(intersection) - 1):
                score = score * 2

        print(f"Card {i + 1}: {num_matches} matches! {score} points.")

        results.append(score)

    return sum(results)
        


def day04b(filename):

    dat = inputlines(filename)

    # Number of copies of each card
    copies = [1] * len(dat)

    results = []

    for i, x in enumerate(dat):
        
        # Find matches
        intersection = find_matches(x)
        num_matches = len(intersection)

        # Add 1 copy to elements `i+1` to `i+1+num_matches` in `copies`
        finish = min([i + num_matches, len(dat)])
        copies = [element + copies[i] if i < index <= finish else element for 
                  index, element in enumerate(copies)]

    return sum(copies)
     
       
       
def find_matches(x):

    tmp = x.split(":")[1].split("|")
    winning_numbers = tmp[0].strip().split(" ")
    my_numbers = tmp[1].strip().split(" ")

    # Remove empty elements (some numbers are seperated by double spaces!)
    winning_numbers = [x for x in winning_numbers if len(x) > 0]
    my_numbers = [x for x in my_numbers if len(x) > 0]

    # Find the intersection 
    intersection = list(set(winning_numbers) & set(my_numbers))

    return intersection
    