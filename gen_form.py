import random, sys, os

def gen_form(depth = None, max_depth=10,num_literals=5):
    if random.random() < 0.2 or depth == max_depth:
        neg = random.random() > 0.5
        lit = random.randint(1,num_literals)
        if neg:
            return "(-" + str(lit) + ")"
        else:
            return str(lit)
    else:
        d = depth
        if d == None:
            d = 0
        op = random.choice(['+','.'])
        if d != 0:
            return '(' + gen_form(d+1,max_depth,num_literals) + ' ' + op + ' ' + gen_form(d+1,max_depth,num_literals) + ')'
        else:
            return '(' + gen_form(d+1,max_depth,num_literals) + ' ' + op + ' ' + gen_form(d+1,max_depth,num_literals) + ')'



if __name__ == "__main__":
    if len(sys.argv) == 1:
        directory = os.path.dirname('./')
    elif len(sys.argv) == 2:
        directory = os.path.dirname(sys.argv[1])
    else:
        printf('Too many arguments, using the current directory')
        directory = os.path.dirname('./')
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(10):
        NNF_STRING = gen_form()
        file_name = "fuzzy_testcase_" + str(i) + ".nnf"
        file_path = os.path.join(directory, file_name)
        fp = open(file_path, "w+")
        fp.write(NNF_STRING + ' 0')
