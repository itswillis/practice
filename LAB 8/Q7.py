class QuadraticEquation:
    def __init__(self, a=1, b=1, c=1):
        self.coefficients = [a, b, c]

    def get_coefficient(self, index):
        if index < 0 or index > 2:
            raise ValueError("Index must be 0, 1, or 2.")
        return self.coefficients[index]

    def has_solution(self):
        discriminant = self.get_discriminant()
        return discriminant >= 0

    def get_discriminant(self):
        a, b, c = self.coefficients
        return b ** 2 - 4 * a * c

    def get_root1(self):
        discriminant = self.get_discriminant()
        if discriminant < 0:
            return 0
        else:
            a, b, _ = self.coefficients
            return (-b + discriminant ** 0.5) / (2 * a)

    def get_root2(self):
        discriminant = self.get_discriminant()
        if discriminant < 0:
            return 0
        else:
            a, b, _ = self.coefficients
            return (-b - discriminant ** 0.5) / (2 * a)

    def __str__(self):
        discriminant = self.get_discriminant()
        if discriminant > 0:
            root1 = self.get_root1()
            root2 = self.get_root2()
            return f"Root 1: {root1:.2f}, Root 2: {root2:.2f}"
        elif discriminant == 0:
            root = self.get_root1()
            return f"One real solution: {root:.2f}"
        else:
            return "No real solutions!"
        
equation1 = QuadraticEquation(4, 4, 1)
print(equation1.has_solution())
print(equation1)
equation2 = QuadraticEquation()
print(equation2.has_solution())
print(equation2)
equation3 = QuadraticEquation(1, 2, -63)
print(equation3.has_solution())
print(equation3)