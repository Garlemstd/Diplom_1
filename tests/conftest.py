import pytest
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


@pytest.fixture
def database():
    return Database()


@pytest.fixture
def ingredients():
    return [
        Ingredient("Vegetable", "Lettuce", 0.5),
        Ingredient("Vegetable", "Tomato", 0.75),
        Ingredient("Meat", "Beef Patty", 3.0),
    ]


@pytest.fixture
def create_burger(create_bun, ingredients):
    _, _, created_bun = create_bun
    burger = Burger()
    burger.set_buns(created_bun)
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)
    return burger


@pytest.fixture
def main_ingridient():
    return "sauce", "Ketchup", 0.5