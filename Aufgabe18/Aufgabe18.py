import nltk
from nltk import Model, Valuation
from nltk.sem.logic import LogicParser

from Aufgabe15.Aufgabe15 import create_kb
from Aufgabe16.Aufgabe16 import check_all_kb


def tt_check_all(kb: list, query, symbols: set, model: dict):
    if len(symbols) == 0:
        if check_all_kb(kb, model):
            return check_all_kb(list(query), model)
        else:
            return True
    else:
        p = symbols.pop()
        model_with_true = dict()
        model_with_true[p] = True
        model_with_true.update(model)
        model_with_false = dict()
        model_with_false[p] = False
        model_with_false.update(model)

        return tt_check_all(kb, query, symbols.copy(), model_with_false) and tt_check_all(kb, query, symbols.copy(),
                                                                                          model_with_true)


bool_exp_parser = LogicParser(True)

tt_check_all(create_kb().set, {bool_exp_parser.parse("A & C -> B | D")}, {"A", "B", "C", "D"}, dict())
