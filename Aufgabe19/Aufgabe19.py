from nltk.sem.logic import LogicParser

from Aufgabe15.Aufgabe15 import KnowledgeBase

from tabulate import tabulate

from Aufgabe16.Aufgabe16 import evaluate


def check_all_kb(kb: list, variables: dict, row: list) -> bool:
    result = True
    for expr in kb:
        evaluation = evaluate(expr, variables)
        row.append(str(evaluation))
        if not evaluation:
            result = False
    return result


def add_all_symbols_values(symbols: dict, row: list):
    for value in symbols.values():
        row.append(str(value))


def tt_check_all(kb: list, query, symbols: list, model: dict, rows: list):
    if len(symbols) == 0:
        row = []
        add_all_symbols_values(model, row)
        if check_all_kb(kb, model, row):
            result = check_all_kb(list(query), model, row)
            row.append(str(result))
            rows.append(row)
            return result
        else:
            result = check_all_kb(list(query), model, row)
            row.append(str(True))
            rows.append(row)
            return True
    else:
        p = symbols.pop()
        model_with_true = dict()
        model_with_true[p] = True
        model_with_true.update(model)
        model_with_false = dict()
        model_with_false[p] = False
        model_with_false.update(model)

        return tt_check_all(kb, query, symbols.copy(), model_with_false, rows) & tt_check_all(kb, query,
                                                                                                symbols.copy(),
                                                                                                model_with_true, rows)


def create_kb():
    knowledge_base = KnowledgeBase()
    with open("copy_paste.ini", "r") as file:
        for line in file:
            knowledge_base.tell(line)
    return knowledge_base

