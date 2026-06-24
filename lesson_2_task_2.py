def is_year_leap(age):
    if age % 4 == 0:
        return True
    else:
        return False

age = int(input("Введите год на проверку: "))
print("год:", age, is_year_leap(age) )