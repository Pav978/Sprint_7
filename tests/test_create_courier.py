from test_data import *
import allure
from meta.work_data import *


class TestCreateCourier:
#1
    @allure.title("Создание курьера со всеми обязательными данными с получением положительного ответа сервера-")
    def test_create_courier_with_all_date(self):
        data = create_random_data_courier()
        response = requests.post(Handle_Scooter.create_courier, json=data)
        assert response.status_code == 201
        assert ResponseError.successful_text in response.text
#2
    @allure.title("Создание курьера без логина с получением сообщения об ошибке-")
    def test_create_courier_without_login_error(self):
        data = create_courier_without_login()
        response = requests.post(Handle_Scooter.create_courier, json=data)
        assert response.status_code == 400
        assert ResponseError.error_drawback_date_text in response.text
#3
    @allure.title("Создание курьера без пароля с получением сообщения об ошибке-")
    def test_create_courier_without_password_error(self):
        data = create_courier_without_password()
        response = requests.post(Handle_Scooter.create_courier, json=data)
        assert response.status_code == 400
        assert ResponseError.error_drawback_date_text in response.text
#4
    @allure.title("Создание курьера с уже существующим логином с возвращением ошибки-")
    def test_create_courier_with_duplicate_login_error(self):
        data = CourierData.courier_date
        response = requests.post(Handle_Scooter.create_courier, json=data)
        assert response.status_code == 409
        assert ResponseError.error_login_text in response.text
#5
    @allure.title("Создание курьера с пустыми данными с возвращением ошибки-")
    def test_create_courier_without_date_error(self):
        data = {"login": "", "firstname": "", "password": ""}
        response = requests.post(Handle_Scooter.create_courier, json=data)
        assert response.status_code == 400
        assert ResponseError.error_drawback_date_text in response.text
