from locators import *


class ApiClass:

    def get_second_page_user_list_with_check_page_number(self):
        result_list_users = requests.get(base_url + users_resource + "?page=2")
        if result_list_users.status_code == 200:
            print("Успешно. Статус код 200.", end=" ")
            if result_list_users.json().get("page") == 2:
                print("Получена страница №2: " + result_list_users.text)
            else:
                print(f"Ошибка. Получена некорректная страница. Номер полученной страницы: {str(result_list_users.json().get('page'))}")
        else:
            print(f"Ошибка. Список пользователей не получен. Статус код: {str(result_list_users.status_code)}")

    def get_user_info(self):
        result_single_user = requests.get(base_url + users_resource_for_id + str(random_real_id))
        assert result_single_user.status_code == 200, f"Ошибка. Данные о пользователе не получены. Статус-код запроса: {str(result_single_user.status_code)}"
        print("Успешно. Статус-код 200. Данные о пользователе получены: " + result_single_user.text)

    def get_unreal_user_info(self):
        result_single_user = requests.get(base_url + users_resource_for_id + str(random_unreal_id))
        assert result_single_user.status_code == 404, f"Ошибка. Данные о пользователе получены. Статус-код запроса: {str(result_single_user.status_code)}"
        print(f"Успешно. Статус-код запроса - 404. Пользователя с id {str(random_unreal_id)} не существует")

    def get_color_list(self):
        result_list_colors = requests.get(base_url + list_colors_resource)
        if result_list_colors.status_code == 200:
            print("Успешно. Статус-код 200. Список цветов получен.", end=" ")
            if result_list_colors.json().get("per_page") == 6:
                print("В полученном списке 6 цветов:", end=' ')
                names = []
                for data in result_list_colors.json()['data']:
                    name = data['name']
                    names.append(name)
                for name in names:
                    print(name, end='; ')
                print(" ")
            else:
                print("Ошибка. В полученном списке не 6 цветов, а " + str(result_list_colors.json().get("per_page")))
        else:
            print(f"Ошибка. Статус-код {str(result_list_colors.status_code)}. Список цветов не получен")

    def get_color_info(self):
        result_single_color = requests.get(base_url + list_colors_resource + str(random_real_id))
        assert result_single_color.status_code == 200, f"Ошибка. Данные о цвете не получены. Статус-код запроса: {str(result_single_color.status_code)}"
        print("Успешно. Статус-код 200. Данные о цвете получены: " + result_single_color.text)

    def get_unreal_color_info(self):
        result_single_color = requests.get(base_url + list_colors_resource + str(random_unreal_id))
        assert result_single_color.status_code == 404, f"Ошибка. Данные о цвете получены. Статус-код запроса: {str(result_single_color.status_code)}"
        print(f"Успешно. Статус-код запроса - 404. Цвета с id {str(random_unreal_id)} не существует")

    def post_new_user(self):
        body_for_create_user = {"name": random.choice(names_matrix), "job": random.choice(job_matrix)}
        result_create_user = requests.post(base_url + users_resource, json=body_for_create_user)
        if result_create_user.status_code == 201:
            print("Успешно. Статус-код запроса 201. Пользователь успешно создан: ", result_create_user.text)
            return result_create_user.json().get('id')
        else:
            print("Ошибка. Пользователь не создан. Статус-код запроса " + str(result_create_user.status_code))

    def put_full_update_user_info(self, new_user_id):
        bode_for_update_user_info = {"name": random.choice(simple_names), "job": random.choice(simple_job)}
        result_update_user_info = requests.put(base_url + users_resource_for_id + str(new_user_id), json=bode_for_update_user_info)
        if result_update_user_info.status_code == 200:
            print("Успешно. Статус-код запроса 200. Информация о пользователе успешно обновлена: ",
                  result_update_user_info.text)
        else:
            print("Ошибка. Информация о пользователе не обновлена. Статус-код запроса " + str(result_update_user_info.status_code))

    def put_half_update_user_info(self, new_user_id):
        bode_for_update_user_info = {"name": random.choice(simple_names)}
        result_update_user_info = requests.put(base_url + users_resource_for_id + str(new_user_id), json=bode_for_update_user_info)
        new_job = result_update_user_info.json().get("job")
        if result_update_user_info.status_code == 200:
            if new_job is None:
                print("Успешно. Статус-код запроса 200. Информация о пользователе успешно перезаписана. Имя изменено, данные о работе удалены: " + result_update_user_info.text)
            else:
                print(
                    "Ошибка. Статус-код запроса 200, но информация о работе не удалена: " + result_update_user_info.text)
        else:
            print("Ошибка. Информация о пользователе не обновлена. Статус-код запроса " + str(result_update_user_info.status_code))
            
    def patch_full_update_user_info(self, new_user_id):
        bode_for_update_user_info = {"name": random.choice(simple_names), "job": random.choice(simple_job)}
        result_update_user_info = requests.patch(base_url + users_resource_for_id + str(new_user_id), json=bode_for_update_user_info)
        if result_update_user_info.status_code == 200:
            print(
                f"Успешно. Статус-код запроса 200. Информация о пользователе c id={str(new_user_id)} успешно обновлена: ",
                result_update_user_info.text)
        else:
            print("Ошибка. Информация о пользователе не обновлена. Статус-код запроса " + str(
                result_update_user_info.status_code))

    def delete_user(self, new_user_id):
        result_delete_user = requests.delete(base_url + users_resource_for_id + str(new_user_id))
        if result_delete_user.status_code == 204:
            print("Успешно. Пользователь успешно удален")
        else:
            print("Ошибка. Пользователь не удален. Статус-код запроса " + str(result_delete_user.status_code))
            
    def post_user_registration(self):
        body_for_registration = {"email": email_for_reg, "password": password}
        result_registration = requests.post(base_url + registration_resource, json=body_for_registration)
        if result_registration.status_code == 200:
            print(
                f"Успешно. Пользователь зарегистрирован. Ему присвоен id={result_registration.json().get('id')} и token={result_registration.json().get('token')}")
        else:
            print("Ошибка. Пользователь не зарегистрирован. Статус-код запроса " + str(
                result_registration.status_code) + ": " + result_registration.text)
            
    def post_reg_without_password(self):
        body_for_registration = {"email": mail_for_negative_reg}
        result_registration = requests.post(base_url + registration_resource, json=body_for_registration)
        if result_registration.status_code == 400:
            print("Успешно. Пользователь не зарегистрирован. Статус-код запроса 404. Сообщение: " + str(result_registration.json().get('error')))
        else:
            print(
                f"Ошибка. Пользователь успешно зарегистрирован. Ему присвоен id={result_registration.json().get('id')} и token={result_registration.json().get('token')}")
            
    def post_reg_with_incorrect_email(self):
        body_for_registration = {"email": mail_for_negative_reg, "password": password}
        result_registration = requests.post(base_url + registration_resource, json=body_for_registration)
        if result_registration.status_code == 400:
            print('Успешно. Пользователь не зарегистрирован. Статус-код запроса 404. Сообщение: "' + str(
                result_registration.json().get('error')) + '"')
        else:
            print(
                f"Ошибка. Пользователь зарегистрирован. Ему присвоен id={result_registration.json().get('id')} и token={result_registration.json().get('token')}")

    def post_authorization(self):
        body_for_auth = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        result_auth = requests.post(base_url + auth_resource, json=body_for_auth)
        if result_auth.status_code == 200:
            print(
                f'Успешно. Пользователь авторизован. Статус-код запроса 200. Ему присвоен token={result_auth.json().get("token")}')
        else:
            print(f"Ошибка. Пользователь не авторизован. Сообщение: " + result_auth.text)

    def post_auth_without_password(self):
        body_for_auth = {"email": "eve.holt@reqres.in"}
        result_auth = requests.post(base_url + auth_resource, json=body_for_auth)
        error_msg = result_auth.json().get('error')
        if result_auth.status_code == 400 and error_msg == "Missing password":
            print(f'Успешно. Пользователь не авторизован. Статус-код запроса 400. Сообщение: "Missing password"')
        else:
            print(f"Ошибка. Пользователь авторизован. Сообщение: " + result_auth.text)

    def get_list_user_with_delay(self):
        result_delay_list_users = requests.get(base_url + users_resource + '?delay=' + str(delay))
        if result_delay_list_users.status_code == 200:
            print(
                f"Успешно. Список пользователей получен с задержкой {str(delay)} секунд: " + result_delay_list_users.text)
        else:
            print("Ошибка. Список пользователей не был получен. Статус-код " + str(result_delay_list_users.status_code))
    
