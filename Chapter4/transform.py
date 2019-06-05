from math import sin,cos,pi,atan
from mat import Mat
from matutil import listlist2mat, coldict2mat, mat2coldict
from image_mat_util import file2mat, mat2display

#Task 4.15.1
eliezer = file2mat("eliezer.png")
eliezer_l = eliezer[0]
eliezer_c = eliezer[1]

#Task 4.15.2
def identity():
    return Mat(({'x','y','u'},{'x', 'y', 'u'}), {('x','x'):1, ('y','y'):1, ('u','u'):1})
#print(eliezer_l == identity() * eliezer_l.copy()) #True

#Task 4.15.3
def translation(alpha, beta):
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), {('x', 'x'):1, ('x', 'u'): alpha, ('y', 'y'):1, ('y', 'u'):beta, ('u', 'u'): 1})

#Task 4.15.4
def scale(alpha, beta):
    return Mat(({'x','y','u'},{'x','y','u'}), {('x','x'): alpha, ('y','y'): beta, ('u','u'): 1})

#Task 4.15.5
def rotation(theta):
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), {('x', 'x'): cos(theta), ('y', 'x'): -sin(theta), ('x', 'y'): cos(theta + 3/2*pi), ('y', 'y'): -sin(theta + 3/2*pi), ('u', 'u'): 1})

#Task 4.15.6
def rotation_about(theta, x, y):
    return translation(x, y) * rotation(theta) * translation(-x, -y)

#Task 4.15.7
def reflect_y():
    return scale(1, -1)

#Task 4.15.8
def reflect_x():
    return scale(-1, 1)

#Tak 4.15.9
def scale_color(r, g, b):
    return Mat(({'r', 'g', 'b'}, {'r', 'g', 'b'}), {('r', 'r'): r, ('g', 'g'): g, ('b', 'b'): b})

#Task 4.15.10
def grayscale():
    return Mat(({'r', 'g', 'b'}, {'r', 'g', 'b'}), {('r', 'r'): 1/3, ('r', 'g'): 1/3, ('r', 'b'): 1/3, ('g', 'r'): 1/3, ('g', 'g'): 1/3, ('g', 'b'): 1/3, ('b', 'r'): 1/3, ('b', 'g'): 1/3, ('b', 'b'): 1/3})

#Task 4.15.11
def reflect_about(x1, y1, x2, y2):
    x = x2 - x1
    y = -(y2 - y1)
    theta = atan(y/x)
    print(theta)
    #return translation(-x1, -y1)
    #return rotation(theta) * translation(-x1, -y1)
    #return reflect_x() * rotation(theta) * translation(-x1, -y1)
    #return rotation(-theta) * reflect_x() * rotation(theta) * translation(-x1, -y1)
    return translation(x1, y1) * rotation(-theta + pi/2) * reflect_x() * rotation(theta - pi/2) * translation(-x1, -y1)

"""
eliezer_l_translated = translation(50, 50) * eliezer_l
eliezer_l_scaled = scale(1/2,1/2) * eliezer_l
eliezer_l_rotated = rotation(pi/4) * eliezer_l
eliezer_l_rotated_about = rotation_about(pi/2, 159, 189) * eliezer_l
eliezer_c_grayscale = grayscale() * eliezer_c
eliezer_l_reflected_about_1 = reflect_about(0, 0, 189, 189) * eliezer_l
eliezer_l_reflected_about_2 = reflect_about(80, 0, 81, 189) * eliezer_l
mat2display(eliezer_l_reflected_about_2, eliezer_c, xmin=-81, ymin=-189, crosshairs=True)
"""
