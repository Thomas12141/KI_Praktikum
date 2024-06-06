from nltk import Valuation, Assignment, Model, Tree
from nltk.sem.logic import *


def return_parsed_tree(expr):
    match expr:
        case AndExpression():
            tree = Tree('(^)', [return_parsed_tree(expr.first), return_parsed_tree(expr.second)])
        case OrExpression():
            tree = Tree('(v)', [return_parsed_tree(expr.first), return_parsed_tree(expr.second)])
        case NegatedExpression():
            tree = Tree('(¬)', [return_parsed_tree(expr.term)])
        case ImpExpression():
            tree = Tree('(=>)', [return_parsed_tree(expr.first), return_parsed_tree(expr.second)])
        case IffExpression():
            tree = Tree('(<=>)', [return_parsed_tree(expr.first), return_parsed_tree(expr.second)])
        # FunctionVariableExpression represents a Variable like A - always a leaf
        case FunctionVariableExpression():
            tree = Tree(str(expr.variable), [])
        case _:
            print("Node not found")
            exit(1)
    return tree


#parser erzeugen.
bool_exp_parser = LogicParser(True)
#Der Baum
parse_result = bool_exp_parser.parse("A<=>B=>C")
#Bildet ein Model
model = Model(set([]), Valuation([('A', True), ('B', True), ('C', True), ('D', True)]))
#Prüft ob dieser model diesen Baum auch erfüllt
print(return_parsed_tree(parse_result).draw())

#Und bildet stärker als oder, Negation stärker als und
