from nltk import Model, Valuation, Assignment

from Aufgabe15.Aufgabe15 import create_kb


def check_all_kb(kb: set, model: Model) -> bool:
    for knowledge in kb:
        if not model.satisfy(knowledge, Assignment(set([]))):
            return False
    return True


knowledge_base = create_kb()

model = Model(set([]), Valuation([('A', True), ('B', True), ('C', False), ('D', False)]))

print(check_all_kb(knowledge_base, model))
