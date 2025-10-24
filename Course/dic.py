# students={
#     "umair":"cs student",
#     "nasir":"se student",
#     "Aon":"cs student"
# }

# for s in students:
#     print(s,students[s])

students=[
    {"name":"ali","grade":"a"},
    {"name":"Aon","grade":"a+"},
    {"name":"Ahmed","grade":"a"},
]

for student in students:
    print(student["name"],student["grade"])