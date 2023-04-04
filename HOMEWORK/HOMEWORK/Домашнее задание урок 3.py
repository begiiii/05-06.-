
#def calcPrimeNumbers():
#    myList = list();
#    listPrimeNumbers = list();


#    for i in range(2, 999+1):
#        myList.append(i)
        

#    for i in range(2,999+1):
#        for j in range(2,999+1):
#            if i == j or i == 1:
#                continue
#            if(j%i==0):
#                myList[j-2] = 0 #-2, потому что начинаем счет в цикле с 2, а не с нуля


#    for i in range(len(myList)):
#        if myList[i] != 0:
#            listPrimeNumbers.append(myList[i])

#    return listPrimeNumbers


#def containsIn(num):
#    if(calcPrimeNumbers().__contains__(num)):
#        return print(f"{num} простое число")
#    else:
#        return print(f"{num} не простое число")


#containsIn(11)
#containsIn(5)
#containsIn(25)
#containsIn(997)
#containsIn(801)


#print(calcPrimeNumbers())

#'''
#2. Даны два натуральных числа. Выяснить, в каком из них сумма цифр 
#больше. (Определить функцию для расчета суммы цифр натурального 
#числа.) 
#'''

#def sumDigits(a):
#    summ = 0
#    for x in range(len(str(a))):
#        n = a%10
#        summ+=n
#    return summ

#a = int(input("Введите первое число : "))
#b = int(input("Введите второе число : "))

#if(sumDigits(a)>sumDigits(b)):
#    print(f"{a} > {b}")
#elif(sumDigits(a)<sumDigits(b)):
#    print(f"{a} < {b}")
#else:
#    print(f"{a} = {b}")
    


'''
3. В списке получить все шестизначные счастливые номера. Счастливым 
называют такое шестизначное число, в котором сумма его первых трех 
цифр равна сумме его последних трех цифр. (Определить функцию для 
расчета суммы цифр трехзначного числа.)
Пример объявления списка:
myList = [333444, 1123345, 443344]
'''

def luckyNum(myList):
    print(str(myList[0])[0])
    
    newList = []

    for x in range(len(myList)):
        a =0
        b =0
        for i in range(2+1):
            a+=int(str(myList[x])[i])
        for i in range(3,5+1):
            b+=int(str(myList[x])[i])

        if a==b:
            newList.append(myList[x])
       

    return newList
    
myList = [333444, 1123345,443344]

print(luckyNum(myList))
