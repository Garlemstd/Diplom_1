from data.test_data import BurgerData
from praktikum.bun import Bun


class TestBun:
    def test_create_bun(self):
        create_bun = Bun(BurgerData.BUN_NAME, BurgerData.BUN_PRICE)
        assert create_bun.get_price() == BurgerData().BUN_PRICE
        assert create_bun.get_name() == BurgerData().BUN_NAME

    def test_bun_name_type(self,):
        create_bun = Bun(BurgerData.BUN_NAME, BurgerData.BUN_PRICE)
        assert isinstance(create_bun.get_name(), str)

    def test_bun_price_type(self):
        create_bun = Bun(BurgerData.BUN_NAME, BurgerData.BUN_PRICE)
        assert isinstance(create_bun.get_price(), str)
