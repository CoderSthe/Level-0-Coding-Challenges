# This function calculates the area of a triangle

def calculate_area(side_a, side_b, side_c):

    # Calculate the semi-parameter
    semi_param = (side_a + side_b + side_c) / 2

    # Calculate the area of triangle
    area = (semi_param * (semi_param - side_a) * (semi_param - side_b) * (semi_param - side_c)) ** 0.5

    return area

a = float(input("Enter Side A Length: "))
b = float(input("Enter Side B Length: "))
c = float(input("Enter Side C Length: "))
print("Area of triangle: ", calculate_area(a, b, c))