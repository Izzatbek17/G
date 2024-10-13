# son = 1
# while son<=5:
#     print(son,end=' ')
#     son = son+1
#
# while True:
#     print("01",end="")

# savol = "Istalgan son kiriting"
# savol = "(darur toxtash uchun 'exit' deb yozing):"
# qiymat = ''
# while qiymat != 'exit':
#     qiymat=input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# sonlar = list(range(1,5))
# for son in sonlar:
#     if son==5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# ismlar = []
# n=1
# while True:
#     savol = f"{n}-dostingizni ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana dostingizni qoshasizmi? (ha/yoq)")
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         break
#
# print("Dostlaringiz royxat:")
# for ism in ismlar:
#     print(ism.title())

# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("dostingizni ismini kiriting:")
#     yosh = input(f"{ism.title()}ning yoshini kiriting:")
#     dostlar[ism] = int(yosh)
#
#     javob = input ("Yana dostingizni qoshasizmi? (ha/yoq):")
#     if javob == 'no':
#           ishora = False
#
# for ism,yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# cars = ['toyota','nissan','mazda','toyota','bmw',]
# while 'toyota' in cars:
#     cars.remove('toyota')
# print(cars)

talabalar = ['Botir','Asad','Javohir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting:")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = baho
print(baholangan_talabalar)