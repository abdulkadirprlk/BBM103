# Abdulkadir Parlak 2210765025
# Assignment3
import sys
import os

current_dir_path = os.getcwd()
readingFileName = sys.argv[1] # Input file is taken from the user.
readingFilePath = os.path.join(current_dir_path, readingFileName)

writingFileName = "output.txt"
writingFilePath = os.path.join(current_dir_path, writingFileName)

def read_inputs():
    result = ""
    with open(readingFilePath, "r", encoding="UTF-8") as input_file: # Reading the input file.
        for line in input_file.readlines():
            if line.startswith("CREATECATEGORY"):
                category_name = line[15:26]
                line = line[27:-1]
                line = line.split("x")
                row_count = int(line[0])
                column_count = int(line[1])
                result += create_category(category_name, row_count, column_count)
            elif line.startswith("SELLTICKET"):
                line = line[10:]
                line = line.split()
                customer_name = line[0]
                ticket_type = line[1]
                category_name = line[2]
                line = line[3:]
                if len(line) == 1:
                    result += sell_ticket(customer_name, ticket_type, category_name, line[0])
                elif len(line) == 2:
                    result += sell_ticket(customer_name, ticket_type, category_name, line[0], line[1])
                elif len(line) == 3:
                    result += sell_ticket(customer_name, ticket_type, category_name, line[0], line[1], line[2])
                elif len(line) == 4:
                    result += sell_ticket(customer_name, ticket_type, category_name, line[0], line[1], line[2], line[3])
                elif len(line) == 5:
                    result += sell_ticket(customer_name, ticket_type, category_name, line[0], line[1], line[2], line[3], line[4])
            elif line.startswith("CANCELTICKET"):
                line = line[13:]
                line = line.split()
                category_name = line[0]
                line = line[1:]
                if len(line) == 1:
                    result += cancel_ticket(category_name, line[0])
                elif len(line) == 2:
                    result += cancel_ticket(category_name, line[0], line[1])
                elif len(line) == 3:
                    result += cancel_ticket(category_name, line[0], line[1], line[2])
                elif len(line) == 4:
                    result += cancel_ticket(category_name, line[0], line[1], line[2], line[3])
            elif line.startswith("BALANCE"):
                if "\n" in line: # If line includes a "\n" character, it has 2 different situations.
                    category_name = line[8:-1]
                else:
                    category_name = line[8:]
                result += balance(category_name)
            elif line.startswith("SHOWCATEGORY"):
                if "\n" in line:
                    category_name = line[13:-1]
                else:
                    category_name = line[13:]
                result += show_category(category_name)
    return result

def create_category(category_name, row_count, column_count):
    result = ""
    for j in category_name_list:
        if category_name == j:
            print("Warning: Cannot create the category for the second time. The stadium has already {}.".format(category_name))
            result += "Warning: Cannot create the category for the second time. The stadium has already {}.\n".format(category_name)
            return result
    category = [[" X " for i in range(row_count)] for j in range(column_count)] # 2D list
    category_list.append(category)
    category_name_list.append(category_name)
    print("The category '{}' having {} seats has been created.".format(category_name, row_count * column_count))
    result += "The category '{}' having {} seats has been created.\n".format(category_name, row_count * column_count)
    return result

def sell_ticket(customer_name, ticket_type, category_name, *seat):
    result = ""
    for a in seat:
        if len(a) == 2 or len(a) == 3: # The seats that are singular goes into this if condition.For instance; C1, B4, B12, E10.
            for i in range(len(category_name_list)):
                if category_name_list[i] == category_name:
                    row_letter = len(category_list[i]) - (ord(a[0]) - 64) # row_letter variable stores the corresponding index of the row letter.
                    if row_letter > len(category_list[i]): # Example: a = "X5"
                        print("Error: The category '{}' has less row than the specified index {}!".format(category_name, a))
                        result += "Error: The category '{}' has less row than the specified index {}!\n".format(category_name, a)
                        break
                    if len(a) == 2:#The seats that are singular and with 1 decimal column number goes into this if condition.For instance; C1, B4.
                        column_number = int(a[1])
                        if int(column_number) > len(category_list[i][0]) - 1:  # Example: a = "E45"
                            print("Error: The category '{}' has less column than the specified index {}!".format(category_name, a))
                            result += "Error: The category '{}' has less column than the specified index {}!\n".format(category_name, a)
                            break
                        elif row_letter > len(category_list[i]) and int(column_number) > len(category_list[i][0] - 1):  # Example: a = "Q37"
                            print("Error: The category '{}' has less row and column than the specified index {}!".format(category_name, a))
                            result += "The category '{}' has less row and column than the specified index {}!\n".format(category_name, a)
                            break
                        if category_list[i][row_letter][column_number] == " X ":
                            category_list[i][row_letter][column_number] = " " + ticket_type[0].upper() + " "
                            if ticket_type == "season":
                                category_list[i][row_letter][column_number] = " T "
                            print("Success: {} has bought {} at {}".format(customer_name, a, category_name))
                            result += "Success: {} has bought {} at {}\n".format(customer_name, a, category_name)
                        else:
                            print("Warning: The seat {} cannot be sold to {} since it was already sold!".format(a, customer_name))
                            result += "Warning: The seat {} cannot be sold to {} since it was already sold!\n".format(a, customer_name)
                    elif len(a) == 3:#The seats that are singular and with 2 decimal column number goes into this if condition.For instance; C11, A17, F20.
                        column_number = int(a[1:3])
                        if int(column_number) > len(category_list[i][0]) - 1:  # Example: a = "E45"
                            print("Error: The category '{}' has less column than the specified index {}!".format(category_name, a))
                            result += "Error: The category '{}' has less column than the specified index {}!\n".format(category_name, a)
                            break
                        elif row_letter > len(category_list[i]) and int(column_number) > len(category_list[i][0] - 1):  # Example: a = "Q37"
                            print("Error: The category '{}' has less row and column than the specified index {}!".format(category_name, a))
                            result += "The category '{}' has less row and column than the specified index {}!\n".format(category_name, a)
                            break
                        if category_list[i][row_letter][column_number] == " X ":
                            category_list[i][row_letter][column_number] = " " + ticket_type[0].upper() + " "
                            if ticket_type == "season":
                                category_list[i][row_letter][column_number] = " T "
                            print("Success: {} has bought {} at {}".format(customer_name, a, category_name))
                            result += "Success: {} has bought {} at {}\n".format(customer_name, a, category_name)
                        else:
                            print("Warning: The seat {} cannot be sold to {} since it was already sold!".format(a, customer_name))
                            result += "Warning: The seat {} cannot be sold to {} since it was already sold!\n".format(a, customer_name)

        else:#If our seat tuple has more than one seat, it goes into this condition.
            for i in range(len(category_name_list)):
                if category_name_list[i] == category_name:
                    row_letter = len(category_list[i]) - (ord(a[0]) - 64)
                    if row_letter > len(category_list[i]): # Example: a = "X5"
                        print("Error: The category '{}' has less row than the specified index {}!".format(category_name, a))
                        result += "Error: The category '{}' has less row than the specified index {}!\n".format(category_name, a)
                        break
                    if len(a) == 4: # Example: a = "C1-3"
                        if int(a[3]) > len(category_list[i][0]): # Example : a = "A34"
                            print("Error: The category '{}' has less column than the specified index {}!".format(category_name, a))
                            result += "Error: The category '{}' has less column than the specified index {}!\n".format(category_name, a)
                            break
                        elif int(a[3]) > len(category_list[i][0]) and row_letter > len(category_list[i]): # Example: a = "X34"
                            print("Error: The category '{}' has less column and row than the specified index {}!".format(category_name, a))
                            result += "Error: The category '{}' has less column and row than the specified index {}!\n".format(category_name, a)
                            break
                        is_seats_empty = True
                        for k in range(int(a[1]), int(a[3]) + 1):
                            if category_list[i][row_letter][k] != " X ":#checking if any seat is full at seat sequence.
                                is_seats_empty = False
                                print("Warning: The seats {} cannot be sold to {} since some of them have already been sold!".format(a, customer_name))
                                result += "Warning: The seats {} cannot be sold to {} since some of them have already been sold!\n".format(a, customer_name)
                                break
                        if is_seats_empty:
                            for k in range(int(a[1]), int(a[3]) + 1):
                                category_list[i][row_letter][k] = " " + ticket_type[0].upper() + " "
                                if ticket_type == "season":
                                    category_list[i][row_letter][k] = " T "
                            print("Success: {} has bought {} at {}".format(customer_name, a, category_name))
                            result += "Success: {} has bought {} at {}\n".format(customer_name, a, category_name)
                    elif len(a) == 5:#Example: a = "C2-10"
                        if int(a[3:5]) > len(category_list[i][0]): #Example: a = "A34"
                            print("Error: The category '{}' has less column than the specified index {}!".format(category_name, a))
                            result += "Error: The category '{}' has less column than the specified index {}!\n".format(category_name, a)
                            break
                        elif int(a[3:5]) > len(category_list[i][0]) and row_letter > len(category_list[i]): # Example: a = "X34"
                            print("Error: The category '{}' has less column and row than the specified index {}!".format(category_name, a))
                            result += "Error: The category '{}' has less column and row than the specified index {}!\n".format(category_name, a)
                            break
                        is_seats_empty = True
                        for k in range(int(a[1]), int(a[3:5]) + 1):
                            if category_list[i][row_letter][k] != " X ":
                                is_seats_empty = False
                                print("Warning: The seats {} cannot be sold to {} since some of them have already been sold!".format(a, customer_name))
                                result += "Warning: The seats {} cannot be sold to {} since some of them have already been sold!\n".format(a, customer_name)
                                break
                        if is_seats_empty:
                            for k in range(int(a[1]), int(a[3:5]) + 1):
                                category_list[i][row_letter][k] = " " + ticket_type[0].upper() + " "
                                if ticket_type == "season":
                                    category_list[i][row_letter][k] = " T "
                            print("Success: {} has bought {} at {}".format(customer_name, a, category_name))
                            result += "Success: {} has bought {} at {}\n".format(customer_name, a, category_name)
                    elif len(a) == 6:#Example: a = "C10-20"
                        if int(a[4:6]) > len(category_list[i][0]): #Example: a = "A34"
                            print("Error: The category '{}' has less column than the specified index {}!".format(category_name, a))
                            result += "Error: The category '{}' has less column than the specified index {}!\n".format(category_name, a)
                            break
                        elif int(a[4:6]) > len(category_list[i][0]) and row_letter > len(category_list[i]): # Example: a = "X34"
                            print("Error: The category '{}' has less column and row than the specified index {}!".format(category_name, a))
                            result += "Error: The category '{}' has less column and row than the specified index {}!\n".format(category_name, a)
                            break
                        is_seats_empty = True
                        for k in range(int(a[1:3]), int(a[4:6]) + 1):
                            if category_list[i][row_letter][k] != " X ":
                                is_seats_empty = False
                                print("Warning: The seats {} cannot be sold to {} since some of them have already been sold!".format(a, customer_name))
                                result += "Warning: The seats {} cannot be sold to {} since some of them have already been sold!\n".format(a, customer_name)
                                break
                        if is_seats_empty:
                            for k in range(int(a[1:3]), int(a[4:6]) + 1):
                                category_list[i][row_letter][k] = " " + ticket_type[0].upper() + " "
                                if ticket_type == "season":
                                    category_list[i][row_letter][k] = " T "
                            print("Success: {} has bought {} at {}".format(customer_name, a, category_name))
                            result += "Success: {} has bought {} at {}\n".format(customer_name, a, category_name)
    return result

def cancel_ticket(category_name, *seat):
    result = ""
    for a in seat:
        for i in range(len(category_name_list)):
            if category_name_list[i] == category_name:
                row_letter = len(category_list[i]) - (ord(a[0]) - 64)
                if len(a) == 2:#Example: a = "C0"
                    column_number = int(a[1])
                elif len(a) == 3:#Example a = "A13"
                    column_number = int(a[1:3])
                if column_number > len(category_list[i][0]) - 1:#Example: a = "E45"
                    print("Error: The category '{}' has less column than the specified index {}!".format(category_name, a))
                    result += "Error: The category '{}' has less column than the specified index {}!\n".format(category_name, a)
                    break
                elif row_letter > len(category_list[i]):#Example a = "Z3"
                    print("Error: The category '{}' has less row than the specified index {}!".format(category_name, a))
                    result += "Error: The category '{}' has less row than the specified index {}!\n".format(category_name, a)
                    break
                elif row_letter > len(category_list[i]) and column_number > len(category_list[i][0]) - 1:#Example: a = "Q37"
                    print("Error: The category '{}' has less row and column than the specified index {}!".format(category_name, a))
                    result += "Error: The category '{}' has less row and column than the specified index {}!\n".format(category_name, a)
                    break
                if category_list[i][row_letter][column_number] == " X ":
                    print("Error: The seat {} at '{}' has already been free! Nothing to cancel.".format(a, category_name))
                    result += "Error: The seat {} at '{}' has already been free! Nothing to cancel.\n".format(a, category_name)
                else:
                    category_list[i][row_letter][column_number] = " X "
                    print("Success: The seat {} at '{}' has been canceled and now ready to sell again.".format(a, category_name))
                    result += "Success: The seat {} at '{}' has been canceled and now ready to sell again.\n".format(a, category_name)
    return result

def balance(category_name):
    result = ""
    student_count = 0
    full_count = 0
    season_count = 0
    for i in range(len(category_name_list)):
        if category_name == category_name_list[i]:
            for j in range(len(category_list[i])):
                for k in category_list[i][j]:
                    if k == " S ": # Student ticket = 10$
                        student_count += 1
                    elif k == " T ": # Season ticket = 250$
                        season_count += 1
                    elif k == " F ": # Full ticket = 20$
                        full_count += 1
    print("category report of {}".format(category_name))
    print("------------------------------")
    print("Sum of students = {}, Sum of full pay = {}, Sum of season ticket = {}, and Revenues = {} Dollars".format(student_count, full_count, season_count, (student_count*10 + full_count*20 + season_count*250)))
    result += "category report of {}\n".format(category_name)
    result += "------------------------------\n"
    result += "Sum of students = {}, Sum of full pay = {}, Sum of season ticket = {}, and Revenues = {} Dollars\n".format(student_count, full_count, season_count, (student_count*10 + full_count*20 + season_count*250))
    return result

def show_category(category_name):
    result = ""
    print("Printing category layout of {}".format(category_name), end="")
    result += "Printing category layout of {}".format(category_name)
    for i in range(len(category_name_list)):
        if category_name_list[i] == category_name:
            for j in range(len(category_list[i])):
                print()
                result += "\n"
                print(chr(64 + len(category_list[i]) - j), end="") # This is for the letters of category layout. Ex: A B C D E F...
                result += chr(64 + len(category_list[i]) - j)
                for k in range(len(category_list[i][j])): # For printing X's
                    print(category_list[i][j][k], end="")
                    result += category_list[i][j][k]
    print(" ")
    result += " \n"
    for i in range(len(category_name_list)):
        if category_name_list[i] == category_name:
            for j in range(len(category_list[i])): # This is for the numbers of category layout. Ex: 0 1 2 3 4 5 6...
                if len(str(j)) == 1:
                    print("  " + str(j), end="")
                    result += "  " + str(j)
                elif len(str(j)) == 2:
                    print(" " + str(j), end="")
                    result += " " + str(j)
    print()
    result += "\n"
    return result


customer_name_list = []
category_name_list = []
category_list = [] # This is a 3D list.

with open(writingFilePath, "w", encoding="UTF-8") as output_file:
    output_file.write(read_inputs())