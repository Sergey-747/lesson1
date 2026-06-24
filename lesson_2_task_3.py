#Напишите функцию square , принимающую один аргумент 
# #— сторону квадрата — и возвращающую площадь квадрата.
#Если переданный аргумент был не целым, округлите результат вверх
import math

# def square(a):
#     sum = a ** 2
#     return sum

# a = float((input("Введите сторону длину стороны квадрата: ")))
# a_round = round(a)
# print("Площадь квадрата = ", math.ceil(square(a_round)))


def square(side):
    area = side ** 2
    return area    

side = math.ceil(float((input("Введите сторону длину стороны квадрата: "))))
print("Площадь квадрата = ", square(side))

