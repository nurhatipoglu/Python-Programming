from random import randint
random = []
sum=0
for i in range(0,20):
    random.append(randint(1,100))
    sum = sum+ random[i]
print("Liste:",random)
print("Toplam:",sum)
print("Ortalama",(sum/20))

sayac=0
for i in range(0,20):
    if random[i] %2 ==0:
        sayac = sayac+1
print("Listedeki çift sayı sayısı:",sayac)

max = random[0]
for i in range (1,20):
    if random[i] >max:
        max = random[i]
    
print("En buyuk 1.eleman:",max)

min = random[0]
for j in range (1,20):
    if random[j] <min:
        min = random[j]
    
print("En kucuk 1.eleman:",min)
random.remove(max)
random.remove(min)

max2 = random[0]
for l in range (1,18):
    if random[l] >max2:
        max2 = random[l]
    
print("En buyuk 2.eleman:",max2)

min2 = random[0]
for m in range (1,18):
    if random[m] <min2:
        min2 = random[m]
    
print("En kucuk 2.eleman:",min2)
