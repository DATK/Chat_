from src import sh
from random import randint

def rand_pas(les):
    st="1йцукенгшщзхъэждлорпавыфячсмиттьбю.234567890qazxswedcvfrtgbnhyujm,kiol./;p[']!@#$%^&*(_+-=QWERTYUIOPLKJJHGFDSA)ZXCVBNM"
    res=""
    for i in range(les):
        a=randint(0,len(st)-1)
        res+=st[a]
    return res
data=[]
data_hash=[]
data_name=[]
for i in range(1_000_0):
    data.append(rand_pas(randint(4,21)))
    data_name.append(rand_pas(randint(6,12)))
    
for j in range(len(data)):
    data_hash.append(sh.hash(data[j],data_name[j]))

count = 0   
for m in range(len(data_hash)):
    for n in range(m):
        if data_hash[m]==data_hash[n]:
            count+=1
            print(data_name[m],data_name[n],data[m],data[n],data_hash[m],data_hash[n],sep="   |||   ",end="\n\n")
    
print(count)