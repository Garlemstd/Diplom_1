

class TestIngridients:

    def test_ingredient_initialization(self, ingredients):
        ing_type, name, price = ingredients[0].type, ingredients[0].name, ingredients[0].price,
        assert ingredients[0].type == ing_type
        assert ingredients[0].name == name
        assert ingredients[0].price == price

    def test_get_price(self, ingredients):
        price = ingredients[0].price
        assert ingredients[0].get_price() == price

    def test_get_name(self, ingredients):
        name = ingredients[0].name
        assert ingredients[0].get_name() == name

    def test_get_type(self, ingredients):
        ing_type = ingredients[0].type
        assert ingredients[0].get_type() == ing_type

    def test_ingredient_price_type(self, ingredients):
        assert isinstance(ingredients[0].get_price(), float)

    def test_ingredient_name_type(self, ingredients):
        assert isinstance(ingredients[0].get_name(), str)

    def test_ingredient_type_type(self, ingredients):
        assert isinstance(ingredients[0].get_type(), str)
