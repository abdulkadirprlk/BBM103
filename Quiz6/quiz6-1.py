# Abdulkadir Parlak 2210765025
import sys

x = int(sys.argv[1])

def rec_diamond(n): # Top of the pyramid
    if n == 1:
        return "*" * (2*x-1)
    else:
        return " " * (n - 1) + "*" * (2*x - (2*n-1)) + "\n" + rec_diamond(n - 1)

def rec_diamond2(n): # Bottom of the pyramid
    if n == (x-1):
        return " " * n + "*"
    else:
        return " " * n + "*" * (2*x - (2*n+1)) + "\n" + rec_diamond2(n + 1)

print(rec_diamond(x))
print(rec_diamond2(1))