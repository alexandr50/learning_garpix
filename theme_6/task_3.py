class Nikola:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        if self.name != 'Николай':
            self.name = f'Я не {self.name}, а Николай.'

n = Nikola(12, 'Max')
n1 = Nikola(12, 'Николай')
print(n.name)
print(n1.name)
