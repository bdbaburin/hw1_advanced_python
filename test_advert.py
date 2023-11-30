import pytest
from issue_01 import Advert
import json


def test_iphone():
    data = {
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"],
        },
    }
    phone_adv = Advert(data=data)
    assert phone_adv.title == "iPhone X"
    assert phone_adv.price == 100
    assert phone_adv.location.address == "город Самара, улица Мориса Тореза, 50"


def test_corgi():
    data = {
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        },
    }
    corgi_adv = Advert(data)
    assert corgi_adv.class_ == "dogs"


def test_python():
    lesson_str = """{
                    "title": "python",
                    "price": 0,
                    "location": {
                    "address": "город Москва, Лесная, 7",
                    "metro_stations": ["Белорусская"]
                    }
                    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.location.address == "город Москва, Лесная, 7"


def test_price_negative():
    lesson_str = '{"title": "python", "price": -1}'
    lesson = json.loads(lesson_str)
    with pytest.raises(ValueError):
        Advert(lesson)


def test_price_negative2():
    lesson_str = '{"title": "python", "price": 1}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    with pytest.raises(ValueError):
        lesson_ad.price = -3


if __name__ == "__main__":
    pass
