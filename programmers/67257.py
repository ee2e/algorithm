import re, itertools

def solution(expression):
    p = re.compile('(\d+)([\+\-\*]?)')
    exp = p.findall(expression)
    
    exp_list = []
    for e in exp:
        exp_list += e
    
    save = exp_list[:-1]
    
    hash_table = {'*': 1, '-': 2, '+': 3}
    orders = itertools.permutations(['*', '-', '+'])
    maxV = 0
    
    for order in orders:
        exp_list = save
        for o in order:
            i = 1
            while i < len(exp_list):
                if len(exp_list) == 1:
                    break
                if exp_list[i] == o:
                    if hash_table[o] == 1:
                        num = int(exp_list[i-1]) * int(exp_list[i+1])
                    elif hash_table[o] == 2:
                        num = int(exp_list[i-1]) - int(exp_list[i+1])
                    else:
                        num = int(exp_list[i-1]) + int(exp_list[i+1])
                    if i-2 >= 0 and i+2 < len(exp_list):
                        exp_list = exp_list[:i-1] + [num] + exp_list[i+2:]
                    elif i+2 < len(exp_list):
                        exp_list = [num] + exp_list[i+2:]
                    else:
                        exp_list = exp_list[:i-1] + [num]
                else:
                    i += 1
        if abs(exp_list[0]) > maxV:
            maxV = abs(exp_list[0])

    return maxV