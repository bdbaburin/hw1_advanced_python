from issue_01 import Advert as BaseAdvert
import json


class ColorizeMixin:
    '''
    Миксин для окрашивания вывода в консоль
    в определнный цвет
    '''
    def __repr__(self):
        # sub_str = '\033[1;{};40m'
        sub_str = "\033[{}m{} | {}\033[0m"
        # return sub_str.format(self.repr_color_code) + f'{self.title} | {self.price}\n'
        return sub_str.format(self.repr_color_code, self.title, self.price)


class Advert(ColorizeMixin, BaseAdvert):
    '''Класс объявления с возможностью цветного вывода в консоль
    Атрибуты:
    '''
    repr_color_code = 33

    def __init__(self, data):
        super().__init__(data=data)


if __name__ == "__main__":
    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    lesson_ad.repr_color_code = 35
    print(lesson_ad)
    df = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
        "address": "город Самара, улица Мориса Тореза, 50",
        "metro_stations": ["Спортивная", "Гагаринская"]
                    }
            }"""
    df = json.loads(df)
    example = Advert(data=df)
    print(example)
