x = int(input("Lütfen 1. dersi yazınız. \n"))
y = int(input("Lütfen 2. dersi yazınız. \n"))
z = int(input("Lütfen 3. dersi yazınız. \n"))

ort = int((x + y + z) / 3)
if ort < 50:
    durum = "Kaldı"
elif ort == 50:
    durum = "50 ile geçti..."
else:
    durum = "Geçti"

if ort < 50:
    kod = "FF"
elif ort < 58:
    kod = "DD"
elif ort < 65:
    kod = "DC"
elif ort < 75:
    kod = "CC"

print("Durum:", durum)
print("Ortalaması:", ort)
print("Ortalamasının kodu:", kod)