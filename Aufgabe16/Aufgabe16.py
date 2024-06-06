from nltk.sem.logic import *

from Aufgabe15.Aufgabe15 import create_kb


def evaluate(expr, variables) -> bool:
    """
    traverse the tree and evalutes the expression
    """
    match expr:
        case AndExpression():
            return evaluate(expr.first, variables) and evaluate(expr.second, variables)
        case OrExpression():
            return evaluate(expr.first, variables) or evaluate(expr.second, variables)
        case ImpExpression():
            return not evaluate(expr.first, variables) or evaluate(expr.second, variables)
        case NegatedExpression():
            return not evaluate(expr.term, variables)
        case IffExpression():
            return evaluate(expr.first, variables) is evaluate(expr.second, variables)
        case FunctionVariableExpression():
            v = str(expr.variable)
            if v not in variables:
                print("Varibale undefined, default False")
                return False
            return variables.get(v)
        case _:
            print("Node not found")
            exit(1)


def check_all_kb(kb: list, variables: dict) -> bool:
    for expr in kb:
        if not evaluate(expr, variables):
            return False
    return True


knowledge_base = create_kb()

print(check_all_kb(knowledge_base.set, {"A": True, "B": True, "C": True, "D": True}))

