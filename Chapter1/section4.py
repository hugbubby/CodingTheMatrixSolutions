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

def t1():
    plot(S,4)

def t3():
    plot({1+2j+z for z in S}, 4)

def t8():
    plot(scale(S,(1/2)*1j))

def t9():
    plot(translate(scale(S, (1/2)*1j), 2 - 1j))
    
data = color2gray(file2image("./img01.png"))
pts = {(x-(1j*(y-len(data)))) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] < 120}

def t10():
    plot(pts, len(data))

#No idea what this task is even asking.
#def t11()
def t12():
    plot(scale({(x-(1j*(y-len(data)))) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] < 120},((1/2)*1j)), len(data))

def t17():
    plot([e**(2 * pi * 1j * (1/n)) for n in range(1,20)])

def t18():
    plot([s*e**((pi * 1j)/4) for s in S])

def t19():
    plot([s*e**((pi * 1j)/4) for s in pts], len(data))

def t20():
    plot([((s - 1j * len(data)/2 - len(data[0])/2)/2)*(e**((pi * 1j)/4)) for s in pts], len(data))

t20()
input()
