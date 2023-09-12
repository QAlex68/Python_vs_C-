# Дополнительная задача:
# Задача 61: Вывести первые N строк треугольника
# Паскаля. Сделать вывод в виде равнобедренного
# треугольника

def generate_pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        triangle.append(row)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle


def print_pascal_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))


n = int(input("Введите количество строк треугольника Паскаля: "))
pascal_triangle = generate_pascal_triangle(n)
print_pascal_triangle(pascal_triangle)