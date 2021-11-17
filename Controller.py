import Model
import View

file_name = input("Name of Input File: ")
input_file = open(file_name, 'r')
input_file_lines = input_file.readlines()

index = 0
for line in input_file_lines:
    commands = line.split(' ')
    if index == 0:
        pass
    elif index == 1:
        pass
    elif commands[0] == 'request':
        pass
    elif commands[0] == 'release':
        pass
    else:
        print("Invalid Operation\n")
    index += 1

