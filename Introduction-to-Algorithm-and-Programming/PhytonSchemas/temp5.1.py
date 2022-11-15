def writeA ():
    global a
    a = int(input("Lütfen a sayısını yazınız."))

def writeB ():
    global b
    b = int(input("Lütfen b sayısını yazınız."))
    if a == b:
        print("Lütfen sayıları aynı yazmayınız!")
        writeB()

writeA()
writeB()

toplama = a + b
if a < b:
    cikarma = b - a
else: 
    cikarma = a - b
carpma = a * b
bolme = float(a / b)
    
print("Toplama işlemi:", toplama)
print("Çıkarma işlemi:", cikarma)
print("Çarpma işlemi:", carpma)
print("Bölme işlemi:", bolme)

