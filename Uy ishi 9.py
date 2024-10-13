
# dostlar = {
#     "Ali": ["Terminator", "Rambo", "Titanic"],
#     "Vali": ["Tenet", "Inception", "Interstellar"],
#     "Hasan": ["Abdullajon", "Bomba", "Shaytanat"],
#     "Husan": ["Mahallada duv-duv gap", "John Wick"]
# }
#
# for dost, kinolar in dostlar.items():
#     print(f"{dost}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(f"- {kino}")
#     print()
#


# davlatlar = {
#     "O'zbekiston": {
#         "Poytaxt": "Toshkent",
#         "Hududi": "448978 kv.km",
#         "Aholisi": "33000000",
#         "Pul birligi": "so'm"
#     },
#     "Rossiya": {
#         "Poytaxt": "Moskva",
#         "Hududi": "17098246 kv.km",
#         "Aholisi": "144000000",
#         "Pul birligi": "rubl"
#     }
# }
#
#
# for davlat, malumotlar in davlatlar.items():
#     print(f"{davlat}\npoytaxti: {malumotlar['Poytaxt']}")
#     print(f"Hududi: {malumotlar['Hududi']}")
#     print(f"Aholisi: {malumotlar['Aholisi']}")
#     print(f"Pul birligi: {malumotlar['Pul birligi']}")




shaxslar = [
    {
        "ism": "Abu Abdulloh Muhammad ibn Ismoil",
        "tavallud_yili": 810,
        "manzil": "Buxoro",
        "umr": 60,
        "mashhur_asarlar": [
            "Al-jome as-sahih",
            "Al-adab al-mufrad",
            "At-tarix al-kabir",
            "At-tarix as-sag'ir"
        ]
    },
    {
        "ism": "Abdulla Qodiriy",
        "tavallud_yili": 1894,
        "manzil": "Toshkent",
        "umr": 44,
        "mashhur_asarlar": [
            "O'tkan kunlar",
            "Mehrobdan Chayon",
            "Obid ketmon"
        ]
    },
    {
        "ism": "Erkin Vohidov",
        "tavallud_yili": 1936,
        "manzil": "Farg'ona",
        "umr": 80,
        "mashhur_asarlar": [
            "Tong nafasi",
            "Qo'shiqlarim sizga",
            "O'zbegim",
            "Qiziquvchan Matmusa"
        ]
    },
    {
        "ism": "Alisher Navoiy",
        "tavallud_yili": 1441,
        "manzil": "Xirot",
        "umr": 61,
        "mashhur_asarlar": [
            "Xamsa",
            "Lison ut-Tayr Mahbub Al-Qulub",
            "Munoint"
        ]
    }
]


for shaxs in shaxslar:
    print(f"{shaxs['ism']} ({shaxs['manzil']}, {shaxs['tavallud_yili']}-yil) - {shaxs['umr']} yil umr ko'rgan")
    print("Mashhur asarlari:")
    for asar in shaxs['mashhur_asarlar']:
        print(f"- {asar}")

