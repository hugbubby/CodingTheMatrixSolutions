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


# -- Section 6 -- #


#Task 2.6.9
def segment(pt1, pt2):
    return [addn(scalar_vector_mult(alpha*.01, pt1), scalar_vector_mult(1-alpha*.01,pt2)) for alpha in range(100)]

def particular_segment():
    plot(segment([3.5,3],[0.5,1]), 4)

# -- Section 12 -- #

f = open('voting_record_dump109.txt')
mylist = list(f)

#Task 2.12.1
def create_voting_dict(strlist):
    return {line.split(" ")[0] : [int(num) for num in line.split(" ")[3:]] for line in strlist}

#Task 2.12.2
def policy_compare(sen_a, sen_b, voting_dict):
    ret = 1
    record1 = voting_dict[sen_a]
    record2 = voting_dict[sen_b]
    for i in range(len(record1)):
        ret += record1[i] * record2[i]
    return ret

#Task 2.12.3
def most_similar(sen, voting_dict):
    highest_dot_product = 0
    ret = ""
    for person in voting_dict.keys():
        if(person != sen):
            product = policy_compare(sen,person,voting_dict)
            if ret == "" or product > highest_dot_product:
                highest_dot_product = product
                ret = person
    return ret

#Task 2.12.4
def least_similar(sen, voting_dict):
    lowest_dot_product = 0
    ret = ""
    for person in voting_dict.keys():
        if(person != sen):
            product = policy_compare(sen,person,voting_dict)
            if ret == "" or product < lowest_dot_product:
                lowest_dot_product = product
                ret = person
    return ret

voting_dict = create_voting_dict(mylist)

#Task 2.12.5
#print(most_similar("Chafee", voting_dict)) #Jefferson
#print(least_similar("Santorum", voting_dict)) #Feingold

#Task 2.12.7
def find_average_similarity(sen, sen_set, voting_dict):
    sum_of_product = 0
    for compared in sen_set:
        sum_of_product += policy_compare(sen, compared, voting_dict)
    return sum_of_product/len(sen_set)

democrats = {senator.split(" ")[0] for senator in mylist if senator.split(" ")[1] == "D"}

"""
most_similar = ""
highest = -1000000
for i in voting_dict.keys():
    similarity = find_average_similarity(i, democrats, voting_dict)
    if similarity > highest:
        highest = similarity
        most_similar = i

print(most_similar) #Biden
"""

#Task 2.12.8
def find_average_record(sen_set, voting_dict):
    sum_of_records = voting_dict[sen_set.pop()]
    for i in sen_set:
        sum_of_records = addn(sum_of_records, voting_dict[i])
    return [i/(len(sen_set)+1.0) for i in sum_of_records]


"""
average_democrat_record = find_average_record(democrats, voting_dict)
most_similar = ""
highest = -1000000
for i in voting_dict.keys():
    product = 1
    for j in range(len(average_democrat_record)):
        product += voting_dict[i][j] * average_democrat_record[j]
    if product > highest:
        highest = product
        most_similar = i

print(most_similar) #Biden
"""

#Task 2.12.9
def bitter_rivals(voting_dict):
    rivals = ["",""]
    lowest = 10000000000000
    for i in voting_dict.keys():
        for j in voting_dict.keys():
            if i != j:
                similarity = policy_compare(i,j,voting_dict)
                if lowest > similarity:
                    rivals = [i,j]
                    lowest = similarity

    return rivals

#print(bitter_rivals(voting_dict)) = Feingold and Inhofe

#Problem 2.14.8
def plot2DLine(p1, p2):
    plot([addn(scalar_vector_mult(0.01 * i, p1), scalar_vector_mult(1 - 0.01 * i, p2)) for i in range(100)], 5)

#plot2DLine([-1.5,2], [3,0])
#plot2DLine([2,1], [-2,2])

#Problem 2.14.10 -- in vec.py

