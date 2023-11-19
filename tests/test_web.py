from locators import *
from base.web_class import WebClass


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestWeb:

    @pytest.fixture(scope="function")
    def setup_function(self, driver):
        driver.get(base_url)

    @pytest.mark.user
    @pytest.mark.get_request
    def test_list_user(self, driver, setup_function):  # Клик по запросу LIST USERS на главной странице с проверкой ответа и статус-кода
        main = WebClass(driver)
        body = '{"page":2,"per_page":6,"total":12,"total_pages":2,"data":[{"id":7,"email":"michael.lawson@reqres.in","first_name":"Michael","last_name":"Lawson","avatar":"https://reqres.in/img/faces/7-image.jpg"},{"id":8,"email":"lindsay.ferguson@reqres.in","first_name":"Lindsay","last_name":"Ferguson","avatar":"https://reqres.in/img/faces/8-image.jpg"},{"id":9,"email":"tobias.funke@reqres.in","first_name":"Tobias","last_name":"Funke","avatar":"https://reqres.in/img/faces/9-image.jpg"},{"id":10,"email":"byron.fields@reqres.in","first_name":"Byron","last_name":"Fields","avatar":"https://reqres.in/img/faces/10-image.jpg"},{"id":11,"email":"george.edwards@reqres.in","first_name":"George","last_name":"Edwards","avatar":"https://reqres.in/img/faces/11-image.jpg"},{"id":12,"email":"rachel.howell@reqres.in","first_name":"Rachel","last_name":"Howell","avatar":"https://reqres.in/img/faces/12-image.jpg"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}'
        resource = '/api/users?page=2'
        main.send_get_request(body, resource, 200)

    @pytest.mark.user
    @pytest.mark.get_request
    def test_single_user(self, driver, setup_function):  # Клик по запросу SINGLE USER на главной странице с проверкой ответа и статус-кода
        main = WebClass(driver)
        main.click_button_single_user(button_single_user)
        body = '{"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}'
        resource = "/api/users/2"
        main.send_get_request(body, resource, 200)

    @pytest.mark.user
    @pytest.mark.get_request
    def test_single_user_not_found(self, driver, setup_function):  # Клик по запросу SINGLE USER NOT FOUND на главной странице с проверкой ответа и статус-кода
        body = '{}'
        resource = '/api/users/23'
        main = WebClass(driver)
        main.click_button_single_user(button_single_user_not_found)
        main.send_get_request(body, resource, 404)

    @pytest.mark.get_request
    def test_list_colors(self, driver, setup_function):  # Клик по запросу LIST <RESOURCE> на главной странице с проверкой ответа и статус-кода
        body = '{"page":1,"per_page":6,"total":12,"total_pages":2,"data":[{"id":1,"name":"cerulean","year":2000,"color":"#98B2D1","pantone_value":"15-4020"},{"id":2,"name":"fuchsia rose","year":2001,"color":"#C74375","pantone_value":"17-2031"},{"id":3,"name":"true red","year":2002,"color":"#BF1932","pantone_value":"19-1664"},{"id":4,"name":"aqua sky","year":2003,"color":"#7BC4C4","pantone_value":"14-4811"},{"id":5,"name":"tigerlily","year":2004,"color":"#E2583E","pantone_value":"17-1456"},{"id":6,"name":"blue turquoise","year":2005,"color":"#53B0AE","pantone_value":"15-5217"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}'
        main = WebClass(driver)
        main.click_button_single_user(button_list_colors)
        main.send_get_request(body, list_colors_resource, 200)

    @pytest.mark.get_request
    def test_single_color(self, driver, setup_function):  # Клик по запросу SINGLE <RESOURCE> на главной странице с проверкой ответа и статус-кода
        body = '{"data":{"id":2,"name":"fuchsia rose","year":2001,"color":"#C74375","pantone_value":"17-2031"},"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}'
        resource = '/api/unknown/2'
        main = WebClass(driver)
        main.click_button_single_user(button_single_color)
        main.send_get_request(body, resource, 200)

    @pytest.mark.get_request
    def test_single_color_not_found(self, driver, setup_function):  # Клик по запросу SINGLE <RESOURCE> NOT FOUND на главной странице с проверкой ответа и статус-кода
        body = '{}'
        resource = '/api/unknown/23'
        main = WebClass(driver)
        main.click_button_single_user(button_single_color_not_found)
        main.send_get_request(body, resource, 404)

    @pytest.mark.user
    @pytest.mark.post_request
    def test_create_user(self, driver, setup_function):  # Клик по запросу CREATE на главной странице с проверкой ответа и статус-кода
        body_for_request = {"name": "morpheus", "job": "leader"}
        main = WebClass(driver)
        main.click_button_single_user(button_create_user)
        main.send_post_request(body_for_request, users_resource, 201)

    @pytest.mark.user
    @pytest.mark.put_request
    def test_update_user_put(self, driver, setup_function):  # Клик по запросу UPDATE на главной странице с проверкой ответа и статус-кода
        body_for_request = {"name": "morpheus", "job": "zion resident"}
        resource = '/api/users/2'
        main = WebClass(driver)
        main.click_button_single_user(button_update_user_put)
        main.send_put_request(body_for_request, resource, 200)

    @pytest.mark.user
    @pytest.mark.patch_request
    def test_update_user_patch(self, driver, setup_function):  # Клик по запросу UPDATE на главной странице с проверкой ответа и статус-кода
        body_for_request = {"name": "morpheus", "job": "zion resident"}
        resource = '/api/users/2'
        main = WebClass(driver)
        main.click_button_single_user(button_update_user_patch)
        main.send_patch_request(body_for_request, resource, 200)

    @pytest.mark.user
    @pytest.mark.delete_request
    def test_delete_user(self, driver, setup_function):  # Клик по запросу DELETE на главной странице с проверкой ответа и статус-кода
        resource = '/api/users/2'
        main = WebClass(driver)
        main.click_button_single_user(button_delete_user)
        main.send_delete_request(resource, 204)

    @pytest.mark.post_request
    def test_reg(self, driver, setup_function):  # Клик по запросу REGISTER - SUCCESSFUL на главной странице с проверкой ответа и статус-кода
        body_for_request = {"email": "eve.holt@reqres.in", "password": "pistol"}
        main = WebClass(driver)
        main.click_button_single_user(button_reg)
        main.send_post_request(body_for_request, registration_resource, 200)

    @pytest.mark.post_request
    def test_reg_unsuccessful(self, driver, setup_function):  # Клик по запросу REGISTER - UNSUCCESSFUL на главной странице с проверкой ответа и статус-кода
        body_for_request = {"email": "sydney@fife"}
        main = WebClass(driver)
        main.click_button_single_user(button_reg_unsuccessful)
        main.send_post_request(body_for_request, registration_resource, 400)

    @pytest.mark.post_request
    def test_login(self, driver, setup_function):  # Клик по запросу LOGIN - SUCCESSFUL на главной странице с проверкой ответа и статус-кода
        body_for_request = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        main = WebClass(driver)
        main.click_button_single_user(button_login)
        main.send_post_request(body_for_request, auth_resource, 200)

    @pytest.mark.post_request
    def test_login_unsuccessful(self, driver, setup_function):  # Клик по запросу LOGIN - UNSUCCESSFUL на главной странице с проверкой ответа и статус-кода
        body_for_request = {"email": "peter@klaven"}
        main = WebClass(driver)
        main.click_button_single_user(button_login_unsuccessful)
        main.send_post_request(body_for_request, auth_resource, 400)

    @pytest.mark.user
    @pytest.mark.get_request
    def test_delay_list_user(self, driver, setup_function):  # Клик по запросу DELAYED RESPONSE на главной странице с проверкой ответа и статус-кода
        body = '{"page":1,"per_page":6,"total":12,"total_pages":2,"data":[{"id":1,"email":"george.bluth@reqres.in","first_name":"George","last_name":"Bluth","avatar":"https://reqres.in/img/faces/1-image.jpg"},{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},{"id":3,"email":"emma.wong@reqres.in","first_name":"Emma","last_name":"Wong","avatar":"https://reqres.in/img/faces/3-image.jpg"},{"id":4,"email":"eve.holt@reqres.in","first_name":"Eve","last_name":"Holt","avatar":"https://reqres.in/img/faces/4-image.jpg"},{"id":5,"email":"charles.morris@reqres.in","first_name":"Charles","last_name":"Morris","avatar":"https://reqres.in/img/faces/5-image.jpg"},{"id":6,"email":"tracey.ramos@reqres.in","first_name":"Tracey","last_name":"Ramos","avatar":"https://reqres.in/img/faces/6-image.jpg"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}'
        resource = '/api/users?delay=3'
        main = WebClass(driver)
        main.click_button_single_user(button_delay_list_user)
        main.send_get_request(body, resource, 200)

