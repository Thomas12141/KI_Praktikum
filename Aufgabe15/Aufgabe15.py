from nltk.sem.logic import LogicParser


class KnowledgeBase:

    def __init__(self):
        self.bool_exp_parser = LogicParser(True)
        self.set = []

    def tell(self, argument: str):
        self.set.append(self.bool_exp_parser.parse(argument))


def create_kb():
    knowledge_base = KnowledgeBase()
    knowledge_base.tell("A & C -> B | D")
    knowledge_base.tell("A & C <-> B | D")
    knowledge_base.tell("A -> C <-> B -> D")
    knowledge_base.tell("A | C <-> B | D")
    knowledge_base.tell("A | C -> B & D")

    return knowledge_base
