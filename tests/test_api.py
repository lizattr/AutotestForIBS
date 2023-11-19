from base.api_class import ApiClass
from locators import *


class TestApi:

    @pytest.mark.user
    @pytest.mark.get_request
    # Получение второй страницы списка пользователей с проверкой номера страницы
    def test_get_second_page_user_list_with_check_page_number(self):
        test = ApiClass()
        test.get_second_page_user_list_with_check_page_number()

    @pytest.mark.user
    @pytest.mark.get_request
    # Получение данных о существующем пользователе
    def test_get_user_info(self):
        test = ApiClass()
        test.get_user_info()

    @pytest.mark.user
    @pytest.mark.get_request
    # Запрос данных о несуществующем пользователе. Негативный сценарий
    def test_get_unreal_user_info(self):
        test = ApiClass()
        test.get_unreal_user_info()

    @pytest.mark.get_request
    # Запрос списка цветов c проверкой количества цветов на странице и выводом списка цветов
    def test_get_color_list(self):
        test = ApiClass()
        test.get_color_list()

    @pytest.mark.get_request
    # Получение данных об известном цвете
    def get_color_info(self):
        test = ApiClass()
        test.get_color_info()

    @pytest.mark.get_request
    # Запрос данных о неизвестном цвете
    def test_get_unreal_color_info(self):
        test = ApiClass()
        test.get_unreal_color_info()

    @pytest.mark.user
    @pytest.mark.post_request
    # Создание пользователя
    def test_post_new_user(self):
        test = ApiClass()
        test.post_new_user()

    @pytest.mark.user
    @pytest.mark.put_request
    # Полное обновление информации о пользователе методом PUT
    def test_put_full_update_user_info(self):
        test = ApiClass()
        new_user_id = test.post_new_user()
        test.put_full_update_user_info(new_user_id)

    @pytest.mark.user
    @pytest.mark.put_request
    # Частичное обновление информации о пользователе методом PUT
    def test_put_half_update_user_info(self):
        test = ApiClass()
        new_user_id = test.post_new_user()
        test.put_half_update_user_info(new_user_id)

    @pytest.mark.patch_request
    # Полное обновление информации о пользователе методом PATCH
    def test_patch_full_update_user_info(self):
        test = ApiClass()
        new_user_id = test.post_new_user()
        test.patch_full_update_user_info(new_user_id)

    @pytest.mark.user
    @pytest.mark.delete_request
    # Удаление пользователя
    def test_delete_user(self):
        test = ApiClass()
        new_user_id = test.post_new_user()
        test.delete_user(new_user_id)

    @pytest.mark.user
    @pytest.mark.post_request
    # Регистрация нового пользователя
    def test_post_user_registration(self):
        test = ApiClass()
        test.post_user_registration()

    @pytest.mark.user
    @pytest.mark.post_request
    # Регистрация нового пользователя без пароля. Негативный сценарий
    def test_post_reg_without_password(self):
        test = ApiClass()
        test.post_reg_without_password()

    @pytest.mark.user
    @pytest.mark.post_request
    # Регистрация нового с некорректным емейлом. Негативный сценарий
    def test_post_reg_with_incorrect_email(self):
        test = ApiClass()
        test.post_reg_with_incorrect_email()

    @pytest.mark.user
    @pytest.mark.post_request
    # Авторизация пользователя
    def test_post_authorization(self):
        test = ApiClass()
        test.post_authorization()

    @pytest.mark.user
    @pytest.mark.post_request
    # Авторизация пользователя без введения пароля. Негативный сценарий
    def test_post_auth_without_password(self):
        test = ApiClass()
        test.post_auth_without_password()

    @pytest.mark.user
    @pytest.mark.get_request
    # Получение списка пользователей с задержкой от 1 до 5 секунд
    def test_get_list_user_with_delay(self):
        test = ApiClass()
        test.get_list_user_with_delay()
