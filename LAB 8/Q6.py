class QuadraticEquation:
    def __init__(self, a=1, b=1, c=1):
        self.coefficients = [a, b, c]

    def get_coefficient(self, index):
        if index < 0 or index > 2:
            raise ValueError("Index must be 0, 1, or 2.")
        return self.coefficients[index]

equation1 = QuadraticEquation(1, 2, 1)
print(equation1.coefficients)
equation2 = QuadraticEquation()
print(equation2.coefficients)
print(equation1.get_coefficient(0))
print(equation1.get_coefficient(1))
print(equation1.get_coefficient(2))
print(type(equation1))