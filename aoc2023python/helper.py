import re

def inputlist(filename):
    f = open(filename, "r")
    dat = f.read()
    output = dat.split()
    return output

def inputlines(filename):
    f = open(filename, "r")
    dat = f.readlines()
    output = [re.sub("\n", "", x) for x in dat]
    return output
