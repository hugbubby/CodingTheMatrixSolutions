from plotting import plot

def addn(v, w):
    return [v[i] + w[i] for i in range(len(v))]

def scalar_vector_mult(alpha, v):
    return [alpha * v[i] for i in range(len(v))]


# -- Section 3 -- #


#Task 2.3.1
L = [[2,2], [3,2], [1.75,1], [2,1], [2.25,1], [2.5,1], [2.75,1], [3,1], [3.25,1]]
def face_by_vectors():
    plot(L,4)


# -- Section 4 -- #


#Task 2.4.3
def face_translated():
    plot([addn(v, [1,2]) for v in L], 4)


# -- Section 5 -- #


#Task 2.5.4
def face_scaled():
    plot([scalar_vector_mult(0.5,l) for l in L], 4)
    plot([scalar_vector_mult(-0.5,l) for l in L], 4)
