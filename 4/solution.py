import re
def read_data(input_file):
    lines = [line.replace('\n',' ') for line in open(input_file).read().split('\n\n')]
    return [dict(tuple(x.split(':')) for x in line.split()) for line in lines]

def get_data(test= True):
    test_file = "test2.txt"
    main_file = "input.txt"
    file_to_use = test_file if test else main_file
    return read_data(file_to_use)

def hgt(field): 
    val, units = field[:-2], field[-2:]
    if re.match("\d+(cm|in)", field):
        val = int(val)
        return 150 <= val <= 193 if units == "cm" else 59 <= val <= 76
    return False

ruleset = {
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: hgt(x),
    'ecl': lambda x: re.match("(amb|blu|brn|gry|grn|hzl|oth)", x) != None,
    'pid': lambda x: len(x) == 9 and x.isnumeric()
    'hcl': lambda x: re.match("#[0-9,a-f]{6}", x) != None,
}


def is_valid(necessary, present):
    return necessary.issubset(present.keys()) and all([ruleset[key](present[key]) for key in ruleset])
        



if __name__ == "__main__":
   
    data = get_data(False)
    necessary1 = set(['pid', 'hgt', 'ecl', 'byr', 'eyr', 'iyr', 'hcl'])

    print( sum([ is_valid(necessary1, passport) for passport in data ]) )
