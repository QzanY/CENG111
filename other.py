def insert(liste,x):
    if len(liste) == 0:
        return [x]
    if x<=liste[0]:
        return [x] + liste
    else:
        return [liste[0]] + insert(liste[1:],x)
def insertion_sort(liste):
    if len(liste) <= 0:
        return []
    else:
        return insert(liste[0],liste[1:])

######################################################

def helper(start,n,prev1,prev2):
    if start == n:
        return prev1 + prev2
    else:
        return helper(start+1,n,prev1+prev2,prev1)
def fibonacci(n):
    if n ==0 or n == 1:
        return n
    else:
        return helper(2,n,1,0)

######################################################

def helper2(n,results):
    if results[n] < 0:
        results[n] = helper2(n-1,results) + helper2(n-2,results)
    else:
        return results[n]
def fib(n):
    result = [0,1] + [-1] * (n-1)
    return helper2(n,result)

#######################################################

def helperr(L,eleman):
    if L == []:
        return [] 
    else:
        return [[eleman],L[0]] + helperr(L[1:],eleman)

def power(L):
    if L == []:
        return [[]]
    asd = power(L[1:])
    return helperr(asd,L[0]) + asd

#######################################################

def helper3_lcs(seq1,seq2,res):
    if len(seq1)*len(seq2) == 0:
        return res
    else:
        if seq1[0] == seq2[0]:
            return helper3_lcs(seq1[1:],seq2[1:],res+seq1[0])
        else:
            return helper3_lcs(seq1[1:],seq2[1:],res)

def LCS(seq1,seq2):
    if len(seq1)*len(seq2) == 0:
        return ""
    else:
        return helper3_lcs(seq1,seq2,"")

########################################################

def seq_search(x,L):
    for i in L:
        if x == L:
            return True
    return False

#########################################################

def bubble_sort(liste):
    lenn = len(liste)
    changed = True
    while changed:
        changed = False
        index = 0
        while index < lenn -1:
            if liste[index] > liste[index+1]:
                liste[index] , liste[index+1] = liste[index+1], liste[index]
                changed = True
            index += 1
    return liste
# a = [1,5,3,2,-1,6,20,10,9,-6,18]
# print(bubble_sort(a))
# print(a) ---> a is changed

##########################################################

def selection_sort(liste:list):
    index = 0
    while index < len(liste)-1:
        j = liste.index(min(liste[index:]))
        liste[index],liste[j] = liste[j],liste[index]
        index+=1
    return liste

###########################################################

def maxind(liste):
    maxx = liste[0]
    res = 0
    for i,item in enumerate(liste):
        if item>maxx:
            maxx = item
            res = i
    return res

def pancake_sort(liste:list):
    L = len(liste)
    for i in range(0,L):
        max_index = maxind(liste[0:L-i])
        liste[0:max_index+1] = liste[0:max_index+1][::-1]
        liste[0:L-i] = liste[0:L-i][::-1]
    return liste

############################################################

def counting_sort(liste):
    limit = max(liste)
    counts = [0] * limit
    for element in liste:
        counts[element-1] += 1
    for i in range(1,limit):
        counts[i] += counts[i-1]
    result = [0] * len(liste)
    for item in liste:
        result[counts[item-1]-1] = item
        counts[item-1] -=1
    return result
    
a = [1,5,3,2,6,20,10,9,18,6,6,18,20]
print(counting_sort(a))

def count_sort(liste):
    count = [0]*max(liste)
    for a in liste:
        count[a-1] +=1
    result=[]
    for i,x in enumerate(count):
        result.extend([i+1]*x)
    return result

def max_index(liste):
    maxx = liste[0]
    index = 0
    for i,x in enumerate(liste):
        if x>maxx:
            maxx = x
            index = i
    return index

def pancake_sort(liste):
    L = len(liste)
    for i in range(L):
        maxindex = max_index(liste[:L-i])

        liste[0:maxindex+1] = liste[0:maxindex+1][::-1]
        liste[:L-i] = liste[:L-i][::-1]
    return liste

    

