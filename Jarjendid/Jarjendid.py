spisok=[] #Tühi loetelu(list)
num=[1,2,3,4,5]
abc=["Abc","B","C"]
slovo="Programmeerimine"
slovo_list=list(slovo)
print(slovo) #Sõna
print(slovo_list) #Tähtede kaupa

while True:
    valik=int(input("1 - добавить букву в список\n2 - склеить списки\n3 - добавить буквы на i - позицию\n4 - удалить букву\n"))
    if valik==1:
        a=input("Введи букву\n")
        slovo_list.append(a) #Lisab loendi lõppu elemendi
        print(f"Добавили {a}, новый список", slovo_list)
    elif valik==2:
        slovo_list.extend(abc) #Laiendab nimekirja, lisades lõppu kõik nimekirja elemendid
        print(slovo_list) 
    elif valik==3:
        a=input("Введи букву, которую хочешь добавить")
        i=int(input("Введи номер позиции, куда хочешь добавить буквы\n"))
        slovo_list.insert(i-1,a) #0,1,2..
        print(slovo_list)
    elif valik==4:
        a=input("Введи букву, которую хочешь удалить\n")
        n=slovo_list.remove(a)
    else:
        print("Искомой буквы нет")
    print(slovo_list)



