import requests
import random
import datetime
import pytest
from selenium import webdriver

base_url = "https://reqres.in"
users_resource = "/api/users"
users_resource_for_id = "/api/users/"
list_colors_resource = "/api/unknown/"
registration_resource = "/api/register"
auth_resource = "/api/login"

random_real_id = random.randint(1, 12)
random_unreal_id = random.randint(13, 100)
password = random.randint(111111, 999999)
delay = random.randint(1, 5)
email_for_reg = "eve.holt@reqres.in"
mail_for_negative_reg = f"testmail{datetime.datetime.utcnow().strftime('%d%M%S')}@mail.com"

names_matrix = ['morpheus', 'trinity', 'neo', 'agent smith']
job_matrix = ['leader', 'the first mate', 'the one', 'agent']

simple_names = ['nick', 'ann', 'kate', 'sam']
simple_job = ['florist', 'banker', 'doctor', 'artist']

button_single_user = '[data-id="users-single"]'
button_single_user_not_found = '[data-id="users-single-not-found"]'
button_list_colors = '[data-id="unknown"]'
button_single_color = '[data-id="unknown-single"]'
button_single_color_not_found = '[data-id="unknown-single-not-found"]'
button_create_user = '[data-id="post"]'
button_update_user_put = '[data-id="put"]'
button_update_user_patch = '[data-id="patch"]'
button_delete_user = '[data-id="delete"]'
button_reg = '[data-id="register-successful"]'
button_reg_unsuccessful = '[data-id="register-unsuccessful"]'
button_login = '[data-id="login-successful"]'
button_login_unsuccessful = '[data-id="login-unsuccessful"]'
button_delay_list_user = '[data-id="delay"]'
