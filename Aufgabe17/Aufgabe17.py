from nltk import Valuation, Assignment, Model, Tree
from nltk.sem.logic import *
#parser erzeugen.
bool_exp_parser = LogicParser(True)


#Der Baum
parse_result = bool_exp_parser.parse("(A & C -> B | D) & (A & C <-> B | D)"
                                     + "& (A -> C <-> B -> D) & (A | C <-> B | D)"
                                     + " & (A | C -> B & D)")
#Bildet ein Model
model = Model(set([]), Valuation([('A', True), ('B', True), ('C', False), ('D', False)]))
#Prüft ob dieser model diesen Baum auch erfüllt
print(model.satisfy(parse_result, Assignment(set([]))))
