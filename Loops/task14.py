# A program that prints floyd's triangle with n number of rows

n = int(input("Enter the number of rows: ")) #Prompt the user

count = 1 # variable to store the numbers in the triangle

for i in range(1, n+1): # loop through the number of rows
    for j in range(i): # print the number in the ith row
        print(count, end=" ")
        count += 1 # increment the count variable
    print()