# Dərs 3 · Blok 1 — Python-un 10 kərpici
# İşə salma (de-praktikum qovluğundan): python src/l3_basics_start.py
# Dərsdə hər kərpicin kodunu slayddan öz bölməsinə yazırıq.
# Hər bölmə əvvəlcə öz başlığını çap edir — terminalda həmişə
# ən aşağıdakı bölməyə baxın. Tam kod dərsdən sonra Teams-də olacaq.

print("=== Kərpic 1 ===")   # Proqram — əmrlər ardıcıllığı
# TODO: print(...) ilə 4 sətir (slayd «Kərpic 1»)
print("Salam, data mühəndisliyi")
print("Baza stansiyası:", "BAK-0207")
print(2+3)
print("2+3")
print("=== Kərpic 2 ===")   # Dəyişən — adı olan qutu
# TODO: cell, rsrp, drops
cell = "BAK-0207"
rsrp =-95.5
print(cell, rsrp)

rsrp = -108.1
print(cell,rsrp)

drops = 2
drops = drops + 1
print("drops =", drops)
#name = input()
#age = input()
#number=int(age) + 1

#print("My name is" ,name, "and i am" ,age,"years old")

print("=== Kərpic 3 ===")   # Tiplər: int, float, str, bool, None
# TODO: type(...) və «mətn ≠ ədəd»
print(type(3))
print(type(-95.5))
print(type("BAK-0207"))
print(type (True))
print(type (None))
a = "-95.5"
b = -95.5
print(b + 10)
print(a + "10")
print(float (a)+10)
#print(float("N/A"))
print("=== Kərpic 4 ===")   # Müqayisə → True / False
# TODO: rsrp < -105, ==
# print(True>False)
#print (number>25)
print("=== Kərpic 5 ===")   # Siyahı (list)
# TODO: rsrp_list, indeks, len, orta
half_list = [4.5,5.5,6.5,7.5,7.6]
#half_input=input()
#half=int(half_input)
#print(half_list[half])
print("=== Kərpic 6 ===")   # Lüğət (dict)
# TODO: row = {...}, row["region"]
row={"soda":["Coca-Cola","Pepsi","Fanta"],"Fast Food":["pizza","pasta"]}
print(row["soda"])
print(row["Fast Food"])
row["dairy products"] = ["Milk", "Bread"]
print(row)
print("=== Kərpic 7 ===")   # Dövr (for) və şərt (if / else)
# TODO: zəif ölçmələri saymaq

print("=== Kərpic 8 ===")   # Funksiya: çağırmaq və yaratmaq
# TODO: round, len, max; def is_weak(rsrp)

print("=== Kərpic 9 ===")   # Nöqtə: metod
# TODO: name.strip().capitalize()

print("=== Kərpic 10 ===")  # import — hazır alət qutusu
# TODO: import math; import pandas as pd
