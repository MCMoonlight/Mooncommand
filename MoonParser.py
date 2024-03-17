import ast
import operator as op

# supported operators
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.USub: op.neg}

def mout(value):
    print(value)
    return value

def eval_expr(node):
    if isinstance(node, ast.Constant):  # <number> or <string>
        return node.value
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        return operators[type(node.op)](eval_expr(node.left), eval_expr(node.right))
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_expr(node.operand))
    elif isinstance(node, ast.Call):  # <function>(<arguments>)
        if node.func.id == 'mout':
            return mout(eval_expr(node.args[0]))
        else:
            raise TypeError(node)
    else:
        raise TypeError(node)

def parse(code):
    # convert the .mo syntax to Python syntax
    code = code.replace('for(int i =', 'for i in range(')

    # parse the code to abstract syntax tree
    tree = ast.parse(code, mode='exec')

    # create a new namespace for the execution of the for loop
    namespace = {'mout': mout}

    # execute the code
    exec(compile(tree, filename="<ast>", mode="exec"), namespace)

def read_mo_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def parse_mo_file():
    while True:
        # get the file path from user input
        file_path = input("请输入你的.mo文件:")

        # check if the file is a .mo file
        if not file_path.endswith('.mo'):
            print("这不是一个.mo文件，请重新输入。")
            continue

        # read the .mo file
        code = read_mo_file(file_path)

        try:
            # parse the code
            parse(code)
        except SyntaxError as e:
            print(e)

        # exit the loop
        break

# test
parse_mo_file()