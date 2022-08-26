import ast
import pprint
import astpretty

# with open("examples/addition.py", "r") as source:
#     document_tree = ast.parse(source.read()).body
#     bodies_num = len(document_tree)
#     for bodies in range(bodies_num):
#         node = document_tree[bodies]
#         print("Node: ", node.__class__.__name__, )
#         result = astpretty.pformat(node, indent='   ', show_offsets=False)
#         print(result)

def generate_AST(PATH):
    with open(PATH, "r") as source:
        tree = {}
        sections = ast.parse(source.read()).body
        bodies_num = len(sections)
        for section_num in range(bodies_num):
            ast_info = {}
            for node in ast.walk(sections[section_num]):
                for field_name, child_node in ast.iter_fields(node):
                    if child_node is not None and child_node != []:
                        ast_info[node.__class__.__name__] = ast_info.get(node.__class__.__name__, (field_name, child_node))
            tree[sections[section_num].__class__.__name__ + '_{}'.format(section_num+1)] = tree.get(sections[section_num].__class__.__name__ + '_{}'.format(section_num+1), ast_info)
    return tree


if __name__ == '__main__':
    PATH = "examples/small.py"
    tree = generate_AST(PATH)
    pp = pprint.PrettyPrinter(depth=4)
    pp.pprint(tree)
