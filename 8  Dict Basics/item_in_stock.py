"""
Уяви, що ти власник (власниця) магазину. У тебе є інвентарний список товарів у формі словника, де ключі — це назви
    товарів, а значення — це кількість товарів на складі. Ти хочеш швидко перевірити наявність певного товару та його
    кількість, не викликаючи помилку, якщо товару немає в наявності.
Для цього напиши функцію check_item_stock(), яка:
    Приймає inventory (інвентарний список) та item_name (назву товару, який потрібно перевірити). Використай метод get()
        для отримання кількості товару на складі.
    Якщо товар є у списку поверни True, інакше — False.
Наприклад:
    inventory = {"apples": 30, "bananas": 45}
    item_name = "oranges"
    check_item_stock(inventory, item_name) # False
"""


def check_item_stock(inventory: dict, item_name: str) -> bool:
    return (inventory.get(item_name,0) > 0)


inventory = {"apples": 30, "bananas": 45}
item_name = "oranges"
item_name2 = "apples"
print(check_item_stock(inventory, item_name)) # False
print(check_item_stock(inventory, item_name2)) # False
