# Abdulkadir Parlak 2210765025
import os
import sys

current_dir_path = os.getcwd()
reading_file_name = sys.argv[1]
reading_file_path = os.path.join(current_dir_path, reading_file_name)

writing_file_name = sys.argv[2]
writing_file_path = os.path.join(current_dir_path, writing_file_name)

line_list = []
def mcr(x):# message code and line code returner (for "sort" method)
    return int(x[:4]), int(x[5])

def read_inputs():
    result = ""
    with open(reading_file_path, "r", encoding="UTF-8") as input_file:
        for line in input_file.readlines():
            line_list.append(line)
    line_list.sort(key=mcr)
    a = 1
    for i in line_list:
        if "0" == i[5]:
            result += "Message\t{}\n".format(a)
            a += 1
        if "\n" in i:
            result += i
        else:
            result += i + "\n"
    return result

def write_outputs():
    with open(writing_file_path, "w", encoding="UTF-8") as output_file:
        output_file.write(read_inputs())

write_outputs()