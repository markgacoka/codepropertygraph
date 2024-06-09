import ast

code = "one_plus_two = 1+2"
tree = ast.parse(code)
output = ast.dump(tree, indent=4)

print(output)
