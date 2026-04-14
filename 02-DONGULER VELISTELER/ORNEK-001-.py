#Aşağıda verilen gramajlar listesi üzerinde bir for döngüsü kur.

#Eğer bir elmanın ağırlığı 150 gramdan büyükse ekrana "Büyük Elma: [gramaj] gr" yazdır.

#Eğer 150 gram ve altındaysa "Küçük Elma: [gramaj] gr" yazdır.

#Ekstra: Döngünün en sonunda, toplam kaç adet "Büyük Elma" olduğunu bir değişken kullanarak hesapla ve yazdır.

# gramajlar = [120, 185, 140, 210, 150, 195, 110]

gramajlar = [120, 185, 140, 210, 150, 195, 110]
buyuk_elma=[]
kucuk_elma=[]

for gramaj in gramajlar :

    if gramaj >150 :
        buyuk_elma.append(gramaj)


    else :
        kucuk_elma.append(gramaj)

print(f"Büyük Elma :  {buyuk_elma}gr")
print(f"Küçük Elma :{kucuk_elma}gr")

gramajlar.clear()

B_elma=len(buyuk_elma)
K_elma=len(kucuk_elma)
G_elma=len(gramajlar)

print(F"{B_elma} tane Büyük elma  var")
print(F"{K_elma} tane Büyük elma  var")
print(F"{G_elma} tane elma kaldı")