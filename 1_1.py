file = open("input/1_1.txt")
print(sum([int(line)//3 - 2 for line in file]))