import time
start =time.clock()
def get_hanmings(a=[]):
        start = 0
        c=[]
        b=[1,2,3,4,5]
        for i in b[start:]:
            for j in a[start:]:
                    c.append(i*j)
        
        start +=  1
        d = list(set(c))
        return d


a=[1,2,3,4,5]
pre_result = [1,2,3,4,5]
while pre_result[-1] <= 10**135:
    b = get_hanmings(a)
    a = list(set(b)-set(a))
    for i in a:
        pre_result.append(i)

result=[]
for i in pre_result:
    if i <= 10**100:
        result.append(i)
        
result.sort()
print('In range of 10**100, the count is %d ' % len(result))

end = time.clock()
print('Running time: %s Seconds'%(end-start))


