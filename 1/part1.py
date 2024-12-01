l1, l2 = [], []
while True:
    try:
        a,b = input().split("   ")
        l1.append(int(a))
        l2.append(int(b))
    except:
        break
l1.sort()
l2.sort()
sum = 0
for i,j in zip(l1,l2):
    sum += abs(i - j)
print(sum)
