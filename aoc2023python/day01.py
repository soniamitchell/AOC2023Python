import re

def day01(filename):

  dat = inputlist(filename)
  numbers = num()

  # Convert "two" into "2", etc.
  for i, s in enumerate(dat):
    for k in list(numbers.keys()):
        if k in s:
            dat[i] = re.sub(k, k[0] + numbers[k] + k[-1], dat[i])

  # Extract and concatenate the first and last digits in each string
  digits = [re.findall(r'\d', x) for x in dat]
  calibration_value = [int(x[0] + x[-1]) for x in digits]

  return sum(calibration_value)


def num():
  numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0" 
  }
  return numbers