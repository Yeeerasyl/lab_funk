students = input("Введите имена студентов через пробел: ")
names = students.split()

va_names = ()

for name in names:
    if "ва" in name:
        va_names += (name,)
    elif "Ва" in name:
        va_names += (name,)

# Выводим имена, содержащие "ва"
print("Имена, содержащие 'ва':")
print(" ".join(va_names))
