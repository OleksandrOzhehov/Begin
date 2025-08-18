"""
Час оновлювати програмне забезпечення! Інженери випустили оновлення для застарілих версій роботів. Потрібно вишикувати
    всіх роботів та перевірити у кого з них застаріле ПЗ.
Напиши функцію get_outdated(), яка:
Приймає список роботів robots та ціле число new_version.
Повертає список індексів тих роботів, у яких core_version менший за new_version.
Наприклад:

robots = [
  { "core_version": 9 },
  { "core_version": 13 },
  { "core_version": 16 },
  { "core_version": 9 },
  { "core_version": 14 },
]

get_outdated(robots, 10) # [0, 3]
get_outdated(robots, 14) # [0, 1, 3]
get_outdated(robots, 8) # []
get_outdated(robots, 18) # [0, 1, 2, 3, 4]

💡 Тобі потрібно використати вбудовану функцію enumerate(). Спробуй загуглити її, використавши пошук по «python
    mastering enumerate function», щоб побачити як саме її використовують. Ось приклад якісного ресурсу з описом:
    geeksforgeeks (https://www.geeksforgeeks.org/what-does-the-enumerate-function-in-python-do/.
"""

def get_outdated(robots: list, new_version: int) -> list:
    # write your code here
    outlist = []
    for i in range(len(robots)):
        if robots[i]["core_version"] < new_version:
            outlist.append(i)
    return outlist

def get_outdated_from_mentor(robots: list, new_version: int) -> list:
    outdated_robots = []
    for i, robot in enumerate(robots):
        if robot["core_version"] < new_version:
            outdated_robots.append(i)
    return outdated_robots



robots = [
  { "core_version": 9 },
  { "core_version": 13 },
  { "core_version": 16 },
  { "core_version": 9 },
  { "core_version": 14 },
]

print(get_outdated(robots, 10)) # [0, 3]
print(get_outdated(robots, 14)) # [0, 1, 3]
print(get_outdated(robots, 8)) # []
print(get_outdated(robots, 18)) # [0, 1, 2, 3, 4]
