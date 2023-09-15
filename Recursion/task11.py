# A python program that implements the binary search algorthm recursively
# The function searches for an element in a sequence and returns it's index
# Returns -1 if value not returned

def binary_search(seq, low, high, elm):
    if low > high:
        return -1
    else:
        middle = (low + high) // 2

        if elm == seq[middle]:
            return middle
        elif elm < seq[middle]:
            return(binary_search(seq, low, middle-1, elm))
        else:
            return(binary_search(seq, middle +1, high, elm))



ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

print(binary_search(ls, 0, len(ls), 100))