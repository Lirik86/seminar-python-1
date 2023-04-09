try:
    ticket=int(input("Введите номер билета: "))
    if ticket<1000000 and ticket>99999:
        a=((ticket//1000)%10)+((ticket//10000)%10)+(ticket//100000)
        b=(ticket%10)+((ticket%100)//10)+((ticket%1000)//100)
        if a==b:
            print("Yes")
        else:
            print("No")
    else:
        print("Вы ввели не номер билета!")
except ValueError:
    print("Вы ввели не номер билета!")
