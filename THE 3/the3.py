def pattern_search(pattern,image):
    p_returner = [pattern]
    for n in range(3):
        p1 = []
        p_i=len(p_returner[-1])
        p_j = len(p_returner[-1][0])
        item = ""
        for j in range(p_j):
            for i in reversed(range(p_i)):
                item += p_returner[-1][i][j]
            p1.append(item)
            item =""
        p_returner.append(p1)
    for index,p in enumerate(p_returner):
        if index == 0:
            rot = 0
        elif index == 1:
            rot = 90
        elif index == 2:
            rot = 180
        elif index == 3:
            rot = 270
        i = 0
        l = len(p)
        li = len(image)
        find_j = 0
        find_i = 0
        kontrol = False
        counter = 0
        while i<li-l+1:
            if p[0] in image[i]:
                probs = []
                lii = len(image[i])
                lp = len(p[0])
                for m in range(0,lii-lp+1):
                    if image[i][m:lp+m] == p[0]:
                        probs.append(m)
                for prob in probs:
                    kontrol2 = True
                    kontrol3 = True
                    for j in range(1,len(p)):
                        if kontrol3:
                            if not(image[i+j][prob:prob+lp] == p[j]):
                                kontrol2 = False
                                kontrol3 = False
                                break
                    if kontrol2:
                        find_i = i
                        find_j = prob
                        kontrol = True
            else:
                counter += 1
            i+=1
        if kontrol and (counter <= li-l+1):
            return ((find_i,find_j,rot))
    return False

# P1 = ["ao3","nz1"]
# I = ["abcdEFgh","1234AB32","jEF89!.,","13181abc","AozcDEFG","BanHIJKL"]
# print(pattern_search(P1, I))


            


