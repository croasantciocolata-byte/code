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
