# Last task from task.py
birthdate = ("year", "month", "day")
student = {
    "name": "Nico",
    "age": "20",
    "email": "someone@gmail.com",
    "birthdate": birthdate
}
interests = {"football", "basketball", "football", "tennis"}
student["interests"] = interests

print(student)
print("----")

# All tasks from Task_11_9.py
# Task1
fructe = ["mar", "banana", "cirese"]
# 2
print(fructe[1])
# 3
print(fructe[-1])
# 4
fructe.append("portocala")
print(fructe)
# 5
fructe.insert(2 , "kiwi")
print(fructe)
# 6
fructe.append("ananas")
fructe.append("struguri")
print(fructe)
# 7
print(fructe.index("cirese"))
# 8
fructe.remove("kiwi")
print(fructe)

# 9
fructe.sort()
print(fructe)
# 10
fructe.reverse()
print(fructe)
# 11
fructe.pop()
print(fructe)
# 12
print(len(fructe))
# 13
fructe[0] = 'mango'
print(fructe)
# 14
new_list = ['papaya', 'pepene']
vr = fructe + new_list
print(vr)
# 15
del vr[2]
print(vr)
# 16
vr.sort(reverse = True)
print(vr)
# 17
print(vr[:3])
print("----")
# 18
for i in fructe:
    print(i)
print("----")

#19
lists = ['morcov', 'telina']
lista_imbricata = [fructe, lists]
print(lista_imbricata)
# 20
print(lista_imbricata[1][1])
print("----")

# Task2
# 1
lista = [4, 5, 6]
suma = 0
for i in lista:
    suma += i
print(suma)
print("----")

# 2
lista = [1, 'x', 3]
print('x' in lista)
print("----")

# 3
text = 'radar'
reversed_text = text[::-1]
if text == reversed_text:
    print("Este palindrom")
else:
    print("Nu e palindrom")
print("----")

#4
lista = [1, 2, 3, 4, 5]
sorted_list = sorted(lista)
if lista == sorted_list:
    print("Lista e sortata crescator")
else:
    print("Lista nu e sortata crescator")
print("----")

# 5
lista1 = ['a', 'b', 'c']
lista2 = ['a', 'b', 'c', 'd', 'e']

# am facut verificarea, daca lista2 e mai mica, atunci nu are sens sa verific cu lista 1
lenght_1 = len(lista1)
lenght_2 = len(lista2)
if lenght_1 > lenght_2:
    print("Lista 1 e mai scurta decat lista 2, verificarea nu sa reusit face")
    exit()

# codul nu face ceea ce trebuie...ideea este, dar nu inteleg cum sa aplic
index_stop = 0
for i in lista1:
    for j in lista2[index_stop]:
        if i == j:
            index_stop += 1
            print(True)
            break
        else:
            print(False)


# aceasta pare pana ce cea mai corecta, pana ce
"""if lista1[0] == lista2[0] and lista1[1] == lista2[1] and lista1[2] == lista2[2]:
    print("True")
else:
    print("False")"""
    
"""Lista data, desi e conform cerintelor, nu este efectiva pentru verificarea subsecventei altei liste.
Deoarece daca lista2 ar fi fost lista2 = ['r', 'a', 'b', 'c', 'd', 'e'], atunci in acest caz ar fi returnat False pentru ca primul caracter
din lista1 nu corespunde cu primul caracter din lista1
Cred ca ar fi fost mai bine sa se parcurga mai intai fiecare caracter prin for
sa se verifice daca caracterul din lista1 corespunde cu unul din caracterele listei2
si daca urmatoarul caracter din lista1 corespunde cu lista2, si daca urmatorul caracter din lista1 corespunde cu lista2 atunci e True
altfel e False.
"""
