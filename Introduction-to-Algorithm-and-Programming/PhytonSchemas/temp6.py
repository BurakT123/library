a = int(input("Lütfen a sayısını yazınız"))
b = int(input("Lütfen b sayısını yazınız"))

if a == b:
    b = int(input("Lütfen b sayısını yazınız"))
    toplam = a + b
    cikarma = a - b
    carpma = a * b
    bolme = a / b
else:
    toplam = a + b
    cikarma = a - b
    carpma = a * b
    bolme = a / b
    
print("Toplam:", toplam)
print("Çıkarma:", cikarma)
print("Çarpma:", carpma)
print("Bölme:", bolme)