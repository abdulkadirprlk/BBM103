import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

x = a**b
x_str_list = list(str(x))#x_str_list contains every digit of the number as elements
x_int_list = [int(i) for i in x_str_list]#making all elements integer

print("{}^{} = {} = ".format(a, b, x), end="")
while len(str(sum(x_int_list))) != 1:#digits of sum of digits != 1
    if len(x_int_list) == 2:#count of digits
        print(x_str_list[0], "+", x_str_list[1], "=", sum(x_int_list), "= ", end="")
        x_str_list = list(str(sum(x_int_list)))
        x_int_list = [int(i) for i in x_str_list]
    elif len(x_int_list) == 3:
        print(x_str_list[0], "+", x_str_list[1], "+", x_int_list[2], "= ", sum(x_int_list), "= ", end="")
        x_str_list = list(str(sum(x_int_list)))
        x_int_list = [int(i) for i in x_str_list]
    elif len(x_int_list) == 4:
        print(x_str_list[0], "+", x_str_list[1], "+", x_int_list[2], "+", x_int_list[3], "= ", sum(x_int_list), "= ", end="")
        x_str_list = list(str(sum(x_int_list)))
        x_int_list = [int(i) for i in x_str_list]

#digits of sum of digits = 1 situations
if len(x_int_list) == 2:#count of digits
    print(x_str_list[0], "+", x_str_list[1], "=", sum(x_int_list))
elif len(x_int_list) == 3:#Example: 3^5 = 125
    print(x_str_list[0], "+", x_str_list[1], "+", x_str_list[2], "=", sum(x_int_list))
elif len(x_int_list) == 4:
    print(x_str_list[0], "+", x_str_list[1], "+", x_int_list[2], "+", x_int_list[3], "= ", sum(x_int_list))
