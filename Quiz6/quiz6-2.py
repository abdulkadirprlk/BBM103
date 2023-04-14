# Abdulkadir Parlak 2210765025
import sys

x = int(sys.argv[1])

rec_diamond_list = [" "*(i) for i in range(x)] # Creating the list with list comprehension.
rec_diamond_list2 = ["*"*(i+1) for i in range(0, 2*x, 2)] # Same here.
rec_diamond_list.sort(reverse=True)

for i in range(x):
    print(rec_diamond_list[i] + rec_diamond_list2[i])

rec_diamond_list2.sort(reverse=True) # After the top part of the pyramid, I reversed the list
rec_diamond_list.sort()              # in order to use the same list again for the bottom part of the shape.
rec_diamond_list2.pop(0)

for i in range(x-1): # When printing I used standard iteration method.
    print(rec_diamond_list[i+1] + rec_diamond_list2[i])