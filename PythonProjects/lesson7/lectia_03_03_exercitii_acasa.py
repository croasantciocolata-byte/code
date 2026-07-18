if __name__=="__main__":
    print("Bun venit la lectia 03.3 - for, while (continuare)")


    # Exercitiul 1. Afisarea unui model de stele:
    """ *
        **
        ***
        ****
        *****"""
    # Folosind for


    # Folosind while


    # Exercitiul 2: Modificare a exercitiului 1: Scrie codul ca sa afisezea asa un 'brad', cu inaltimea n nivele - introdus de la tastiera
    """     *
           ***
          *****
         *******
        *********   """

    # Exercitiul 3: Scrie un cod care sa afiseze '*' pe diagonala principala a unei matrixi nxn,
    # si elementele mai sus de aceasta, si sa afiseze ' ' in triunghiul de mai jos de diagonala
    # penntru un orarecare n introdus de la tastatura, n fiind dimensiunea matricii nxn
    """*****
        ****
         ***
          **
           *"""


    # Exercitiul 4: Scrierea unui program care citeste o lista de numere de la tastatura si afiseaza suma si media lor
    # print("Exercitiul 3: Scrierea unui program care citeste o lista de numere de la tastatura si afiseaza suma si media lor")
    # # Folosind for, apoi folosind while






    # Exercitiul 5. Simularea aruncarii unei monede
    # Cu ajutorul functiei random, simuleaza 100 de aruncari de moneda si vezi de cate orie a iesit banul vs stema
    # import random
    # random.random() -> ne da un numar float intre 0 si 1

    import random
    print(random.randint(1, 1000))
    # banul = random.randint(1, 1000) >= 500
    # stema = random.randint(1, 1000) < 500
    nr_aruncari = 100
    banul = random.random() >= 0.5
    stema = random.random() < 0.5

    index_aleatoriu = random.randint(1, 10000)
    lista_partiticipanti = [] # 10000 nr de telefoate
    #lista_partiticipanti[index_aleatoriu]


    # Folosind for


    # Folosind while

    # Exercitiul 6. Cu ajutorul random.randint(1, max_vale) simulati rezultatul unui concurs in care castigatorul
    # se alege aleatoriu dintr-o lista de participanti care contine numele acestora