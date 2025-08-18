"""
Уявімо, що ти організовуєш масштабний захід і маєш список гостей, де ім'я гостя є ключем, а статус підтвердження участі
    є значенням. Ти отримав(-ла) нову інформацію від декількох гостей і хочеш оновити свій список.
Напиши функцію update_guest_list(), яка:
Приймає guest_list та оновлення new_guests.
Оновлює список гостей новою інформацією за допомогою update().
Приклад:
    guest_list = {"Alice": True, "Bob": False, "Charlie": True}
    new_guests = {"Bob": True, "Dave": False}
update_guest_list(guest_list, new_guests) == {'Alice': True, 'Bob': True, 'Charlie': True, 'Dave': False}
"""

def update_guest_list(guest_list: dict, new_guests: dict) -> dict:
    guest_list.update(new_guests)

def update_guest_list_of_mentor(guest_list: dict, new_guests: dict) -> dict:
    guest_list.update(new_guests)
    return guest_list


guest_list = {"Alice": True, "Bob": False, "Charlie": True}
new_guests = {"Bob": True, "Dave": False}
print(guest_list)
update_guest_list(guest_list, new_guests)
print(guest_list)
