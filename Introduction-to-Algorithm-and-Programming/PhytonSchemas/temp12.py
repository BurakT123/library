import math

a = math.sqrt(4) #hangi sayının karesi olduğunu gösterir (kök alma)

b = math.ceil(2.6) #artı yönde sayıyı yukarı yuvarlamaya yarar.
b1 = -math.ceil(2.6) #eksi yönde sayıyı yukarı yuvarlamaya yarar.

c = math.floor(2.6) #artı yönde sayıyı aşağı yuvarlamaya yarar.
c1 = -math.floor(2.6) #eksi yönde sayıyı aşağı yuvarlamaya yarar.

d = math.pow(5, 2) #sayısının karesini almayı sağlar (5 üzeri 2)
d1 = math.pow(25, 1/2) #hangi sayının karesi olduğunu gösterir (kök alma)
d2 = math.pow(27, 1/3) #hangi sayının karesi olduğunu gösterir (kök alma)
d3 = math.pow(36, 1/3)
d4 = math.pow(6, 2/3)

e = math.trunc(2.9) # küsüratı (ondalıklı kısmı) atar.
e1 = math.trunc(2.3) # küsüratı (ondalıklı kısmı) atar.

f = math.log10(100)
f1 = math.log(100, 10)
f2 = math.log(100, 2.71)

g = math.sin(math.radians(30))
g1 = math.cos(math.radians(60))
g2 = math.tan(math.radians(45))
g3 = 1 / math.tan(math.radians(45))

#print(a)
#print(b, b1)
#print(c, c1)
#print(d, d1, d2, d3, d4)
#print(e, e1)
#print(f, f1, f2)
#print(g, g1, g2, g3)

text = ""
for i in range(0, 45 + 1):
    h = math.sin(math.radians(i))
    h1 = math.cos(math.radians(i))
    h2 = math.tan(math.radians(i))
    if (h2 == 0):
        h3 = "tanımsız"
    else: 
        h3 = 1 / math.tan(math.radians(i))
    text = text + str(i) + " derece: \n" + str(h) + " " + str(h1) + " " + str(h2) + " " + str(h3) + "\n\n"
    
#print(text)

i = math.degrees(math.asin(0.5))
i1 = math.degrees(math.acos(0.5))
i2 = math.degrees(math.atan(0.5))
i3 = math.degrees(1 / math.atan(1))

print(i, i1, i2, i3)



