from the4 import construct_forest

def tester():

    with open("cases.txt" ,"r") as f:
        cases = f.readlines()

        with open("results.txt","r") as f:
            results = f.readlines()

            comparison = []
            for case, result in zip(cases,results):

                a = construct_forest(eval(case))
                b = eval(result)

                single_case_bool = []

                while b != []:
                
                    if b[0] in a:
                        a.remove(b[0])
                        b.pop(0)
                        single_case_bool.append(True)

                    else:
                        b.pop(0)
                        single_case_bool.append(False)  

                if a != []:
                    comparison.append(False)
                
                elif all(single_case_bool):
                    comparison.append(True)        
                
                else:
                    comparison.append(False)

    false_lines = []
    n=0
    for j in comparison:
        if j == False:
            false_lines.append(n+1)
            n +=1
        else:
            n +=1          

    if false_lines != []:
        print("False cases' line numbers are :" , false_lines)

    else:
        print("Well done! All true :)")
tester()
