import json
from collections import defaultdict

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return {'child': obj.__class__.__name__}

class AstGraphGenerator(object):

    def __init__(self, source):
        self.graph = defaultdict(lambda: [])
        self.source = source  # lines of the source code

    def __str__(self):
        return str(self.graph)

    def _getid(self, node):
        try:
            lineno = node.lineno - 1
            return "%s: %s" % (type(node), self.source[lineno].strip())

        except AttributeError:
            return type(node)

    def visit(self, node):
        """Visit a node."""
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node."""
        for _, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        self.visit(item)

            elif isinstance(value, ast.AST):
                print(self._getid(node), " : ", node.__dict__)
                print("Value: ", value.__dict__)
                node_source = self._getid(node)
                value_source = self._getid(value)
                # self.graph[node_source].append(value_source)
                self.graph[type(node).__name__].append(value.__dict__)
                self.visit(value)
        return self.graph

import ast

code = 'one_plus_two=1+2'
tree = ast.parse(code)
generator = AstGraphGenerator(code)
final_graph = generator.generic_visit(tree)

json_object = json.dumps(dict(final_graph), default=dumper, indent = 4)
#print(json_object)

