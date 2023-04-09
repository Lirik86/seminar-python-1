try:
    num = int(input("Введите трех значное число: "))
    if num>99 and num<1000:
        a = num // 100
        b = (num // 10)%10
        c = num%10
        sum = a+b+c
        print(f"Сумма чисел трехзначного числа {num} равна {sum}")
    else: 
        print("Вы ввели не трехзначнное число!")
except ValueError:
    print("Вы ввели не трехзначнное число!")
