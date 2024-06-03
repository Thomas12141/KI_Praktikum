from nltk import Model, Valuation, Assignment
from nltk.sem.logic import *

from Aufgabe15.Aufgabe15 import create_kb


def evaluate(expr, variables) -> bool:
    """
    traverse the tree and evalutes the expression
    """
    if isinstance(expr, AndExpression):
        return evaluate(expr.first, variables) and evaluate(expr.second, variables)
    elif isinstance(expr, OrExpression):
        return evaluate(expr.first, variables) or evaluate(expr.second, variables)
    elif isinstance(expr, ImpExpression):
        return not evaluate(expr.first, variables) or evaluate(expr.second, variables)
    elif isinstance(expr, NegatedExpression):
        return not evaluate(expr.term, variables)
    elif isinstance(expr, IffExpression):
        return evaluate(expr.first, variables) is evaluate(expr.second, variables)
    elif isinstance(expr, FunctionVariableExpression):
        v = str(expr.variable)
        if v not in variables:
            print("Varibale undefined, default False")
            return False
        return variables.get(v)
    else:
        print("Node not found")
        exit(1)


def check_all_kb(kb: list, variables: dict) -> bool:
    for expr in kb:
        if not evaluate(expr, variables):
            return False
    return True


knowledge_base = create_kb()

print(check_all_kb(knowledge_base.set, {"A": True, "B": True, "C": False, "D": True}))
