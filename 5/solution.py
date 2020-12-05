
def get_data(test= True):
    test_file = "test.txt"
    main_file = "input.txt"
    file_to_use = test_file if test else main_file
    return read_data(file_to_use)

read_data= lambda f : [ l.strip() for l in open(f)]
toId = lambda r,c : (r*8)+c
bin2dec = lambda n : int(n, 2)
r = lambda l, transform : transform(l[:-3].replace("F", "0").replace("B", "1"))
c = lambda l, transform : transform(l[-3:].replace("L", "0").replace("R", "1"))

def split(data, transform = lambda x : x):
    return [ (r(l, transform), c(l, transform)) for l in  data]




if __name__ == "__main__":

    tickets = split(get_data(False), bin2dec)
    ids = sorted([ toId(*seat) for seat in tickets], reverse = True)
    
    print(ids[0])
    
    #part 2
    for i in range(1, len(ids)):
       if ids[i-1] - ids[i] > 1:
           print((ids[i-1] + ids[i])//2)

   
