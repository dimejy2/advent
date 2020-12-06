from pprint import pprint as pp

def read_data(input_file):
    return [ [ set(ans) for ans in line.split("\n") ] for line in open(input_file).read().split('\n\n')]


def get_data(test= True, read_function = read_data):
    test_file = "test.txt"
    main_file = "input.txt"
    file_to_use = test_file if test else main_file
    return read_function(file_to_use)

if __name__ == "__main__":

    data = get_data(False)
    #data = get_data()
    p1 = [ len(set.union(*l)) for l in data]
    p2 = [ len(set.intersection(*l)) for l in data]
    print(sum(p1), sum(p2))
