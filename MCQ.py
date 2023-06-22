def mcq(questions):
    lent=len(questions)
    marks=0
    skip=0
    marks2=0
    skip2=0
    
    for j in range(lent):
        i=j
        print('i1= ',i)
        marks=0
        while i<lent:
            marks+=questions[i][0]
            skip+=questions[i][1]
            #print('marks1= ',marks)
            #print('skip= ',skip)
            i=questions.index(questions[i])+skip+1
            print('i= ',i)
        print('marks= ',marks)
        if marks>marks2:
            marks2=marks
            marks=0
    print(marks2)
    #print(marks)
    #print(marks2)
    #print(marks)
mcq([[1,1],[2,2],[3,3],[4,4],[5,5]])
    
        