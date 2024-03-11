def pascal_triangle(n):
    """
    Generate Pascal's Triangle of size n.

    :param n: Size of the triangle
    :type n: int
    :return: Pascal's Triangle as a list of lists
    :rtype: List[List[int]]
    """
    if n <= 0:
        return []

    triangle = [[1] * (i + 1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle

def print_triangle(triangle):
    """
    Print Pascal's Triangle.

    :param triangle: Pascal's Triangle
    :type triangle: List[List[int]]
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
