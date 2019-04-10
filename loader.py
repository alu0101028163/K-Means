import sys              # Command line arguments
import re               # Regular expressions
import numpy as np      # Arrays for high performance operations

f = open(sys.argv[1], "r")
number_of_entries = f.readline()
dimension = f.readline()
entries = []

for line in f:
    line = re.sub(r'[,]', r'.', line) # Changes commas for dots
    line = re.sub(r'\t', r' ', line)  # Changes tabs for spaces
    line = line.split(' ')            # Breaks the line by its spaces and returns a list.
    points = [float(point) for point in line]
    entries.append(points)

entries = np.array(entries)
print(entries)
f.close()
