a = float(input("Введите первое действительное число: "))
b = float(input("Введите второе действительное число: "))
c = float(input("Введите третье действительное число: "))
y = [a if 0 < a < 1 else None, b if 0 < b < 1 else None, c if 0 < c < 1 else None]
y = [num for num in y if num is not None]
print(y if y else "Нет подходящих чисел.")
