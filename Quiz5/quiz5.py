# Abdulkadir Parlak 2210765025
import sys
import os

lines = "-------------" # In order not to print them each time, I assigned this print template to a variable.
print_screen = "My results:\t\t{}\nResults to compare:\t{}" # I separated them because sometimes I need just one of them.

def my_round(text): # I implemented my own round function as you wanted.
    if float(text) % 1 >= 0.5:
        return int(float(text)) + 1
    else:
        return int(float(text))

try: # IndexError for the number of file names can occur.
    if len(sys.argv) < 3:
        raise IndexError("number of input files less than expected.")
    elif len(sys.argv) > 3:
        raise IndexError("number of input files more than expected.")

    path = os.getcwd() # Taking the current working directory and join it to the files.
    input_file_name = sys.argv[1] # After that, checking if the file in question really exists or not.
    input_file_path = os.path.join(path, input_file_name)
    if not os.path.exists(input_file_path): # Checking if that file exists for the first txt file
        raise IOError("cannot open {}".format(sys.argv[1]))

    output_file_name = sys.argv[2]
    output_file_path = os.path.join(path, output_file_name)
    if not os.path.exists(output_file_path): # Checking if that file exists for the second txt file
        raise IOError("cannot open {}".format(sys.argv[2]))

    with open(sys.argv[1], "r", encoding="UTF-8") as input_file:
        with open(sys.argv[2], "r", encoding="UTF-8") as output_file:
            for line in input_file: # I want my for loop iterate over even if an error occurs.
                line_list = line.split() # If an error occurs in the for loop, the program prints an error message and the
                                         # codes after that line will be still executable.
                try:
                    result2 = ""  # This result2 variable stores the corresponding data_comparison.txt file line.
                    result2 = output_file.readline()
                    result2 = result2.replace("\n", " ")

                    if len(line_list) < 4: # IndexError can occur.
                        raise IndexError("number of operands less than expected.")
                    elif len(line_list) > 4:
                        raise IndexError("number of operands more than expected.")

                    div = my_round(line_list[0]) # Rounding floats to integer.
                    nondiv = my_round(line_list[1]) # ValueError can occur.
                    From = my_round(line_list[2])
                    to = my_round(line_list[3])

                    result = "" # This result variable stores my results.
                    for i in range(From, to + 1):
                        if (i % div == 0) and (i % nondiv != 0):  # ZeroDivisionError can occur.
                            result += str(i) + " "

                    if result != result2: # checking if numbers are the same with data_comparison.txt
                        raise AssertionError("results don't match.") # AssertionError can occur.
                    else: # If no error occurs, this else block will be executed.
                        print(lines)
                        print(print_screen.format(result, result2))
                        print("Goool!!!")

                except ZeroDivisionError:
                    print(lines)
                    print("ZeroDivisionError: You can't divide by 0.")
                    print("Given input:", line, end="")

                except AssertionError as e:
                    print(lines)
                    print(print_screen.format(result, result2))
                    print("AssertionError:", e)

                except IndexError as e:
                    print(lines)
                    print("IndexError:", e)
                    print("Given input:", line, end="")

                except ValueError as e:
                    print(lines)
                    print("ValueError: only numeric input is accepted.")
                    print("Given input:", line, end="")

                except Exception as e:
                    print("kaBOOM: run for your life!")

except IndexError as e:
    print("IndexError:", e)

except IOError as e:
    print("IOError:", e)

except Exception as e: # If an unknown error occurs, this line will be executed.
    print("kaBOOM: run for your life!")

finally: # finally block will be always executed at the end of the output regardless of the input.
    print("~ Game Over ~")
