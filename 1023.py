from collections import Counter
n1 = int(input())
n2 = str(n1*2)
a = Counter(str(n1))
b = Counter(n2)
if a==b:
    print('Yes')
else:
    print('No')
print(n2)