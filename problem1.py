
class Calculator:
    def __init__(self, a, b, symbol):
        self.a = a
        self.b = b
        self.symbol= symbol

    def calculate(self):
        if self.symbol == "add":
            return self.a + self.b
        elif self.symbol== "subtract":
            return self.a - self.b
        elif self.symbol == "multiply":
            return self.a * self.b
        elif self.symbol == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "divison by zero is not possiable"
        else:
            return "this is the invalid operation"


a = float(input("Enter the first digit: "))
b = float(input("Enter the second digit: "))
symbol = input("Enter operation (add or subtract or multiply or divide): ")

calc = Calculator(a, b, symbol)
print("Result:", calc.calculate())
