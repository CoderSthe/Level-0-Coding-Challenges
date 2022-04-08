def calculate_area(side_a, side_b, side_c):

    semi_param = (side_a + side_b + side_c) / 2

    area = (semi_param * (semi_param - side_a) * (semi_param - side_b) * (semi_param - side_c)) ** 0.5

    return round(area, 2)

print("Area of triangle: ", calculate_area(4, 5, 6))