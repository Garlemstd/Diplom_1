import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDB:
    def test_database_initialization(self, database):

        assert len(database.buns) == 3  # База создает 3 булки при инициализации
        assert len(database.ingredients) == 6  # База создает 6 ингредиентов при инициализации

    @pytest.mark.parametrize("index, expected_name, expected_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300),
    ])
    def test_available_buns(self, database, index, expected_name, expected_price):
        bun = database.available_buns()[index]
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price

    @pytest.mark.parametrize("index, expected_type, expected_name, expected_price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_available_ingredients(self, database, index, expected_type, expected_name, expected_price):
        ingredient = database.available_ingredients()[index]
        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price

