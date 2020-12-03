from operator import mul

class path:
    def __init__(self, r_start, c_start, r_delta, c_delta):
        self.r_delta = r_delta
        self.c_delta = c_delta
        self.r = r_start
        self.c = c_start

    def next(self):
        self.r += self.r_delta
        self.c += self.c_delta

    def curr(self):
        return self.r, self.c

class grid:
    def __init__(self, grid):
        self.grid = grid
        self.end = len(grid)
        self.wrap = len(grid[0])

    def _translate(self,r,c):
        return r, c % self.wrap
        
    def _in_grid(self, r, c):
        return r < self.end
    
    def _get_loc(self, r, c):
        return self.grid[r][c]

    def _is_tree(self, r, c):
        r, c = self._translate(r,c)
        return self._get_loc(r,c) == '#'
    
    def count_trees(self, path):
        tree_count = 0
        while self._in_grid(*path.curr()):
            tree_count += self._is_tree(*path.curr())
            path.next()
        return tree_count

def read_data(input_file):
    return [line.strip() for line in open(input_file, 'r')]

def get_data(test= True):
    test_file = "test.txt"
    main_file = "input.txt"
    file_to_use = test_file if test else main_file
    return read_data(file_to_use)

if __name__ == "__main__":
   
    data = get_data(False)
    g = grid(data) 
    
    path_args = [(0,0,1,1), (0,0,1,3), (0,0,1,5), (0,0,1,7), (0,0,2,1)]

    # part 1
    part1 =  path(*path_args[1])
    print(g.count_trees(part1))
    
    # part 2
    part2 = map( lambda args : g.count_trees(path(*args)), path_args)
    print( list(part2), reduce(mul,part2, 1))
