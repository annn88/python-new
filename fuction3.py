def is_right_triangle(side1,side2,side3):
    '''
    function to check the sides of a right triangle
    :param side1: side1 of a right triangle
    :param side2: side2 of a right triangle
    :param side3: side3 of a right triangle
    :return:check if the given sides are part of a triangle otherwise not
    '''
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2==sides[0]**2+sides[1]**2:
        return True
    return False

side1=int(input("enter the length of first side:"))
side2=int(input("enter the length of second side:"))
side3=int(input("enter the length of third side:"))
if is_right_triangle(side1,side2,side3):
    print(f"the given sides are part of a right angled triangle")
else:
        print(f"the given sides are not part of a right angled triangle")