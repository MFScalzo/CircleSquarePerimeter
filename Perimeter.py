def perimeter(shape, num):
    squareVal = shape == 's'
    circleVal = shape == 'c'

    return (num * squareVal * 4) + (num * circleVal * 6.28)

print(perimeter("s",7))
print(perimeter("c",4))
print(perimeter("c",9))