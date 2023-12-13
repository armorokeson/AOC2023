import sys
from math import lcm

def create_dict(node_list):
    nodes = {}
    for node in node_list:
        key = node.split(' = ')[0]
        value = node.split(' = ')[1]
        nodes[key] = (value[1:4], value[6:9])
    return nodes

def traverse(insts, nodes):
    num_steps = 0
    curr_node = 'AAA'
    i = 0
    while True:
        if curr_node == 'ZZZ':
            return num_steps
        if insts[i] == 'R':
            curr_node = nodes.get(curr_node)[1]
        else:
            curr_node = nodes.get(curr_node)[0]
        num_steps += 1
        i += 1
        if i == len(insts):
            i = 0

def get_next_nodes(nodes, current_nodes, side):
    next_nodes = []
    for node in current_nodes:
        next_nodes.append(nodes.get(node)[side])
    return next_nodes

def traverse2(insts, nodes, curr_node):
    num_steps = 0
    i = 0
    while True:
        if curr_node[2] == 'Z':
            return num_steps

        if insts[i] == 'R':
            curr_node = nodes.get(curr_node)[1]
        else:
            curr_node = nodes.get(curr_node)[0]

        num_steps += 1
        i += 1
        if i == len(insts):
            i = 0

def get_starting_nodes(nodes):
    starting_nodes = set()
    for node in nodes:
        if node[2] == 'A':
            starting_nodes.add(node)
    return starting_nodes

def part1():
    file = open(sys.argv[-1], 'r')
    insts = file.readline().splitlines()[0]
    nodes = create_dict(file.read().splitlines()[1:])

    print(traverse(insts, nodes))

def part2():
    file = open(sys.argv[-1], 'r')
    insts = file.readline().splitlines()[0]
    nodes = create_dict((file.read().splitlines()[1:]))
    starting_nodes = get_starting_nodes(nodes.keys())

    steps = []
    for node in starting_nodes:
        steps.append(traverse2(insts, nodes, node))

    print(lcm(*steps))

# part1()
part2()
