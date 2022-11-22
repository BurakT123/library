liste1 = ["elma", "armut", "portakal"]
liste2 = ["ayva", "mandalina", "karpuz", "kivi", "muz"]
liste = liste1 + liste2

liste.append("kiraz")
liste.insert(4, "vişne") #araya eleman ekleme
liste.remove("elma")
liste.pop(1) #sıradakini kaldırma
#.copy() liste kopyalam
#.count() bir elemandan kaçtane var?
#.extent()
#.index()

count1 = 1
text = ""
for meyve in liste:
    text = text + str(count1) + "." + meyve + " "
    count1 = count1 + 1
    if count1 - 1 == len(liste):
        print(text)

print()

count2 = 1
for meyve in liste:
    if count2 == 1:
        print("Listenin ilk meyvesi: " + meyve)
    elif count2 == len(liste):
        print("Listenin son meyvesi: " + meyve)
    count2 = count2 + 1

print()

print("Toplam meyve sayısı:" + str(len(liste)))

print()

liste.reverse()
print(liste)

print()

liste.sort()
print(liste)

print()

for i in range(0, len(liste)):
    liste.pop(0)

print(liste)
