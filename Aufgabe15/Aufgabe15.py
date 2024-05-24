from nltk.sem.logic import LogicParser

bool_exp_parser = LogicParser(True)
knowledge_base = []
knowledge_base.append(bool_exp_parser.parse("A & C -> B | D"))

knowledge_base.append(bool_exp_parser.parse("A & C <-> B | D"))

knowledge_base.append(bool_exp_parser.parse("A -> C <-> B -> D"))

knowledge_base.append(bool_exp_parser.parse("A != C <-> B = D"))

knowledge_base.append(bool_exp_parser.parse("A = C -> B & D"))