"""
Уяви, що ти організовуєш велику виставку техніки та моди, і маєш окремі списки відвідувачів для кожного відділу. Твоє
    завдання — використати методи множин для аналізу цієї інформації:
        union() для отримання списку всіх унікальних відвідувачів виставки;
        intersection() для визначення відвідувачів, які зацікавлені і в техніці, і в моді;
        difference() для знаходження відвідувачів, які зацікавлені лише в техніці, але не в моді.
        Напиши функцію event_planning() повинна повернути кортеж з двох множин: тих хто віддає перевагу обом напрямкам,
            та тих хто віддає перевагу тільки одному напрямку.
Наприклад:
    electronics_attendees == {"Alex", "Maria", "John"}
    clothing_attendees == {"John", "Sophia", "Maria", "Mike"}
    event_planning(electronics_attendees, clothing_attendees) == ({"John", "Maria"}, {"Alex", "Sophia", "Mike"})
"""

def event_planning(electronics_attendees: set, clothing_attendees: set) -> tuple[set, set]:
    return (electronics_attendees & clothing_attendees, electronics_attendees ^ clothing_attendees)

def event_planning_from_mentor(electronics_attendees: set, clothing_attendees: set) -> tuple[set, set]:
    both_interested = electronics_attendees.intersection(clothing_attendees)
    only_tech = electronics_attendees.difference(clothing_attendees)
    only_fashion = clothing_attendees.difference(electronics_attendees)
    only_one_area = only_tech.union(only_fashion)
    return both_interested, only_one_area
