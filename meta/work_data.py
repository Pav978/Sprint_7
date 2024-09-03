import requests
from faker import Faker
from test_data import Handle_Scooter

# Данные для курьера с исользованием библиотеки Faker-
def create_random_data_courier():
    fake = Faker()
    login = fake.user_name()
    password = fake.password()
    first_name = fake.first_name()
    data = {
        "login": login,
        "firstname": first_name,
        "password": password
    }

    return data

# Создание курьера без ввод логина-
def create_courier_without_login():
    fake = Faker()
    password = fake.password()
    first_name = fake.first_name()
    data = {
        "login": "",
        "firstname": first_name,
        "password": password
    }

    return data

# Создание курьера без ввода пароля-
def create_courier_without_password():
    fake = Faker()
    login = fake.user_name()
    first_name = fake.first_name()
    data = {
        "login": login,
        "firstname": first_name,
        "password": ""
    }

    return data

# Создание курьера и сохранение данных о нем в случае удачной регистрации-
def create_new_courier_and_input_daet():
    login_pass = []
    data = create_random_data_courier()
    response = requests.post(Handle_Scooter.create_courier, data=data)
    if response.status_code == 201:
        login_pass.append(data.get("login"))
        login_pass.append(data.get("password"))
        login_pass.append(data.get("first_name"))
    return login_pass
