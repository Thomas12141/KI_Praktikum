from Aufgabe15.Aufgabe15 import KnowledgeBase
from Aufgabe16.Aufgabe16 import check_all_kb

from tabulate import tabulate


def tt_check_all(kb: list, query, symbols: set, model: dict, rows: list):
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

        return tt_check_all(kb, query, symbols.copy(), model_with_false, rows) and tt_check_all(kb, query, symbols.copy(),
                                                                                          model_with_true, rows)


def create_kb():
    knowledge_base = KnowledgeBase()
    with open("copy_paste.ini", "r") as file:
        for line in file:
            knowledge_base.tell(line)
    return knowledge_base


headers = []
symbols = ["A", "B", "C", "D"]
for symbol in symbols:
    headers.append(symbol)
kb = create_kb()

for knowledge in kb.set:
    headers.append(str(knowledge))

print(tabulate([[str(True), str(True), str(True), str(True), str(True), str(True), str(True)]], headers=headers, tablefmt='orgtbl'))