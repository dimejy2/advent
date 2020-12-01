def two_sum(target, data):
    for i in range(len(data)):
        candidate = data[i]
        diff = target - candidate
        # could make this faster by using binary search since the list is sorted.
        if diff in data[i+1:]:
            return (True, diff * candidate, [candidate, diff])
    return (False, -1, [])



def three_sum(target, data):

    for i in range(len(data)):
        candidate = data[i]
        sub_target = target - candidate
        # could reduce memory usage by passing the reference to the array and the current index
        success, product, elems  = two_sum(sub_target, data[i+1:])
        if success:
            return(True, candidate * product, [ candidate, *elems])
    return (False, -1, [])


if __name__ == "__main__":
    inputFile = "input.txt"
    data = sorted([int(line.strip()) for line in open(inputFile, 'r')])
    
    print(two_sum(2020, data))
    print(three_sum(2020, data))
