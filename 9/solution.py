exec(open("../1/solution.py").read())

def read_data(input_file):
    return [ int(line.strip()) for line in open(input_file)]


def get_data(test= True, read_function = read_data):
    test_file = "test.txt"
    main_file = "input.txt"
    file_to_use = test_file if test else main_file
    return read_function(file_to_use) , 5 if test else 25 


def find_weak(data, preamble):
    for i in range(preamble, len(data)):
        target = data[i]
        target_range = data[i-preamble : i] 
        strong, _, _ = two_sum(target, target_range)
        if not strong:
            return target
    return -1



def find_range(data, target):

    l, r = 0,2

    for l in range(len(data)):
        
        while sum(data[l:r]) < target and r < len(data) and r-l >= 2:
            r = r+1

        if sum(data[l:r])  == target:
            mx, mn = max(data[l:r]), min(data[l:r])
            print(mn, mx, mx+mn)
            return mx + mn
    
    return -1

if __name__ == "__main__":
    
    data = get_data(False)
    weak = find_weak(*data)
    print(weak)
    print(find_range(data[0], weak))
