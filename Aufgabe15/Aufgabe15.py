from nltk.sem.logic import LogicParser


def create_kb():
    bool_exp_parser = LogicParser(True)
    knowledge_base = [bool_exp_parser.parse("A & C -> B | D"), bool_exp_parser.parse("A & C <-> B | D"),
                      bool_exp_parser.parse("A -> C <-> B -> D"), bool_exp_parser.parse("A | C <-> B | D"),
                      bool_exp_parser.parse("A | C -> B & D")]

    return knowledge_base
