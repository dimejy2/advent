def parse_line(line, range_delim):
    ranges, sub, text = line.split()
    lo, hi =  [ int(r) for r in ranges.split(range_delim) ]
    return ( lo, hi, text, sub[0])

def rule_1(lo, hi, text, sub ):
    return text.count(sub) in range(lo, hi+1)

def rule_2(lo, hi, text, sub):
    idx  = [lo - 1, hi - 1]
    if all([ i in range(len(text)) for i in idx ]):
        return sum([text[i] == sub for i in idx]) == 1
    return False

def read_data(input_file):
    return [ line.strip() for line in open(input_file, 'r')]

def apply_rule(rule, data, aggregator = sum):
    return aggregator(map( lambda x : rule(*x), data))

if __name__ == "__main__":

    dash = "-"
    test_file = "test.txt"
    input_file = "input.txt"
    rules = [rule_1, rule_2]

    data =  map( lambda line : parse_line(line, dash), read_data(input_file))
    results = [apply_rule(rule, data) for rule in rules]
    print(results)

