from time import sleep

import Model as Model
import View as View

view = View.View()
file_name = input("Name of Input File: ")
input_file = open(file_name, 'r')
input_file_lines = input_file.readlines()

index = 0
for line in input_file_lines:
    commands = line.split()
    if index == 0:
        Model.add_process(int(commands[0]))
        for x in range(0, len(Model.get_processes())):
            view.add_process(Model.get_processes()[x])
    elif index == 1:
        Model.add_resource(commands)
        print("Initialized for {0} processes and {1} resources".format(str(len(Model.get_processes())),
                                                                       str(len(Model.get_resources()))))
        for x in range(0, len(Model.get_resources())):
            view.add_resource(Model.get_resources()[x])
    elif commands[0] == 'request':
        Model.request_resource(int(commands[1]), int(commands[2]), int(commands[3]))
        Model.check_deadlock()
        sleep(1)
    elif commands[0] == 'release':
        Model.release_resource(int(commands[1]), int(commands[2]), int(commands[3]))
        Model.check_deadlock()
        sleep(1)
    else:
        print("Invalid Operation\n")
    index += 1
