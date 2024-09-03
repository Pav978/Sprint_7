import allure
from meta.work_data import *
from test_data import ResponseError
from test_data import Handle_Scooter


class TestLoginCourier:
#1
    @allure.title("Вход курьера с правильно введенными данными-")
    def test_login_courier_with_correct_data(self):
        data = create_new_courier_and_input_daet()
        response = requests.post(Handle_Scooter.courier_login, json={"login": data[0], "password": data[1]})
        assert response.status_code == 200
        assert ResponseError.id_text in response.text
#2
    @allure.title("Вход курьера в прилоежине без логина с возваращением ошибки-")
    def test_login_courier_without_login(self):
        data = create_new_courier_and_input_daet()
        response = requests.post(Handle_Scooter.courier_login, json={"login": "", "password": data[1]})
        assert response.status_code == 400
        assert ResponseError.error_date_enter_text in response.text
#3
    @allure.title("Вход курьера без пароля с возвращением ошибки-")
    def test_login_courier_without_password(self):
        data = create_new_courier_and_input_daet()
        response = requests.post(Handle_Scooter.courier_login, json={"login": data[0], "password": ""})
        assert response.status_code == 400
        assert ResponseError.error_date_enter_text in response.text
#4
    @allure.title("Вход курьера с правильным логином, но не правильным паролем с возвращением ошибки-")
    def test_correct_login_with_incorrect_password(self):
        data = create_new_courier_and_input_daet()
        response = requests.post(Handle_Scooter.courier_login, json={"login": data[0], "password": "kurwa"})
        assert response.status_code == 404
        assert ResponseError.error_without_account_text in response.text
#5
    @allure.title("Вход курьера с не правильным логином и правильным паролем-")
    def test_login_incorreсt_with_correct_password(self):
        data = create_new_courier_and_input_daet()
        response = requests.post(Handle_Scooter.courier_login, json={"login": "bobr", "password": data[1]})
        assert response.status_code == 404
        assert ResponseError.error_without_account_text in response.text
#6
    @allure.title("Вход курьера с несуществующими данными и возвращением ошибки-")
    def test_login_without_data(self):
        data = create_random_data_courier()
        response = requests.post(Handle_Scooter.courier_login, json=data)
        assert response.status_code == 404
        assert ResponseError.error_without_account_text in response.text
