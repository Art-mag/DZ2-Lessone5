class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"{item_name} not found in {self.name}")


# Создание объектов класса Store
store1 = Store("Магазин продуктов 'Пятерочка'", "ул. Пушкина, 10")
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
store1.add_item("молоко", 1.2)

store2 = Store("Магазин 'ВкусВилл'", "пр. Ленина, 15")
store2.add_item("орехи", 2.0)
store2.add_item("мед", 3.5)
store2.add_item("овсянка", 1.0)

store3 = Store("Магазин бытовой техники 'М.Видео'", "ул. Советская, 5")
store3.add_item("холодильник", 500)
store3.add_item("телевизор", 700)
store3.add_item("стиральная машина", 400)


# Тестирование методов выбранного магазина
print("Выбранный магазин для тестирования:", store1.name)
print("Адрес магазина:", store1.address)
print("Ассортимент товаров:", store1.items)

store1.add_item("груши", 0.8)
print("Ассортимент после добавления нового товара:", store1.items)

store1.update_price("яблоки", 0.6)
print("Цена яблок после обновления:", store1.get_price("яблоки"))

store1.remove_item("молоко")
print("Ассортимент после удаления товара 'молоко':", store1.items)

print("Цена бананов:", store1.get_price("бананы"))
print("Цена молока:", store1.get_price("молоко"))  # Этого товара уже нет, вернется None
