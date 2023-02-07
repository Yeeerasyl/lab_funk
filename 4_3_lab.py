students=[
    [
        "Yerasyl",
        [5,4,5,5,4,5]
    ],
    [
        "Alikhan",
        [3,3,4,3,4,5]
    ],
    [
        "Abylai",
        [3,4,5,3,3,3,3]
    ]
]

print(students)
def name_key(people):
    return(people[0])

students.sort(key=name_key)

print(students)