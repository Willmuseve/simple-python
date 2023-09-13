# A python program that prints the corresponding season based on the value of the season number
# possible values of season_num are: 1 for Spring, 2 for Summer, 3 for Fall, 4 for Winter
# prints "Please enter a valid number"  if the vaue 

print("Enter season number: ")
season_number = int(input())

if season_number == 1:
    print("It's spring")
elif season_number == 2:
    print("It's summer")
elif season_number == 3:
    print("Its fall")
elif season_number == 4:
    print("It's winter")
else:
    print("Please enter a valid number!")