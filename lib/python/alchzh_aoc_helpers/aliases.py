import collections
import re

from dotmap import DotMap

NEWLINE_PATTERN = re.compile(r"\r?\n")
def lines(string, strip=True):
    string = str(string)
    if strip:
        string = string.strip()
    return re.split(NEWLINE_PATTERN, string)

sp = str.split
sr = str.strip

DotMap.i = DotMap.items
DotMap.k = DotMap.keys
DotMap.v = DotMap.values

en = enumerate
fs = frozenset
rn = range

DM = DotMap

Co = collections.Counter

rfi = re.finditer
rfa = re.findall

pr = print()
