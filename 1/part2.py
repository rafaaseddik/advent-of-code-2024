l1 = []
map = dict()
while True:
    try:
        a,b = input().split("   ")
        l1.append(int(a))
        map[int(b)] = map.get(int(b),0)+1
    except:
        break
sum = 0
for i in l1:
    sum += i * map.get(i,0)
print(sum)

