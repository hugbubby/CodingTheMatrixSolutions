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

#Problem 1.7.9
#print(mySum([])) = Undefined!
#print(myProduct([])) = Undefined!
#print(myMin([])) = Undefined!
print("myConcat([]): ", myConcat([]))
print("myUnion([]): ", myUnion([]))

#Problem 1.7.12-1
def procedure_transform(a,b,L):
    return [a*z + b for z in L]
