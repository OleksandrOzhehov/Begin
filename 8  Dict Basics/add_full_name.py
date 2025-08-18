"""
База даних зберігає користувачів у такому форматі:
    {
      "first_name": "Ivan",
      "last_name": "Vasylchenko",
    }
Було б зручно додати поле full_name в кожен словник.
Створи функцію add_full_name(), яка:
    Приймає словник user.
    Додає до нього поле full_name з ім'ям та прізвищем поєднаними одним пробілом.
    Нічого не повертає.
Наприклад:
    user = {
      "first_name": "Ivan",
      "last_name": "Vasylchenko",
    }

    add_full_name(user)

    # user == {
    #   "first_name": "Ivan",
    #   "last_name": "Vasylchenko",
    #   "full_name": "Ivan Vasylchenko",
    # }
"""

def add_full_name(user: dict) -> None:
    # write your code here
    user["full_name"] = user["first_name"] + " " + user["last_name"]
    return None
