# A program that prints a pyramid pattern wit asterics

num_rows = int(input("Enter a number: "))

k = (num_rows * 2) -2 # variable k that takes the num_rows, miltiplies by 2 then subtracts 2

for i in range(0, num_rows): #initializes the number of rows entered by the user
    for j in range(0, k): # prints spaces from range 0 and k leaving space for the asteric
        print(" ", end="")

    k = k - 2 # deducts 2 to provide space for the asterics during the next iteration

    for j in range(0, i + 1): # prints the asterics with a space 
        print("*", end=" ")
    print("")

    