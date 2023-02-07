name=str(input("введите ваше имя: "))
last_name=str(input("введите вашу фамилию: "))

print("длина имени: ",len(name))
if (name.isalpha())==True:
    print("Это имя состоит только из букв")
else:
    print("В этом имени есть цифры")
print("Первая буква имение заглавная: ",name.istitle())
print(last_name+" "+name)
print(name*3)
print(name[0:3])
print(name.upper())
print(name.lower())
print(" буква",name[0] ," в ASCII коде: ",ord(name[0]))
print(name.capitalize())