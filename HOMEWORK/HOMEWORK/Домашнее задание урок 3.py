
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
#                myList[j-2] = 0 #-2, ������ ��� �������� ���� � ����� � 2, � �� � ����


#    for i in range(len(myList)):
#        if myList[i] != 0:
#            listPrimeNumbers.append(myList[i])

#    return listPrimeNumbers


#def containsIn(num):
#    if(calcPrimeNumbers().__contains__(num)):
#        return print(f"{num} ������� �����")
#    else:
#        return print(f"{num} �� ������� �����")


#containsIn(11)
#containsIn(5)
#containsIn(25)
#containsIn(997)
#containsIn(801)


#print(calcPrimeNumbers())

#'''
#2. ���� ��� ����������� �����. ��������, � ����� �� ��� ����� ���� 
#������. (���������� ������� ��� ������� ����� ���� ������������ 
#�����.) 
#'''

#def sumDigits(a):
#    summ = 0
#    for x in range(len(str(a))):
#        n = a%10
#        summ+=n
#    return summ

#a = int(input("������� ������ ����� : "))
#b = int(input("������� ������ ����� : "))

#if(sumDigits(a)>sumDigits(b)):
#    print(f"{a} > {b}")
#elif(sumDigits(a)<sumDigits(b)):
#    print(f"{a} < {b}")
#else:
#    print(f"{a} = {b}")
    


'''
3. � ������ �������� ��� ������������ ���������� ������. ���������� 
�������� ����� ������������ �����, � ������� ����� ��� ������ ���� 
���� ����� ����� ��� ��������� ���� ����. (���������� ������� ��� 
������� ����� ���� ������������ �����.)
������ ���������� ������:
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
