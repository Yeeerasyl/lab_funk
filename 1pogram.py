resume = {
    "Имя": "Ерасыл",
    "Фамилия": "Уалихан",
    "Возраст": 19,
    "Номер":"87475565678",
    "Знание языков":"Python, C++"
}
resume2={
    "Почта":"yeeerrraaasyl@icloud.com"
}

Yerasyl_resume=dict.copy(resume)
print(Yerasyl_resume)
print()

print(resume.keys())
print()

print(resume.values())
print()

resume.update(resume2)
print(resume)
print()

resume.clear()
print(resume)

