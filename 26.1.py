with open('26-j8.txt', 'r') as f:
    nums = f.readline()
    res = []
    for line in f.readlines():
        res.append(int(line))
res.sort()
summ = 0
for i in range(0, int(len(res)*0.7)):
    summ += res[i]
first1 = summ * 0.7
summ = 0
for i in range(int(len(res)*0.7), int(len(res))):
    summ += res[i]
second1 = summ * 0.6
summ = 0
for i in range(0, int(len(res)*0.5)):
    summ += res[i]
first2 = summ * 0.6
summ = 0

for i in range(int(len(res)*0.5), len(res)):
    summ += res[i]
second2 = summ * 0.65

final1 = first1 + second1
final2 = first2 + second2
if final1 > final2:
    print(int(final1 - final2), int(res[-1]*0.6))
else:
    print(int(final2 - final1), int(res[-1]*0.65))
    

    
    
        
        
        
