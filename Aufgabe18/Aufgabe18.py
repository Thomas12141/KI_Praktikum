import nltk
from nltk import Model, Valuation
from nltk.sem.logic import LogicParser

from Aufgabe15.Aufgabe15 import create_kb
from Aufgabe16.Aufgabe16 import check_all_kb


def tt_check_all(kb: list, query, symbols: set, model: set):
    if len(symbols) == 0:
        if check_all_kb(kb, Model(set([]), Valuation(model))):
            return check_all_kb(list(query), Model(set([]), Valuation(model)))
        else:
            return True
    else:
        p = symbols.pop()
        model_with_true = set()
        model_with_true.add((p, True))
        model_with_false = set()
        model_with_false.add((p, False))

        return tt_check_all(kb, query, symbols.copy(), model.union(model_with_false)) and tt_check_all(kb, query, symbols.copy(), model.union(model_with_true))


bool_exp_parser = LogicParser(True)

tt_check_all(create_kb(), {bool_exp_parser.parse("A & C -> B | D")}, {"A", "B", "C", "D"}, set())
