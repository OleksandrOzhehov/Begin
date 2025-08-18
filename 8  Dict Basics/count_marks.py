"""
У 5-А класі багато батьків почали жалітись, що навіть вони не можуть впоратися із завданням на диференційне числення,
    яке дали дітям на контрольній роботі. Потрібно перевірити, чи справді завдання занадто складне для п'ятикласників.
Для цього потрібно зібрати статистику учнів, які отримали кожну з можливих оцінок (від 1 до 12). Ми дуже розраховуємо
    на твою допомогу у цьому завданні.
Напиши функцію count_marks(), яка:
    Приймає один параметр — шкільний журнал class_register.
    Повертає бажану статистику.
    Журнал зберігається у вигляді словника, де ключі — це імена учнів, а значення — оцінки, які вони отримали за
        контрольну роботу.
Приклад журналу:
        class_register = {
          "Robb Stark": 10,
          "Sansa Stark": 12,
          "Arya Stark": 6,
          "Bran Stark": 8,
          "Jon Snow": 8,
        }
Функція також має повертати словник. У ньому ключі — це оцінки, а значення — це кількість учнів, які отримали цю
    оцінку. Наприклад, для наведеного вище журналу статистика має бути наступною:
        count_marks(class_register) == {
          6: 1,
          8: 2,
          10: 1,
          12: 1,
        }
"""

def count_marks(class_register: dict) -> dict:
    out_dict = dict()
    for key in class_register:
        if class_register[key] in out_dict:
            out_dict[class_register[key]] += 1
        else:
            out_dict[class_register[key]] = 1
    return out_dict

def count_marks_alternative(class_register: dict) -> dict:
    output_dict ={}
    list_of_marks = list(class_register.values())
    for iter in range(1,13):
        if iter in list_of_marks:
            output_dict.update({iter : list_of_marks.count(iter)})
    return output_dict

from collections import defaultdict
def count_marks_alternative_2(class_register: dict) -> dict:
    output_dict = defaultdict(int)
    list_of_marks = list(class_register.values())
    for mark in list_of_marks:
        output_dict[mark] += 1
    return dict(output_dict)


def count_marks_from_mentor(class_register: dict) -> dict:
    marks_count = {}
    for mark in class_register.values():
        if mark not in marks_count:
            marks_count[mark] = 1
        else:
            marks_count[mark] += 1
    return marks_count
