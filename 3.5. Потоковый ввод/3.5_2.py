import sys
difference = 0
k = 0
for line in sys.stdin:
    difference += abs(int(line.split()[1]) - int(line.split()[2]))
    k += 1
print(round(difference / k))