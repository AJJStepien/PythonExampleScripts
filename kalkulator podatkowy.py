z=True
while z:
    try:
        dochod=input("Wpisz kwotę dochodu: ")
        dochod = dochod.replace(",",".")
        dochod=float(dochod)
        z=False
    except:
        print("chyba wpisałeś coś nie tak :P")
        
if dochod <= 85528:
    podatek = (dochod * 0.18) - 556.2
    if podatek < 0:
        podatek=0.0
    print("Podatek wynosi 18%")
    print("Przyznana ulga: 556.2 talarów")
    print()
else:
    nadwyzka = dochod - 85528
    podatek = 14839.2 + (nadwyzka*0.32)
    print("Podatek wynosi 14839.2 talarów oraz 32% z nadwyżki ponad próg dochodowy")
    print("Zarobiłeś ", nadwyzka, "ponad próg dochodowy. Podatek od nadwyżki wynosi:", nadwyzka*0.32)
    print()
print("Podatek dochodowy wynosi: ", round(podatek), "talarów")
