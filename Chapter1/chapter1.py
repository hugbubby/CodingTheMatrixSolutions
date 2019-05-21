from plotting import plot
from image import file2image,color2gray
from math import pi,e

S = {2+2j,3+2j,1.75+1j,2+1j,2.25+1j,2.5+1j,2.75+1j,3+1j,3.25+1j}

def scale(S, factor):
    return {x*factor for x in S}

def rotate(S):
    return {x*1j for x in S}

def translate(S, added):
    return {x+added for x in S}


# -- Section 4 -- #


#Task 1.4.1
def t1():
    plot(S,4)

#Task 1.4.3
def t3():
    plot({1+2j+z for z in S}, 4)

#Task 1.4.8
def t8():
    plot(scale(S,(1/2)*1j))

#Task 1.4.9
def t9():
    plot(translate(scale(S, (1/2)*1j), 2 - 1j))
   

data = color2gray(file2image("./img01.png"))
pts = {(x-(1j*(y-len(data)))) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] < 120}

#Task 1.4.10
def t10():
    plot(pts, len(data))

#No idea what this task is even asking.
#Task 1.4.11
#def t11()

#Task 1.4.12
def t12():
    plot(scale({(x-(1j*(y-len(data)))) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] < 120},((1/2)*1j)), len(data))

#Task 1.4.17
def t17():
    plot([e**(2 * pi * 1j * (1/n)) for n in range(1,20)])

#Task 1.4.18
def t18():
    plot([s*e**((pi * 1j)/4) for s in S])

#Task 1.4.19
def t19():
    plot([s*e**((pi * 1j)/4) for s in pts], len(data))

#Task 1.4.20
def t20():
    plot([((s - 1j * len(data)/2 - len(data[0])/2)/2)*(e**((pi * 1j)/4)) for s in pts], len(data))


# -- Section 5 -- #


ciphertext = [21, 4, 21, 11, 25, 3, 11, 21, 4, 25, 26]
def intToChar(num):
    if num == 26:
        return ' '
    else:
        return chr(ord('A') + num)

#Task 1.5.1
def t1():
    for i in range(32):
        k = ''
        for j in [intToChar(x ^ i) for x in ciphertext]:
            k += j
        print(k) # EVE IS EVIL


# -- Section 7 -- #


#Problem 1.7.1
def my_filter(L, num):
    return [x for x in L if (x % num) != 0]

#Problem 1.7.2
def my_lists(L):
    return [[y for y in range(1,x+1)] for x in L]

#Problem 1.7.3
def my_function_composition(f,g):
    return {x : g[f[x]] for x in f.keys()}

#Problem 1.7.4
def mySum(L):
    current = L.pop()
    for i in L:
        current = current + i
    return current

#Problem 1.7.5
def myProduct(L):
    current = L.pop()
    for i in L:
        current = current * i
    return current

#Problem 1.7.6
def myMin(L):
    current = L[0]
    for i in L:
        current = current - (abs(current - i) + (current - i))/2
    return current

#Problem 1.7.7
def myConcat(L):
    current = ""
    for i in L:
        current += i
    return current

#Problem 1.7.8
def myUnion(L):
    current = {0} & {1}
    for i in L:
        current = current | i
    return current

"""
#Test print statements
print("my_filter :", my_filter([1,2,4,5,7], 2))
print("(1) my_lists: ", my_lists([1,2,4]))
print("(2) my_lists: ", my_lists([0]))
print("my_function_composition: ", my_function_composition({0:'a', 1:'b'}, {'a':'apple', 'b':'banana'}))
print("mySum: ",mySum([1,2,3,4,5]))
print("myProduct: ",myProduct([2,2,2,2,2]))
print("myMin: ", myMin([5,-100,3,4,5]))
print("myConcat: ", myConcat(["this", "is", "my", "code"]))
print("myUnion: ", myUnion([{"my"}, {"my"}, {"code"}, {"code"}, {"this"}, {"is"}]))
"""

#Problem 1.7.9
#print(mySum([])) = Undefined!
#print(myProduct([])) = Undefined!
#print(myMin([])) = Undefined!
#print("myConcat([]): ", myConcat([])) = []
#print("myUnion([]): ", myUnion([])) = []

#Problem 1.7.12-1
def procedure_transform(a,b,L):
    return [a*z + b for z in L]
