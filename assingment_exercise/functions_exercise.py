def triangle_area(base, height):
    area = (1/2)*base*height
    return area

def rectangle_area(length, width):
    area = length * width
    return area

def calculate_areas():
    try:
        default_shape = 1
        try:
            shape_input = int(input("your shape type\n(1. triangle\n 2. rectangle\n Default is trianlge)", ))
            default_shape = shape_input
        except:
            default_shape

        print(default_shape)

        if default_shape == 1:
            user_input = input("enter base and height ", )
            base, height = user_input.split(",")
            base = int(base)
            height = int(height)
            result = triangle_area(base, height)
            print(result)

        elif default_shape == 2:
            user_input = input("enter length and width ", )
            length, width = user_input.split(",")
            length = int(length)
            width = int(width)
            result = rectangle_area(length, width)
            print(result)
        else:
            print("Something went wrong")
    except:
        print("Something went wrong")


# calculate_areas()

def print_patterns(num):
    for i in range(1, num):
        s = ""
        for j in range(i):
            s += "*"
        print(s)

print_patterns(7)
