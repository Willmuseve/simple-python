# A python program that prints all possible permutations of a list on a separate line or as a list or tuple
# The list itself is included in the permutations

#import the builtin itertools module
import itertools
MyList =[2, 4, 5]

permutations = itertools.permutations(MyList) # use the permutation function that generates all possible permutations of an iterable and MyList is an iterable

for p in permutations:
    print(list(p))


print("\nnewline")

for p in itertools.permutations(MyList):
    print(list(p))