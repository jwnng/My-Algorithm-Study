"""
def solution(progresses, speeds):
    answer = []
    complete_day = []
    res = 0
    for i in range(len(progresses)):
        days = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            days += 1

            if progresses[i] >= 100:
                complete_day.append(days)
            
    ans = 1
    target = complete_day[0]
    for i in range(1,len(complete_day)):
        if target >= complete_day[i]:
            ans += 1
        else:
            answer.append(ans)   
            target = complete_day[i]
            ans = 1

    answer.append(ans)  
    return answer
"""

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
