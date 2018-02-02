import sys

for line in sys.stdin: # read from the standard input line-by-line
    # i = int(line)
    a = int(line[1])
    b = int(line[4])
    #i = list(map(int, line))
    square = a*a + 2*a*b + b*b
    print(square) # square
