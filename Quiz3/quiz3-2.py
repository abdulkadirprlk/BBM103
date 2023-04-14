import sys

list = sys.argv[1].split(",")# taking input and spliting it
list = [int(i) for i in list]# making all elements integer by using list comprehension

def print_list():# to display the current list
    for i in list:
        print(i, " ", end="")
    print()#to skip to the next line

print_list()#printing the initial list(input)

j = 1
while j < len(list):
    list.pop(j)#pop takes index of the element as argument
    j += 1

j = j - 10# j = 2 here

print_list()

while j < len(list):#to remove every 3rd number in the list
    list.pop(j)
    j += 2

print_list()

j = j - 2#j = 6 here

while j < len(list):# to remove every 7th element in the list
    list.pop(j)
    j += 6

print_list()