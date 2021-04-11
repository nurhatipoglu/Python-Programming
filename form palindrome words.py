import numpy as np 
  
MAX_CHAR = 26
  
#freq [0] 'a' için, ...., freq [25] 'z' için
def countFreq(str, freq, n) : 
    for i in range(0, n) : 
        #Ord () işlevi, Unicode karakteri temsil eden bir tamsayı döndürür.
        freq[ord(str[i]) - ord('a')] += 1
        #freg dizisinin içini sayılarla dolduruyor
  
  
#Palindromik olup olmadığını kontrol etmek için durumlar.
#Palindromik veya palindromik değil şeklinde.
def PalindromYapilabilir(freq, n) : 
      
    #count_odd: hangi sıklıkta olduğunu saymak için
    count_odd = 0
    for i in range(0, MAX_CHAR) : 
        if (freq[i] % 2 != 0): 
            #freg dizisindeki değer tek ise
            count_odd += 1
  
    #çift uzunluktaki metin için
    if (n % 2 == 0): 
        if (count_odd > 0): 
            return False
        else: 
            return True
    
    #tek uzunluktaki metin için
    if (count_odd != 1): 
        return False
    return True
  
  
def BulveSil(freq) : 
    odd_char = 0
    for i in range(0, MAX_CHAR) : 
        if (freq[i] % 2 != 0): 
            #freq tek ise yeni harf ataması gerçekleşir
            freq[i] = freq[i] - 1
            odd_char = (chr)(i + ord('a')) 
            break
              
    return odd_char 
  
  
#ilk palindromik dizeyi bulmak için.
def PalindromBul(str, n) : 
    freq = np.zeros(26, dtype = np.int) 
    #içinde 26 tane 0 bulunan dizi oluşturuyor
    countFreq(str, freq, n) 
  
    #Bir palindromik dizenin 'str'nin karakterleri ile oluşturulup oluşturulamayacağını 
    #kontrol edilmesi.
    if (not(PalindromYapilabilir(freq, n))): 
        #palindrom olmadı
        return False
  
    #freq tek ise değer atanır, değilse boş değere sahiptir.
    odd_char = BulveSil(freq) 
  
    #kelimeyi baştan ve sondan yazdırmak için
    front_index = 0; rear_index = n - 1
  
    #palindrom kelimeyi alfabetik olarak yazmak için 
    for i in range(0, MAX_CHAR) : 
        if (freq[i] != 0) : 
            ch = (chr)(i + ord('a'))
            
            #kelimeyi tutmak için ikiye bölüp ön ve arka index ini tutalım
            for j in range(1, int(freq[i]/2) + 1): 
                str[front_index] = ch 
                front_index += 1
                  
                str[rear_index] = ch 
                rear_index -= 1
              
          
    #freq tek ise onu karşılık gelen indeksinde sakladık 
    if (front_index == rear_index): 
        str[front_index] = odd_char 
  
    #palindromik kelime oluşturulabilir.
    return True
  
  
#palindrom kelimeleri tersine çeviriyoruz.
def TersCevir( str, i, j): 
    while (i < j): 
        str[i], str[j] = str[j], str[i] 
        i += 1
        j -= 1
      
  
  
#aynı metnin karakterlerini kullanarak başka palindrom kelime bulmak
def SonrakiPalindrom(str, n) : 
    #girilen metnin uzunluğu 3 ten az ise palindrom kelime oluşturulamaz
    if (n <= 3): 
        return False
  
    #girilen metnin ortasındaki karekteri bulduk.
    mid = int (n / 2) - 1
      
    #ortadaki karakterden başlayıp alfabetik küçük olanı buluyoruz
    i = mid -1
    while(i >= 0) : 
        if (str[i] < str[i + 1]): 
            break
        i -= 1
  
    #eger kelime bulunmazsa False döndürür.
    if (i < 0): 
        return False
  
    #alfabetik olarak en küçük karakter bulunur ve sıralama.
    smallest = i + 1; 
    for j in range(i + 2, mid + 1): 
        if (str[j] > str[i] and str[j] < str[smallest]): 
            smallest = j 
  
    #en küçük ile karakter arasında yer değiştirme gerçekleşir
    str[i], str[smallest] = str[smallest], str[i] 
  
    #Dize bir palindrom olduğundan, aynı karakter değişimi metnin 2. yarısında yapılmalıdır.
    str[n - i - 1], str[n - smallest - 1] = str[n - smallest - 1], str[n - i - 1] 
  
    #Aralıktaki (i + 1) orta karaktere kadar ters karakter yerleştirilir
    TersCevir(str, i + 1, mid) 
  
    #N çift ise orta + 1 ile n-i-2 aralığındaki karakterleri ters çevirir
    if (n % 2 == 0): 
        TersCevir(str, mid + 1, n - i - 2) 
  
    else: 
        TersCevir(str, mid + 2, n - i - 2) 
  
    #alfabetik olarak daha yüksek palindromikdize oluşturulabilir True döner
    return True
  
  
#Tüm palindromik permütasyonları alfabetik olarak yazdırır
def PalindromYazdir(str, n) : 
      
    #str nin harflerinden ilk palindromik dizenin oluşturulup oluşturulamayacağını kontrol edilir
    if (not(PalindromBul(str, n))): 
        #palindromik kelime oluşturulamadı
        print ("-1") 
        return
      
    # Listeyi dizeye dönüştürme
    print ( "".join(str)) 
  
    # tüm palindromik permütasyonları yazdır
    while (SonrakiPalindrom(str, n)): 
        # Listeyi dizeye dönüştürme
        print ("".join(str)) 
          
#Kodu çalıştıralım
print("Hocam metni kendim oluşturdum bu kadar yapabildim")
str= "isdiidsi"
print("Metin:",str)
n = len(str) #metnin uzunluğu
  
#Diziyi listeye dönüştürürüz, böylece karakterlerin değiştirilmesi kolay olur
str = list(str) 
  
PalindromYazdir(str, n) 