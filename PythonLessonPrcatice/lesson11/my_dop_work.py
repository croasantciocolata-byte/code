if __name__=="__main__":
    print("Bun venit la tema pentru acasa 04.03 - lucru cu seturi si tupluri ")

    ###################### TUPLURI ######################

    # ------------------ Exercițiul 1 ------------------
    print(
        "Exercițiu 1: Scrie o functie care, dat fiind tuplul 'temperaturi' = (22, 25, 17, 19, 30, 21), calculează și afișează temperatura medie.")

    temperaturi = (22, 25, 17, 19, 30, 21)
    def temperatura_medie(temperaturi):
        for i in range(len(temperaturi)):
            suma = temperaturi + temperaturi[i]
            media = suma / len(temperaturi)
            return media
    print(temperatura_medie(temperaturi))    
    

    print("Temperatura medie este:", temperatura_medie(temperaturi = (22, 25, 17, 19, 30, 21)))

    # ------------------ Exercițiul 2 ------------------
    print(
        "Exercițiu 2: Scrie o funcție care, dat fiind tuplul 'zile_saptamana' cu zilele săptămânii, afișează zilele de weekend.")
    def afiseaza_weekend(zile_saptamana):
        pass
    print("Zilele de weekend sunt:",
          afiseaza_weekend(('Luni', 'Marți', 'Miercuri', 'Joi', 'Vineri', 'Sâmbătă', 'Duminică')))

    # ------------------ Exercițiul 3 ------------------
    print(
        "Exercițiu 3: Scrie o funcție care, dat fiind tuplul 'numere' = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), creează un nou tuplu care să conțină doar numerele pare.")
    def filtreaza_pare(numere):
        pass
    print("Numerele pare din tuplu sunt:", filtreaza_pare((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

    # ------------------ Exercițiul 4 ------------------
    print(
        "Exercițiu 4: Scrie o funcție care, dat fiind tuplul 'info' = ('Ion', 'Popescu', 34), unde primele două elemente sunt numele și prenumele unei persoane, iar al treilea element este vârsta, formatează și afișează un șir de caractere 'Numele complet al persoanei este Ion Popescu și are 34 ani.'")
    def formateaza_mesaj(info):
        pass
    print(formateaza_mesaj(('Ion', 'Popescu', 34)))

    # ------------------ Exercițiul 5 ------------------
    print(
        "Exercițiu 5: Scrie o funcție care calculează modulul (absolute value) diferenței primului și celui de-al doilea element al tuplului 'tuplu'.")
    # Nota: modul sau valoarea abosluta se calculeaza cu abs(nr)
    # exemplu: abs(-1) este 3
    def calculeaza_modul(tuplu):
        pass
    print("Valoarea absoluta este:", calculeaza_modul((2, 5)))

    # ------------------ Exercițiul 6 ------------------
    print(
        "Exercițiu 6: Scrie o funcție care, folosind tuplul 'valori' = (100, 200, 300, 400, 500), schimbă valoarea celui de-al treilea element în 350 și afișează tuplul modificat.")

    def modifica_tuplu(valori):
        pass
    print("Tuplul modificat:", modifica_tuplu((100, 200, 300, 400, 500)))

    # ------------------ Exercițiul 7 ------------------

    print("""
    Exercițiu 7: Mini-joc "Găsește comoara"

    Condiții:
    - Harta jocului este reprezentată printr-un tuplu de tupluri, fiecare element putând fi 'pământ', 'apă' sau 'comoară'.
    - Jucătorul introduce coordonatele în format 'x y' (exemplu: 0 1) pentru a căuta comoara.
    - Jocul răspunde dacă jucătorul a găsit comoara, a dat de apă sau este pe pământ uscat.
    - După fiecare încercare, jocul oferă un indiciu dacă jucătorul se apropie sau se îndepărtează de comoara.
    - Scopul jocului este să găsească comoara cu cât mai puține încercări posibile.

    Pentru a începe jocul, jucătorul trebuie să ruleze funcția 'joaca_joc' cu harta jocului și coordonatele comorii ca argumente.
    """)

    print("""
    Exemplu de hartă 5x5 pentru mini-jocul "Găsește comoara":

    P = Pământ
    A = Apă
    C = Comoară

    Harta:
    P P P P P
    P A A A P
    P A C A P
    P A A A P
    P P P P P

    Legenda:
    - 'P' reprezintă pământul.
    - 'A' reprezintă apa.
    - 'C' este locația comorii.
    """)

    # Soluția simplificată pentru mini-jocul "Găsește comoara" fără folosirea try/except

    # Harta jocului este un tuplu de tupluri
    harta = (
        ('P', 'P', 'P', 'P', 'P'),
        ('P', 'A', 'A', 'A', 'P'),
        ('P', 'A', 'C', 'A', 'P'),
        ('P', 'A', 'A', 'A', 'P'),
        ('P', 'P', 'P', 'P', 'P')
    )

    # Coordonatele comorii (presupunem că știm unde este comoara pentru demonstrație)
    x_comoara, y_comoara = 2, 2  # Comoara este la coordonatele (2, 2)


    # Funcția pentru a juca jocul
    def joaca_joc(harta, x_comoara, y_comoara):
        print("Bine ai venit la jocul 'Găsește comoara'!")
        print("Harta are dimensiunea 5x5. Introdu coordonatele în format 'x y' (ex: 2 2) pentru a căuta comoara.")
        incercari = 0

        pass


    joaca_joc(harta, x_comoara, y_comoara)

    ################### SETURI ###################
    # ------------------ Exercițiul 1 ------------------
    print(
        "Exercițiu 1: Scrie o functie care, at fiind un set 'numere_intregi' cu numere întregi pozitive și negative, creează o funcție care să returneze un set cu toate numerele pozitive, fiecare scăzut cu cel mai mic număr pozitiv.")
    numere_intregi = {1, -1, 2, -2, 3, -3}
    def normalizeaza_pozitive(set_input):
        pass
    print(normalizeaza_pozitive(numere_intregi))

    # ------------------ Exercițiul 2 ------------------
    print(
        "Exercițiu 2: Creează o funcție care primește un set de string-uri și returnează un set cu toate anagramele posibile pentru fiecare string din setul inițial.")
    # Nota: Pentru a calcula toate permutarile unui sir de caractere poti folosi functia permutations in felul urmator
    # from itertools import permutations
    # print(permutations(s))
    def genereaza_anagrame(set_stringuri):
        pass


    print(genereaza_anagrame({"abc", "def"}))


    # ------------------ Exercițiul 3 ------------------
    print(
        "Exercițiu 3: Scrie o funcție care să primească un set de numere întregi și să returneze suma diferenței dintre fiecare pereche de numere.")
    # Nota: diferenta dintre doua poate fi negativa
    # de exemplu: 2-3 este -1, dar noi suntem interesati sa adunam valorile pozitive, in acesta caze 1 inloc de -1
    # in asa caz folosim functia modul - abs() - in engleza absolute value:
    # asadar abs(2-3) este 1
    def suma_diferentelor(set_input):
        pass

    print(suma_diferentelor({1, 3, 5}))


    # ------------------ Exercițiul 4 ------------------
    print(
        "Exercițiu 4: Scrie o functie care, dat fiind un set de tuple, unde fiecare tuplu conține (nume, vârstă), scrie o funcție care să returneze un set cu numele persoanelor cu vârsta peste 18 ani.")
    def filtreaza_majori(set_input):
        pass
    persoane = {("Ion", 15), ("Ana", 22), ("Vasile", 18)}
    print(filtreaza_majori(persoane))

    # ------------------ Exercițiul 5 ------------------
    print(
        "Exercițiu 5: Scrie o funcție care să primească două seturi de numere și să returneze produsul cartezian al acestora sub forma unui set de tuple.")
    def produs_cartezian(set1, set2):
        pass

    print(produs_cartezian({1, 2}, {3, 4}))

    # ------------------ Exercițiul 6 ------------------
    print(
        "Exercițiu 6: Scrie o functie care, dat fiind un set 'numere', scrie o funcție care să returneze un set cu toate numerele prime din setul inițial.")
    def filtreaza_prime(set_input):
        pass

    print(filtreaza_prime({1, 2, 3, 4, 5, 6, 7, 8, 9}))

    # ------------------ Exercițiul 7 ------------------
    print(
        "Exercițiu 7: Creează o funcție care să primească un set de numere și să returneze un set cu toate numerele Fibonacci mai mici sau egale cu cel mai mare număr din set.")

    def filtreaza_fibonacci(set_input):
        pass


    print(filtreaza_fibonacci({1, 2, 3, 4, 5, 8, 13, 21}))


    # ------------------ Exercițiul 8 ------------------
    print("""
    Exercitiu 8: Scrie of functie pentru Exercițiu Joc: "Vânătoarea de numere"

    Condiții:
    - La începutul jocului, sistemul generează un set de 5 numere întregi aleatoare, ascunse, în intervalul 1-20.
    - Jucătorul are la dispoziție 10 încercări pentru a ghici toate numerele ascunse.
    - În fiecare încercare, jucătorul introduce un număr între 1 și 20.
    - Dacă numărul ales se află în setul de numere ascunse și nu a fost deja ghicit, jucătorul primește un mesaj de confirmare și numărul de numere rămase de ghicit.
    - Dacă numărul a fost deja ghicit în încercările anterioare, jucătorul este informat că numărul a fost ales anterior.
    - Dacă numărul ales nu se află în setul de numere ascunse, jucătorul este încurajat să încerce din nou.
    - Jocul se încheie când jucătorul a ghicit toate numerele ascunse sau când a epuizat cele 10 încercări.
    - La sfârșitul jocului, jucătorul este informat câte numere a ghicit și care erau numerele ascunse.

    Scopul jocului este să stimuleze gândirea logică și să ofere o modalitate distractivă de a practica lucrul cu seturile în Python.
    """)

    # Importăm modulul pentru a genera numere aleatoare
    import random

    # Generăm setul de numere aleatoare
    numere_ascunse = set(random.sample(range(1, 20), 5))  # Generează un set de 5 numere întregi aleatoare între 1 și 20


    # Funcția pentru a juca jocul
    def ghiceste_numerele_joc(numere_ascunse):
        print("Bine ai venit la 'Vânătoarea de numere'!")
        print("Am ascuns 5 numere între 1 și 20. Ai 10 încercări să le găsești pe toate.")

        ghicite = set()  # Set pentru a păstra numerele ghicite corect
        incercari = 0

        pass


    ghiceste_numerele_joc(numere_ascunse)


if __name__ == "__main__":
    print("Bun venit la tema 06.03 - object oriented programming")

    # ================== OOP, Clase, Mostenire ==================
    # ------------------ Exercițiul 1 ------------------
    print("Defineste o clasa 'Carte' cu atributele 'titlu' si 'autor'.")


    # Solutie


    # ------------------ Exercițiul 2 ------------------
    print("Adauga o metoda 'afiseaza_info' la clasa 'Carte' care afiseaza titlul si autorul.")


    # Solutie


    # ------------------ Exercițiul 3 ------------------
    print("Creeaza o clasa 'Autor' cu atributele 'nume' si 'nationalitate'.")


    # Solutie


    # ------------------ Exercițiul 4 ------------------
    print("Adauga o metoda 'afiseaza_biografie' la clasa 'Autor' care afiseaza numele si nationalitatea.")


    # Solutie


    # ------------------ Exercițiul 5 ------------------
    print("Creeaza o clasa 'Biblioteca' care contine o lista de carti disponibile.")


    # Solutie


    # ------------------ Exercițiul 6 ------------------
    print("Modifica clasa 'Carte' pentru a include anul publicarii si metoda 'afiseaza_info' pentru a-l afisa.")


    # Solutie


    # ------------------ Exercițiul 7 ------------------
    print("Creeaza o subclasa 'Ebook' a clasei 'Carte' care adauga un atribut 'format_fisier'.")


    # Solutie

    # ------------------ Exercițiul 8 ------------------
    print("Adauga o metoda 'afiseaza_info' la clasa 'Ebook' care include si formatul fisierului.")


    # Solutie

    # ------------------ Exercițiul 9 ------------------
    print(
        "Creeaza o clasa 'Imprumut' care gestioneaza imprumuturile cartilor din biblioteca (inclusiv data imprumutului si data returnarii).")
    # Solutie


    # ------------------ Exercițiul 10 ------------------
    print("Modifica clasa 'Biblioteca' pentru a gestiona imprumuturile, inclusiv adaugarea si returnarea cartilor.")


    # Solutie

    # ------------------ Exercițiul 11 ------------------
    """
    Condiția Detaliată a Exercițiului - Jocul "Arena Eroilor"
    Scop: Dezvoltă un joc de luptă numit "Arena Eroilor", în care jucătorii selectează eroi din diferite clase de 
    caractere pentru a concura într-o arenă. Fiecare clasă de caracter va avea abilități unice, demonstrând utilizarea 
    moștenirii în programarea orientată pe obiect pentru a specializa și extinde comportamentele de bază.

    Clase de Implementat:

    Clasa de bază Erou: Aceasta este clasa de bază din care vor deriva toate celelalte clase de caractere. Va conține 
    atributele și metodele comune tuturor eroilor.

    Atribute:
    - nume: Numele eroului.
    - viata: Punctele de viață ale eroului, inițializate la 100.
    Metode:
    - ataca(adversar): O metodă ce primește ca argument un alt erou (adversarul) și îi scade viața în funcție de atacul 
    efectuat. Implementarea inițială va fi generică, specifică fiecărei clase de erou.
    - este_viu(): Returnează True dacă eroul are puncte de viață mai mare decât 0, altfel False.
    Clasa Razboinic: Derivată din clasa Erou, reprezentând un erou care excellează în lupta corp la corp.

    Metode Suplimentare:
    - ataca(adversar): Suprascrie metoda ataca din clasa de bază pentru a reflecta daune mai mari, datorită abilităților 
    de războinic.
    Clasa Arcas: O altă clasă derivată din Erou, caracterizată prin atacuri la distanță.

    Metode Suplimentare:
    - ataca(adversar): Suprascrie metoda ataca pentru a utiliza o săgeată, provocând daune adaptate la stilul său de 
    luptă.
    Clasa Mag: Derivată din Erou, această clasă folosește magia pentru a ataca, având potențialul de a provoca daune 
    masive.

    Metode Suplimentare:
    - ataca(adversar): Suprascrie metoda ataca, reflectând capacitatea sa de a folosi vraji puternice contra adversarilor.
    Funcționalitate Suplimentară:

    Lupta între eroi: Implementează o funcție lupta(eroi), unde eroi este o listă ce conține instanțe ale clasei Erou (și 
    subclasele sale). Funcția va alege aleatoriu doi eroi din listă, care vor lupta unul împotriva celuilalt până când 
    unul dintre ei rămâne fără viață. Lupta se desfășoară prin apeluri alternative ale metodei ataca între cei doi eroi, 
    până când unul dintre ei este învins.
    """
