import sys
for line in sys.stdin:
    if line.find("#") != 0:
        print(line[: line.find("#")])
