sozluk = {}

adet = int(input("Sozluk kac elemanli?"))

for i in range(adet):
    ad = input("Ogrencinin adini giriniz:")
    no = int(input("Ogrencinin numarasini giriniz:"))
    sozluk[ad] = no
print(sozluk)


char = input("Yeni kayıt eklemek istiyorsaniz e , istemiyorsaniz h giriniz.")
while char == "e":
    if char == "e":
        ad = input("Ogrencinin adini giriniz:")
        sozluk[ad] = int(input("Ogrencinin numarasini giriniz:"))
        char = input("Yeni kayıt eklemek istiyorsaniz e , istemiyorsaniz h giriniz.")
    elif char == "h":
        break
    else:
        print("e veya h giriniz:")
        
print(sozluk)