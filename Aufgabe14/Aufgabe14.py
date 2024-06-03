from nltk import Valuation, Assignment, Model, Tree
from nltk.sem.logic import *


def return_parsed_tree(expr):
    if isinstance(expr, AndExpression):
        tree = Tree('(^)', [return_parsed_tree(expr.first), return_parsed_tree(expr.second)])
    elif isinstance(expr, OrExpression):
        tree = Tree('(v)', [return_parsed_tree(expr.first), return_parsed_tree(expr.second)])
    elif isinstance(expr, NegatedExpression):
        tree = Tree('(¬)', [return_parsed_tree(expr.term)])
    elif isinstance(expr, ImpExpression):
        tree = Tree('(=>)', [return_parsed_tree(expr.first), return_parsed_tree(expr.second)])
    elif isinstance(expr, IffExpression):
        tree = Tree('(<=>)', [return_parsed_tree(expr.first), return_parsed_tree(expr.second)])
    # FunctionVariableExpression represents a Variable like A - always a leaf
    elif isinstance(expr, FunctionVariableExpression):
        tree = Tree(str(expr.variable), [])
    else:
        print("Node not found")
        exit(1)
    return tree


#parser erzeugen.
bool_exp_parser = LogicParser(True)
#Der Baum
parse_result = bool_exp_parser.parse("(A | B | C) & (A | B | -C) & (-A | B | C) & (-A | -B | C)")
#Bildet ein Model
model = Model(set([]), Valuation([('A', True), ('B', True), ('C', True), ('D', True)]))
#Prüft ob dieser model diesen Baum auch erfüllt
print(return_parsed_tree(parse_result).draw())

#Und bildet stärker als oder, Negation stärker als und
