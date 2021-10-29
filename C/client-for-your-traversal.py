import json
import sys
from json import JSONDecodeError

# check if dest node is in the neighbor of src node
# if it is not, either create an object or append into the neighbor list
def one_dir_check(src, dest):
    src_list = edges.get(src)
    if src_list:
        for neighbor in src_list:
            if neighbor != '' and neighbor == dest:
                print("Duplicated edge.")
                exit()
        src_list.append(dest)
    else:
        edges[src] = [dest]
    return True

# create a labyrinth and check invalid edges
# we had create_graph(x,y) in our previous traversal.md, but in this case, 
# we actually get edges as input. Our previos traversal.md won't work here, so 
# we change the design of creating labyrinth. The method should takes in distinct
# edges to create a labyrinth.
def lab_creation(input):
    nodes = input[1:]
    output = ["lab"]
    for pair in nodes:
        try:
            src = pair["from"]
            des = pair["to"]
        except:
            exit("Invalid labyrinth creation!")
        if one_dir_check(src, des) and one_dir_check(des,src):
            output.append(pair)
    filter_input.append(output)

# check if add command is valid
# We didn't write this method in our specification because we thought we need
# image color to really show client with labyrinth graph. Thus, we change the 
# design, and have a method that takes name of node and uniqe color string to add
# color on named node
def token_check(input):
    node = input[2]
    color = input[1]
    if node in edges:
        # color has to be one of the color_string
        if color in color_string:
            token[node] = color
            filter_input.append(input)
        else:
            print("Invalid color!")
    else:
        print("Unexsiting node!")

# convert stdin to json
def convert_json(input):
    output = []
    json_decoder = json.JSONDecoder()
    cur_index = 0
    while len(input) > cur_index:
        if input[cur_index] == " ":
            cur_index += 1
        else:
            try:
                json_val, json_index = json_decoder.raw_decode(input[cur_index:])
                cur_index += json_index
                if type(json_val) == list:
                    output.append(json_val)
            except JSONDecodeError:
                cur_index += 1
                continue;
    return output

# parse input commands
def main(commands):
    for command in commands:
        if command[0] == "lab" and len(command) == 1:
            exit("Invalid Labyrinth createion")
        elif command[0] == "lab" and len(command) > 1:
            lab_creation(command)
        elif command[0] == "add" and len(command) == 3:
            token_check(command)
        elif command[0] == "move" and len(command) == 3:
            if command[1] == token.get(command[2]):
                filter_input.append(command)

# the main method
if __name__ == '__main__':
    TCP_IP = '127.0.0.1'
    TCP_PORT = 8000
    BUFFER_SIZE = 1024
    color_string = ["white", "black", "red", "green", "blue"]
    token = {}
    edges = {}
    filter_input = []

    input = sys.stdin.read()
    commands = convert_json(input)
    main(commands)

    # send filtered list to the server
    print("---------STDOUT---------")
    print(filter_input)





