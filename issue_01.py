from keyword import iskeyword


class LowerDecoder:
    """
    Класс, используемый для реализации вложенности атрибутов
    класса JsonDecoder
    """

    def __init__(self):
        pass

    def __repr__(self):
        return f'Available attributes: {", ".join(list(self.__dict__.keys()))}'


class JsonDecoder(LowerDecoder):
    """
    Класс, создающий из json объекта python
    объекты с доступом к атрибутам через точку
    Атрибуты:
        data (dict):
            данные для представления в виде python объекта

    Raises:
        ValueError - возникает в случае неправильного формата данных,
        пустоты данных,
        или отсутствия поля title в данных
    """

    def __init__(self, data: dict):
        self.data = data
        self.attributes_from_json(data=self.data)

    def attributes_from_json(self, data: dict, special_obj: LowerDecoder = None):
        """
        Метод, превращающий json объект в атрибуты текущего объекта

        Параметры:
            data (dict):
                данные для представления в виде полей python объекта
            special_obj (LowerDecoder):
                объект, атрибуты которого создаются (используются
                для вложенности)
        """
        if not data:
            raise ValueError("В инстанс класса не были переданы данные!")
        if not isinstance(data, dict):
            raise ValueError("Данные не находятся в формате JSON")
        if not (special_obj) and "title" not in set(data.keys()):
            raise ValueError("Title is not defined")
        if special_obj:
            obj = special_obj
        else:
            obj = self
        for name, value in data.items():
            if iskeyword(name):
                name = name + "_"
            if name == "price":
                name = "_" + "price"
            if isinstance(value, dict):
                setattr(obj, name, LowerDecoder())
                special_obj = getattr(obj, name)
                self.attributes_from_json(data=value, special_obj=special_obj)
            else:
                setattr(obj, name, value)


class Advert(JsonDecoder):
    """
    Класс объявления

    Атрибуты:
        data (dict):
            данные для представления в виде полей python объекта

    Raises:
        ValueError - возникает в случае
        отрицательного значения для поля price

    """

    def __init__(self, data):
        super().__init__(data=data)
        self.price

    @property
    def price(self):
        current_price = getattr(self, "_price", 0)
        if not isinstance(current_price, (float, int)):
            raise ValueError("Price must be numeric")
        if current_price < 0:
            raise ValueError("Price must be >= 0")
        return current_price

    @price.setter
    def price(self, x):
        if x < 0:
            raise ValueError("Price must be >= 0")
        self._price = x

    def __repr__(self):
        return f"{self.title} | {self.price}"


if __name__ == "__main__":
    df = {
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"],
        },
    }

    example = Advert(data=df)
    print(example)
    print(example.title)
    print(example.price)
    print(example.location.address)
    print(*example.location.metro_stations)
