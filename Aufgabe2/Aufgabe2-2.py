class ProgrammingLanguages:
    def __init__(self):
        self.languages = []

    def add(self, language):
        self.languages.append(language)

    def __iter__(self):
        return iter(self.languages)


my_str = "Hello World"
my_list = [34, 54, 65, 78]
program_languages = ProgrammingLanguages()
program_languages.add("C++")
program_languages.add("Java")
program_languages.add("Python")
for b in my_str:
    print(b)
for e in my_list:
    print(e)
for prog in program_languages:
    print(prog)
