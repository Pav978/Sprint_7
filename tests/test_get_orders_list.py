import allure
import requests
from test_data import Handle_Scooter
from test_data import ResponseError


class TestOrdersList:
    @allure.title("Формирование списка заказов для курьера-")
    def test_order_list(self):
        response = requests.get(Handle_Scooter.get_orders_list)
        assert response.status_code == 200
        assert ResponseError.get_orders_list_text in response.text
