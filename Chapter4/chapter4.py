from vec import Vec
from mat import Mat
from matutil import listlist2mat, coldict2mat, mat2coldict
from GF2 import zero,one
from bitutil import bits2str, str2bits, mat2bits, bits2mat, noise
from image_mat_util import file2mat, mat2display

#Problem 4.6.12
def canBeTriangular(matrix):
    rows = list(matrix.D[0])
    row_zeroes = dict()
    columns = list(matrix.D[1])
    column_zeroes = dict()
    assert len(rows) == len(columns)
    n = len(rows)
    for i in range(n):
        num_zeroes = 0
        for j in range(n):
            if matrix[rows[i],columns[j]] == 0:
                num_zeroes = num_zeroes+1
        row_zeroes[rows[i]] = num_zeroes

    ret_rows = []
    for i in range(n-1, 0, -1):
        highest_index = list(row_zeroes.keys())[0]
        highest = row_zeroes[highest_index];
        for j in row_zeroes.keys():
            if highest < row_zeroes[j]:
                highest_index = j
                highest = row_zeroes[j]
        print(highest)
        if highest < i:
            return ([],[])
        ret_rows.append(highest_index)
        row_zeroes.pop(highest_index)

    for i in range(n):
        num_zeroes = 0
        for j in range(n):
            if matrix[rows[j],columns[i]] == 0:
                num_zeroes+=1
        column_zeroes[i] = num_zeroes
    
    ret_columns = []
    for i in range(n-1, -1, -1):
        highest_index = list(column_zeroes.keys())[0]
        highest = column_zeroes[highest_index]
        for j in column_zeroes.keys():
            if highest < column_zeroes[j]:
                highest_index = j
                highest = column_zeroes[j]
        if(highest < i):
            return ([],[])
        
        ret_columns.append(column_zeroes[highest_index])
        column_zeroes.pop(highest_index)

    matrix.pp(ret_rows.reverse(), ret_columns.reverse())
    return (ret_rows.reverse(), ret_columns.reverse())

#Task 4.14.1
G = listlist2mat([[one,zero,one,one],[one,one,zero,one],[zero,zero,zero,one],[one,one,one,zero],[zero,zero,one,zero],[zero,one,zero,zero],[one,zero,zero,zero]])

#Task 4.14.2
#print(G * Vec({0,1,2,3}, {0: one, 1: zero, 2: zero, 3: one})) # 0 0 one one 0 0 one

#Task 4.14.3
G_R = listlist2mat([[zero, zero, zero, zero, zero, zero, one],[zero, zero, zero, zero, zero, one, zero],[zero, zero, zero, zero, one, zero, zero],[zero, zero, one, zero, zero, zero, zero]])
#print(G_R * G) #Identity 4x4 matrix

#Task 4.14.4
H = listlist2mat([[zero, zero, zero, one, one, one, one], [zero, one, one, zero, zero, one, one], [one, zero, one, zero, one, zero, one]])
#print(H * G) #All zeroes.

#Task 4.14.5
def find_error(err_syndrome):
    ret = Vec({0,1,2,3,4,5,6}, {0: zero, 1: zero, 2: zero, 3: zero, 4: zero, 5: zero, 6: zero})
    err = H * err_syndrome
    H_dict = mat2coldict(H)
    for k in H_dict.keys():
        if(err == H_dict[k]):
            ret[k] = one
            break
    return ret

#Task 4.14.6
#c_received = Vec({0,1,2,3,4,5,6}, {1: one, 2: one, 3: one, 4: one, 6: one})
#print(c_received + find_error(H*c_received))

#Task 4.14.7
def find_error_matrix(S):
    return coldict2mat({key:find_error(mat2coldict(S)[key]) for key in mat2coldict(S).keys()})

#print(find_error_matrix(H))
#print(find_error_matrix(listlist2mat([[one, zero], [one, zero], [one, one]])))

#Task 4.14.8
s = ''.join([chr(i) for i in range(256)])
#print(bits2str(str2bits(s)) == s) #True

#Task 4.14.9
#print(mat2bits(bits2mat(str2bits(s))) == str2bits(s)) #True

#Task 4.14.10
neo_str = "I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it."
#neo_str = 'a'
P = bits2mat(str2bits(neo_str))

#Task 4.14.11
#print(bits2str(mat2bits(P + noise(P, 0.02))))

#Task 4.14.12
C = G * P
CTILDE = C + noise(C, 0.02)

#Task 4.14.13
#print(bits2str(mat2bits(G_R * CTILDE)))

#Task 4.14.14
def correct(A):
    return A + find_error_matrix(A)

#Task 4.14.15
#print(bits2str(mat2bits(G_R * correct(CTILDE))))
#Does not succeed in fixing all the corrupted characters, because sometimes there's more than one error per column.



