year=int(input("Wpisz rok: "))
if year < 1582:
    print("Rok nie należy do kalendarza gregoriańskiego")
elif year % 4 != 0:
    print("Rok zwykly")
elif year % 4 == 0 & year % 100 != 0:
    print("Rok przestępny")
elif year % 100 == 0 & year % 400 != 0:
    print("Rok zwykły")
else:
    print("Rok przestępny")
    