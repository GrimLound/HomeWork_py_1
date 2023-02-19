# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
"""
number = input("Введите трехзначное число: ")
summ = 0
for i in number:
    summ += int(i)
print(summ)
"""
#--------------------------------------------------------------

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
"""
count = int(input("Введите число подходящее под условие: "))
if count >= 6 and count % 6 == 0:
    print(f"Петя сделал - {int((count / 3) / 2)}шт. Катя сделала - {int((count / 3) * 2)}шт."
          f" Сережа сделал - {int((count / 3) / 2)}шт.")
else:
    print("Введенное Вами число не подходит под условие!")
"""
#--------------------------------------------------------------