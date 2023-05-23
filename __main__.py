from app import Aplikace

app = Aplikace()

print("""----------------------
Evidence pojistěných
----------------------""")
while True:
    print("""Vyberte si akci:
1 - Přidat nového pojistěného
2 - Vypsat všechny pojistěné
3 - Vyhledat pojistěné
4 - Konec""")
    vstup = input().strip()
    if vstup == "1":
        jmeno = input("Jméno: ").strip()
        prijmeni = input("Příjmení: ").strip()
        vek = input("Věk: ").strip()
        cislo = input("Číslo: ").strip()
        pridano = app.pridat(jmeno, prijmeni, vek, cislo)
        if pridano:
            print("OK")
        else:
            print("Chybný vstup")

    elif vstup == "2":
        vypsat = app.vyhledat(None)
        for clovek in vypsat:
            print(clovek.to_string())

    elif vstup == "3":
        vyhledat = input("Napište jméno: ").strip()
        vypsat = app.vyhledat(vyhledat)
        for clovek in vypsat:
            print(clovek.to_string())

    elif vstup == "4":
        break
    else:
        print("Špatný vstup")
    print()
