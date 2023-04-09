try:
    sum=int(input("Введите общее число журавликов: "))
    malchiki= (sum//3)//2
    katya= sum-malchiki*2
    print(f"Катя сделала журавликов {katya}, Петя и Сережа сделали журавликов по {malchiki} на каждого.")
except ValueError:
    print("Вы ввели не число!")