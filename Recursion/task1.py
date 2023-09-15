# A program that finds the sum of a list or tuple recursively and prints the total sum

MyList = [5, 6] # define a list

def summed(d):  # function d 
    if len(d) == 0: # base case 
        return 0
    else:
        return d[0] + summed(d[1:]) # extracting the first element from the list

summed(MyList)
print(summed(MyList))