def stamps(a):
    p1,p2,p3 = 0, 0 ,0
    if a == 0:   return (p1,p2,p3)
    while a >= 5:
            a = a - 5
            p1+=1
    while a >= 2:
            a = a - 2
            p2+=1
    if a == 1: p3+=1
    return (p1,p2,p3)