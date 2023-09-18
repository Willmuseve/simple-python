# A program that displays the current date and time and prints
# formatted as yyyy-mm-dd, hh:mm:ss

import datetime

current_time = datetime.datetime.now()

print("The current date and time is:")
print(current_time.strftime("%y-%m-%d %H:%M:%S"))