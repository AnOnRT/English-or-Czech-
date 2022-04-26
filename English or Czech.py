import math
from sys import stdin

en_freq = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153,
           0.772, 4.025, 2.406, 6.749,  7.507, 1.929, 0.095, 5.987, 6.327, 9.056,
           2.758, 0.978, 2.360, 0.150,  1.974, 0.074]

cz_freq = [8.421, 0.822, 0.740, 3.475, 7.562, 0.084, 0.092, 1.356, 6.073, 1.433,
           2.894, 3.802, 2.446, 6.468, 6.695, 1.906, 0.001, 4.799, 5.212, 5.727,
           2.160, 5.344, 0.016, 0.027, 1.043, 1.503]

l1=[]
ls=[]
for line in stdin:
    l1=line.split()
    ls.extend(c for c in l1)

l2=[]
s=''
for i in range(0,len(ls)):
    l2.extend(list(ls[i]))


letters=[]
for i in range(0,len(l2)):
    if(l2[i].isalpha()):
        letters.append(l2[i].lower())


quant=len(letters)

en_current_freq=26*[0]
cz_current_freq=26*[0]

for i in range(26):
    for j in range(len(letters)):
        if i==ord(letters[j])-97:
            en_current_freq[i]+=1/quant
            cz_current_freq[i]+=1/quant

sum_en=0
sum_cz=0
for i in range(26):
    sum_en += ((en_current_freq[i] - en_freq[i]/100)**2) / en_freq[i]
    sum_cz += ((cz_current_freq[i] - cz_freq[i]/100) ** 2) / cz_freq[i]


print("Match with English:","{:.2f}".format(sum_en*100))
print("Match with Czech:","{:.2f}".format(sum_cz*100))

t=min("{:.2f}".format(sum_en*100),"{:.2f}".format(sum_cz*100))
if(t=="{:.2f}".format(sum_en*100)):
    print("Text is in English")
else:
    print("Text is in Czech")
