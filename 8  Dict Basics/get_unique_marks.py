"""
У 4-А класі багато батьків почали жалітись, що в одного з викладачів «не існує» оцінок, крім 2 і 12. Він або ставить 12,
    або, якщо була допущена хоч найдрібніша помилка, 2.
Щоб з'ясувати, чи це дійсно так, ми вирішили дізнатися, які унікальні оцінки він виставив останнім часом.
Напиши функцію get_unique_marks(), яка:
    Приймає один параметр — шкільний журнал class_register.
    Повертає список унікальних оцінок.
    Журнал зберігається у вигляді словника, де ключі — це імена учнів, а значення — оцінки, які вони отримали.
Приклад журналу:
        class_register = {
          "Robb Stark": 2,
          "Sansa Stark": 12,
          "Arya Stark": 2,
          "Bran Stark": 2,
          "Jon Snow": 2,
        }
Для такого журналу, функція get_unique_marks() повинна повернути список [2, 12]
"""

def get_unique_marks(class_register: dict) -> list:
    out_list = []
    for key in class_register:
        if not class_register[key] in out_list:
            out_list.append(class_register[key])
    return out_list


def get_unique_marks_alternative(class_register: dict) -> list:
    return list(set(class_register.values()))


def get_unique_marks_from_mentor(class_register: dict) -> list:
    return list(set(class_register.values()))
