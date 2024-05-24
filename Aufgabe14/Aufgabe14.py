from nltk import Valuation, Assignment, Model, Tree
from nltk.sem.logic import *
#parser erzeugen.
bool_exp_parser = LogicParser(True)
#Der Baum
parse_result = bool_exp_parser.parse("(A | B | C) & (A | B | -C) & (-A | B | C) & (-A | -B | C)")
#Bildet ein Model
model = Model(set([]), Valuation([('A', True), ('B', True), ('C', True), ('D', True)]))
#Prüft ob dieser model diesen Baum auch erfüllt
print(model.satisfy(parse_result, Assignment(set([]))))

#Und bildet stärker als oder, Negation stärker als und
