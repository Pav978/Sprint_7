import allure
import pytest
import requests
from test_data import *

#1-4
class TestCreateOrders:
    @allure.title("Формирование заказа с перебором раскраски самоката-")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["GREY", "BLACK"], []])
    def test_create_orders_color_scooter(self, color):
        data = UserData.test_user
        data["color"] = color
        response = requests.post(Handle_Scooter.create_orders, json=data)
        assert response.status_code == 201
        assert ResponseError.track_text in response.text
