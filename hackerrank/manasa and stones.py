def stones(n, a, b):
    # a_count + b_count = n-1
    answer = []
    if a>b:
        a_count = 0
        b_count = n-1
        while a_count<= n-1:
            tmp = a_count*a+b_count*b
            if tmp not in answer:
                answer.append(tmp)
            a_count+=1
            b_count-=1
    else:
        a_count = n-1
        b_count = 0
        while a_count>= 0:
            tmp = a_count*a+b_count*b
            if tmp not in answer:
                answer.append(tmp)
            a_count-=1
            b_count+=1
    return answer