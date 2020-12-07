import re
from itertools import takewhile, dropwhile

def read_data(input_file):
    split = [ 
            (line.strip().split("contain")[0], 
                line.strip().split("contain")[1].split(",")) 
            for line in open(input_file)]

    lines = {}
    for data in split:
        p, c = data
        children = {}
        for child in c:
            child = child.replace(".", "").replace("bags", "").replace("bag", "").strip()
            if child == "no other": 
                break
            count = int("".join(takewhile(str.isdigit, child)))
            name = "".join(dropwhile(str.isdigit, child))

            children[name.strip()] = count

        lines[p.replace(".", "").replace("bags", "").replace("bag", "").strip()] = children
    return lines



def dfs(graph, curr, target):
    children = graph[curr]
    if curr == target:
        return True
    if children == {}:
        return False
    return any([ dfs(graph, child, target) for child in children])


def dfs2(graph, curr, branching_factor):
    children = graph[curr]
    if children == {}:
        return 0
    total = 0

    for child in children:
        child_count = children[child]
        total += (branching_factor * child_count) + dfs2(graph, child, branching_factor * child_count)

    return total



def get_data(test= True):
    test_file = "test2.txt"
    main_file = "input.txt"
    file_to_use = test_file if test else main_file
    return read_data(file_to_use)

if __name__ == "__main__":

    data = get_data(False)
    target = "shiny gold"

    sm = 0 
    for top_level in data:
        if top_level != target :
            sm += dfs(data, top_level, target)
    print(sm)

    print(dfs2(data, target,1)) 
