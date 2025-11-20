import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def found_error(self):
        if not (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a):
            raise ValueError("Not found this Triangle")
        # if self.a <= 2 and self.b <= 2 and self.c <= 2:
        #     raise ValueError("The numbers have a benn > 2")

    def return_pages(self):
        return f"sm of pages {self.a} to {self.b} to {self.c}"

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        self.found_error()
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def triangle_type(self):
        self.found_error()
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.a == self.c:
            return "isoscene"
        else:
            return "scalene"

    def is_right(self):
        self.found_error()
        a, b, c = sorted([self.a, self.b, self.c])
        return abs(a * a + b * b - c * c) < 1e-9

    def angles(self):
        self.found_error()

        a, b, c = self.a, self.b, self.c

        A1 = math.degrees(math.acos((b * b + c * c - a * a) / (2 * b * c)))
        B1 = math.degrees(math.acos((a * a + c * c - b * b) / (2 * a * c)))
        C1 = math.degrees(math.acos((a * a + b * b - c * c) / (2 * a * b)))

        return A1, B1, C1


t = Triangle(3, 4, 5)
print(t.triangle_type())
print(t.angles())
