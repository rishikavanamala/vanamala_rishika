
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


# Example usage
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
symbol = input("Enter operation (add or subtract or multiply or divide): ")

calc = Calculator(a, b, symbol)
print("Result:", calc.calculate())
