class ListWorker:
    def __init__(self, *args):
        self.args = args

    def return_digits(self):
        arr = []
        for i in self.args:
            if type(i) == int or type(i) == float:
                arr.append(i)
        return arr

    def return_str(self):
        arr = []
        for i in self.args:
            if type(i) == str:
                arr.append(i)
        return arr

    def not_str_and_digits(self):
        arr = []
        for i in self.args:
            if type(i) != str and type(i) != int and type(i) != float:
                arr.append(i)
        return arr


l = ListWorker(2, 4, 6, '9', 4.5, 'kdsjfnjgf', False, bool)
print(l.return_digits())
print(l.return_str())
print(l.not_str_and_digits())
