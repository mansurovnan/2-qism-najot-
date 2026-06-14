# a = lambda x,y: x+y
# print(a(5,4))

# #2
# kvadrat = lambda x:x**2
# print(kvadrat(5))

# #3
# aniqlik = lambda x:"juft" if x%2==0 else "toq"
# print(aniqlik(8))
# #4
# uzunlik= lambda satr: len(satr)
# print(uzunlik("salom"))

# #5
# tariblash = lambda x, y, n: sorted([x,y,n])
# print(tariblash(9,5,8))
# #6
# satr= lambda: f'salom {input('ismni kiriting:')}'
# print(satr())

# #7
# talabalar = [
#     ("Ali", 85),
#     ("Vali", 100),
#     ("Hasan", 90),
#     ("Husan", 78)
# ]
# natija = sorted(talabalar, key=lambda talaba,: talaba[1])
# print(natija)

# #8
# sozlar = ["Ali", 'anbar','salom']

# natija = sorted(sozlar, key=lambda x:len(x))
# print(natija)

# #9
# sonlar = [

#      (89, 85),
#      (90, 100),
#      (50, 90),
#      (20, 78)
# ]
# natija = sorted(sonlar, key=lambda son: son[1])
# print(natija)

# #10
# mahsulotlar = [
#     ("Laptop", 1200),
#     ("Telefon", 800),
#     ("Quloqchin", 150),
#     ("Monitor", 450),
#     ("Klaviatura", 90)
# ]
# natija = sorted(mahsulotlar, key=lambda son: son[1])
# print(natija)

# #11
# talabalar = [
#     ("Ali", [80, 90, 85]),
#     ("Vali", [70, 75, 80]),
#     ("Hasan", [95, 90, 100]),
#     ("Husan", [85, 80, 75])
# ]
# natija = sorted(talabalar, key=lambda son: sum(son[1])/len(son[1]), reverse=True)
# print(natija)

# #12
# sonlar = [23, 45, 12, 87, 34, 91]
# natija = sorted(sonlar, key=lambda son: son%10, reverse=True)
# print(natija)

# #13
# fayllar = [
#     ("video.mp4", 1500),
#     ("photo.jpg", 300),
#     ("music.mp3", 700),
#     ("document.pdf", 200)
# ]
# natija = sorted(fayllar, key=lambda fayl,: fayl[1])
# print(natija)

# #14
# talabalar = [
#     ("Ali", 18, 85),
#     ("Vali", 17, 90),
#     ("Hasan", 18, 95),
#     ("Husan", 17, 80)
# ]
# natija = sorted(talabalar, key=lambda talaba:(talaba[1], talaba[2]))
# print(natija)

# #15
# odamlar = [
#     ("Ali", "Karimov"),
#     ("Vali", "Aliyev"),
#     ("Hasan", "Rasulov"),
#     ("Husan", "Ahmedi")
# ]

# natija = sorted(odamlar, key=lambda odam:(odam[-1]))
# print(natija)

# #16
# sonlar = [2, 3, 4, 5]
# natija = list(map(lambda x:x**3, sonlar))
# print(natija)

# #17
# ismlar = [
#     "Ali",
#     "Muhammad",
#     "Vali",
#     "Hasan",
#     "Abdulaziz",
#     "Oybek",
#     "Dilshod"
# ]
# natija = list(map(lambda x:len(x), ismlar))
# print(natija)

# #18
# mahsulotlar = [
#     "Telefon",
#     "Laptop",
#     "Monitor",
#     "Quloqchin",
#     "Klaviatura"
# ]

# natija = sorted(mahsulotlar, key= lambda x: x[0])
# print(natija)

# #19
# gap = "Python dasturlash tilini organish juda qiziqarli"
# print(list(map(len, gap.split())))

# #20
# sonlar = [23, 45, 12, 87, 34, 91]

# top = lambda sonlar: (max(sonlar), min(sonlar))

# print(top(sonlar))
i = int(input('son'))
a = 3
b=4



while a<=i:
    print(a)
    a, b = b, a+b
    
