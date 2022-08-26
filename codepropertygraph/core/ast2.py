import ast

code = "one_plus_two = 1+2"
tree = ast.parse(code)
# dump = ast.dump(tree, indent=4)

for node in ast.walk(tree):
    for field_name, child_node in ast.iter_fields(node):
        if child_node is not None and child_node != []:
            print(field_name, child_node)

# print(dump)


