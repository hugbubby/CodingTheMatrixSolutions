from vec import Vec

#Problem 3.8.1
def vec_select(veclist, k):
    return [v for v in veclist if v[k] == 0]

def vec_sum(veclist, D):
    return sum(veclist, Vec(D,{}))

def vec_select_sum(D, veclist, k):
    return vec_sum(vec_select(veclist, k), D)

D = {1,2,3,4,5}
v1 = Vec(D, {2 : 3, 4: 0, 5: 42})
v2 = Vec(D, {2 : 0, 4: 3, 5: 42})
v3 = Vec(D, {2 : 3, 4: 3, 5: 42})
v4 = Vec(D, {2 : 0, 4: 0, 5: 42})

"""
print(vec_select([v1, v2, v3, v4], 2)) #Prints list containing only v2,v4
print(vec_select([v1, v2, v3, v4], 4)) #Prints list containing only v1,v4
print(vec_select([v1, v2, v3, v4], 1)) #Prints list of all
print(vec_select([v1, v2, v3, v4], 5)) #Prints list of none

#Should all be true
print(vec_sum([v2, v4], D) == vec_select_sum(D, [v1,v2,v3,v4], 2))
print(vec_sum([v1, v4], D) == vec_select_sum(D, [v1,v2,v3,v4], 4))
print(vec_sum([v1, v2, v3, v4], D) == vec_select_sum(D, [v1,v2,v3,v4], 1))
print(vec_sum([], D) == vec_select_sum(D, [v1,v2,v3,v4], 5))
"""

#Problem 3.8.2
def scale_vecs(vecdict):
    return [(1/k) * vecdict[k] for k in vecdict.keys()]

"""
print(scale_vecs({2 : v1})) # Vec{D, {2 : 1.5, 4: 0.0, 5: 21}}
print(scale_vecs({4 : v1})) # Vec{D, {2 : 0.75, 4: 0.0, 5: 10.5}}
"""

#Problem 3.8.3 -- Returns a set, because sets are more appropriate for this problem than a list.
def GF2_span(D, L):
    if len(L) == 0:
        return [Vec(D, {})]
    else:
        ret = {l_start+l_rest for l_start in [Vec(D,{}), L[0]] for l_rest in GF2_span(D, L[1:])}
        for i in ret:
            for j in D:
                i[j] = i[j] % 2
        return ret

D = {0,1,2,3,4,5}
gf2_v1 = Vec(D, {0: 1, 1: 0, 2: 0})
gf2_v2 = Vec(D, {0: 0, 1: 1, 2: 0})
gf2_v3 = Vec(D, {0: 0, 1: 0, 2: 1})
gf2_v4 = Vec(D, {0: 0, 1: 1, 2: 1})

list_1 = GF2_span(D, [gf2_v1, gf2_v2, gf2_v3])
list_2 = GF2_span(D, [gf2_v1, gf2_v2])
list_3 = GF2_span(D, [gf2_v2, gf2_v4])
list_4 = GF2_span(D, {})
print("\nList one:")
for i in list_1:
    print(i)
print("\nList two:")
for i in list_2:
    print(i)
print("\nList three:")
for i in list_3:
    print(i)
print("\nList four:")
for i in list_4:
    print(i)
