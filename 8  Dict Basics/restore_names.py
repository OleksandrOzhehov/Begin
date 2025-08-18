"""
У базі даних користувачів стався збій: у декого зникли значення з поля first_name. Добре що у user вже є поле full_name,
    з якого ми можемо взяти потрібні дані.
Реалізуй функцію restore_names, яка:
    Приймає список словників users.
    Відновлює first_name у тих, у кого воно відсутнє, спираючись на поле full_name.
    Нічого не повертає.
Наприклад:
    users = [
      {
        "last_name": "Holy",
        "full_name": "Jack Holy",
      },
      {
        "last_name": "Adams",
        "full_name": "Mike Adams",
      },
    ]

restore_names(users)

      users == [
        {
          "first_name": "Jack",
          "last_name": "Holy",
          "full_name": "Jack Holy",
        },
        {
          "first_name": "Mike",
          "last_name": "Adams",
          "full_name": "Mike Adams",
        },
      ]
    Підказка.     Використовуй not in для перевірки входження ключа.
"""

def restore_names(users: list) -> None:
    for i in range(len(users)):
        pos = users[i]["full_name"].index(" ")
        a = users[i]["full_name"][:pos]
        users[i]["first_name"] = a
    return None


def restore_names_from_mentor(users: list) -> None:
    for user in users:
        if "first_name" not in user:
            user["first_name"] = user["full_name"].split(" ")[0]


users = [
  {
    "last_name": "Holy",
    "full_name": "Jack Holy",
  },
  {
    "last_name": "Adams",
    "full_name": "Mike Adams",
  },
]

restore_names(users)
