"""
У нас більше немає потреби зберігати дані про країну наших користувачів, тому ми вирішили видалити це поле з бази у два
етапи.
Напиши функцію remove_country(), яка:
    Видаляє поле country з бази даних users в усіх, у кого status дорівнює active.
    Нічого не повертає.
Наприклад:
        users = [
          { "name": "Emma", "status": "active", "country": "Ukraine" },
          { "name": "Avram", "status": "disabled", "country": "Poland" },
        ]
    # Видаляємо інформацію про країну у тих користувачів, у кого поле "status"
    # має значення "active" та отримуємо:
        users == [
          { "name": "Emma", "status": "active"},
          { "name": "Avram", "status": "disabled", "country": "Poland" },
        ]
"""


def remove_country(users: list) -> None:
    # write your code here
    for s in range(len(users)):
        if users[s]["status"] == "active":
            users[s].pop("country")
    return None


def remove_country_from_mentor(users: list) -> None:
    for user in users:
        if user["status"] == "active":
            del user["country"]
