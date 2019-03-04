print("Hello World")


class MakeClassDiagram:
    def __init__(self, filename):
        self.allMyClasses = []
        self.code = filename

    def count_occurrences(self, word, sentence):
        return sentence.lower().split().count(word)

    def find_classes(self):
        value = self.count_occurrences("class", self.code)

        for i in range (0, value):
            self.allMyClasses.append(self.code.split("class")[i + 1])


filename = """class MakeClassDiagram: def __init__(self, filename): self.allMyClasses = [] self.code = test
class Test:
class Test2:"""
mkd = MakeClassDiagram(filename)
mkd.find_classes()
print(mkd.allMyClasses)