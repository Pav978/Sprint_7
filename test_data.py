class Url:
    url = 'https://qa-scooter.praktikum-services.ru'

#Ручки приложения
class Handle_Scooter:
    create_courier = f'{Url.url}/api/v1/courier'
    courier_login = f'{Url.url}/api/v1/courier/login'
    create_orders = f'{Url.url}/api/v1/orders'
    get_orders_list = f'{Url.url}/api/v1/orders'


class UserData:
    test_user = {
        'firstname': 'Кот',
        'lastname': 'Саймон',
        'address': 'Воронеж, Лизюково',
        'metroStation': 11,
        'phone': '+77777777777',
        'rentTime': 5,
        'deliveryDate': '2024-08-08',
        'comment': 'Привет...',
        'color': []

    }
class CourierData:
    courier_date = {
        "login": "Kot",
        "password": "1234",
        "firstName": "Simon"
    }

class ResponseError:
    successful_text = '{"ok":true}'
    error_drawback_date_text = "Недостаточно данных для создания учетной записи"
    error_login_text = "Этот логин уже используется"
    track_text = "track"
    get_orders_list_text = "orders"
    id_text = "id"
    error_date_enter_text = "Недостаточно данных для входа"
    error_without_account_text = "Учетная запись не найдена"

