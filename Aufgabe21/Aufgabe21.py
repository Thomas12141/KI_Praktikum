from nltk.sem.logic import LogicParser
from tabulate import tabulate

from Aufgabe15.Aufgabe15 import KnowledgeBase
from Aufgabe19.Aufgabe19 import tt_check_all

kb = KnowledgeBase()

kb.tell("-P11")
kb.tell("B11<->(P12|P21)")
kb.tell("B21<->(P11|P22|P31)")
kb.tell("-B11")
kb.tell("B21")


headers = []
symbols = ["P11", "B11", "P12", "P21", "P22", "P31", "B21"]
for symbol in symbols:
    headers.append(symbol)

for knowledge in kb.set:
    headers.append(str(knowledge))

rows = []

bool_exp_parser = LogicParser(True)
headers.append("P12")
headers.append("entails")
tt_check_all(kb.set, {bool_exp_parser.parse("P12")}, symbols.copy(), dict(), rows)
print(tabulate(rows, headers=headers, tablefmt='orgtbl'))
