from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from locators import *


class WebClass(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    request_link = "url"
    response_body = "//pre"

    # getters

    def get_request_link(self):
        return WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, self.request_link)))

    def get_test_response_body(self):
        return WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, self.response_body))).text

    # actions

    def click_button_single_user(self, locator):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator))).click()

    def click_request_link(self):
        self.get_request_link().click()

    def check_text_body(self, body_expected):
        text_body = self.get_test_response_body()
        assert body_expected in text_body, "Ошибка. Текст не совпадает"
        print("Успешно. Текст ответа совпадает с ожидаемым результатом.", end=" ")

    def check_get_status_code(self, resource, code):
        response = requests.get(base_url + resource)
        assert response.status_code == code, f"Ошибка. Статус-код {str(response.status_code)} некорректный"
        print(f"Успешно. Статус-код {str(response.status_code)}")

    def check_post_status_code(self, body_for_request, resource, code):
        response = requests.post(base_url + resource, json=body_for_request)
        assert response.status_code == code, f"Ошибка. Статус-код {str(response.status_code)} некорректный"
        print(f"Успешно. Статус-код {str(response.status_code)}")

    def check_put_status_code(self, body_for_request, resource, code):
        response = requests.put(base_url + resource, json=body_for_request)
        assert response.status_code == code, f"Ошибка. Статус-код {str(response.status_code)} некорректный"
        print(f"Успешно. Статус-код {str(response.status_code)}")

    def check_patch_status_code(self, body_for_request, resource, code):
        response = requests.patch(base_url + resource, json=body_for_request)
        assert response.status_code == code, f"Ошибка. Статус-код {str(response.status_code)} некорректный"
        print(f"Успешно. Статус-код {str(response.status_code)}")

    def check_delete_status_code(self, resource, code):
        response = requests.delete(base_url + resource)
        assert response.status_code == code, f"Ошибка. Статус-код {str(response.status_code)} некорректный"
        print(f"Успешно. Статус-код {str(response.status_code)}")

    # methods

    def send_get_request(self, body_expected, resource, code):
        self.click_request_link()
        self.check_text_body(body_expected)
        self.check_get_status_code(resource, code)

    def send_post_request(self, body_for_request, resource, code):
        self.click_request_link()
        self.check_post_status_code(body_for_request, resource, code)

    def send_put_request(self, body_for_request, resource, code):
        self.click_request_link()
        self.check_put_status_code(body_for_request, resource, code)

    def send_patch_request(self, body_for_request, resource, code):
        self.click_request_link()
        self.check_patch_status_code(body_for_request, resource, code)

    def send_delete_request(self, resource, code):
        self.click_request_link()
        self.check_delete_status_code(resource, code)
