import pandas as pd
import numpy as np
import re

def day02(filename):

    dat = inputlines(filename)

    impossible = []
    total_power = 0

    for i, x in enumerate(dat):

        # Tidy up data
        game, cubes = x.split(": ")
        cubes = re.sub(";", ",", cubes)
        cubes = cubes.split(", ")
        cubes = [x.split(" ") for x in cubes]
        cubes = pd.DataFrame(cubes, columns = ["number", "colour"])
        cubes["number"] = pd.to_numeric(cubes["number"])

        maximum = cubes.groupby("colour").max("number")
        power = np.prod(maximum, axis = 0)
        total_power = total_power + power

        # Maximum value of cubes
        limit = {"red": 12, 
                 "green": 13,
                 "blue": 14}

        for k in list(limit.keys()):
            if (maximum.loc()[k] > limit[k]).any():
                impossible.append(i + 1)
                break
        
    games = list(range(1, len(dat) + 1))
    possible = list(set(games) - set(impossible))

    return print("Sum of IDs = " + str(sum(possible)) + "\nPower = " + str(total_power.item()))
