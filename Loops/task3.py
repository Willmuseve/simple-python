# A program that prints the first non negaive integers from 1 to 100

list = []
for i in range(1, 101):
    list.append(i)
sumo = sum(list)
print(sumo)