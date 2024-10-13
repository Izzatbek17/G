# def avto_info(kompaniya,model,rangi,korobka,yili,narhi=None):
#     avto = {
#         'kompaniya':kompaniya,
#         'model': model,
#         'rangi': rangi,
#         'korobka': korobka,
#         'yili': yili,
#         'narhi': narhi,
#     }
#     return avto
#
# avto1 = avto_info('Nissan','R35','зелённый','mexanika',2012,3000)
# avto2 = avto_info('Toyota','Supra','oq','mexanika',2009)
# avtolar = [avto1,avto2]
# print('Onlay bozordagi mavjud avtomobilar:')
# for avto in avtolar:
#     narh = avto['narhi']
# else:
#     narh = "Nomalum"
# print(f"{avto['rangi']} {avto['model']} narhi {narh}")


# def oraliq(min,max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min +=1
#     return sonlar
# print(oraliq(5,10))


# def avto_info(kompaniya,model,rangi,korobka,yili,narhi=None):
#     avto = {
#         'kompaniya':kompaniya,
#         'model': model,
#         'rangi': rangi,
#         'korobka': korobka,
#         'yili': yili,
#         'narhi': narhi,
#     }
#     return avto
#
# avtolar = []
# while True:
#     kompaniya = input('kompaniya:')
#     model = input('model:')
#     rangi = input('rangi:')
#     korobka = input('korobka:')
#     yili = input('yili:')
#     narhi = input('narhi')
#
#     avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narhi))
#
#     javob = input('Yana qoshasizmi? (ha/yoq):')
#     if javob == 'no':
#         break
# print(avtolar)

#
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini qoying:")
#         baholar[ism]=baho
#     return baholar


def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()

ismlar = ['ali','vali']
katta_harf(ismlar)
print(ismlar)


# talabalar = ['ali','vali','hasan','husan']
# def bahola (ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting:")
#         baholar[baho]=ism
#     return  baholar
# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)
