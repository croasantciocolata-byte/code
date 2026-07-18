    # 5. Verificați dacă o listă este subsecvență a altei liste.
    # Exemplu: lista ['a', 'b', 'c'] este subsecventa a listei ['a', 'b', 'c', 'd', 'e'] dar nu este secventa a listei ['a', 'b', 'f', 'c', 'd', 'e']
print("Verificați dacă o listă este subsecvență a altei liste.")
lista1 = ['a', 'b', 'c']
lista2 = ['a', 'b', 'c', 'd', 'e']
lista3 = ['a', 'b', 'f', 'c', 'd', 'e']

index_lista1 = 0  
for elem in lista2:
    if index_lista1 < len(lista1) and elem == lista1[index_lista1]:
        index_lista1 += 1  
    if index_lista1 == len(lista1):
        break  


este_subsecventa_lista2 = index_lista1 == len(lista1)

index_lista1 = 0  
for elem in lista3:
    if index_lista1 < len(lista1) and elem == lista1[index_lista1]:
        index_lista1 += 1  
    if index_lista1 == len(lista1):
        break  

este_subsecventa_lista3 = index_lista1 == len(lista1)

print("Lista ['a', 'b', 'c'] este subsecvență a listei ['a', 'b', 'c', 'd', 'e']:", este_subsecventa_lista2)
print("Lista ['a', 'b', 'c'] este subsecvență a listei ['a', 'b', 'f', 'c', 'd', 'e']:", este_subsecventa_lista3)