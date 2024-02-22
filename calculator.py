class Calculator:
    def add(self, x, y):
        return x + y
    
    def multi(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero.")
    
    def subtract(self, x, y):
        result = x - y
        return result
