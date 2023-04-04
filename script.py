import re

filename = "results.csv"
#1872-11-30,Scotland,England,0,0,Friendly,Glasgow,Scotland,FALSE
pattern = re.compile(r'^([\d]{4,4})\-\d\d\-\d\d,(.*),.*$')

with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        res = re.match(pattern, line)
        if res:
            print(f"{res.group(2)}\n")