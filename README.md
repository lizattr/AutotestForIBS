# Тестовое задание по написанию автотестов для https://reqres.in/

## Описание
Проект содержит в себе тесты как для тестирования API с помощью библиотеки requests, так и UI-тесты, созданные с помощью webdriver. Цель проекта - продемонстрировать умения и знания в области написания автоматизированных тестов.

## Структура проекта

AutotestForIBS/
│
├── base/
│   ├── api_class.py - страница, содержащая методы тестирования api
│   ├── base_class.py - страница, содержащая базовые функции для вызова в других классах
│   └── web_class.py - страница, которая содержит методы для UI-тестирования
│
├── tests/
│   ├── test_api.py - страница с тестами для API
│   ├── test_web.py - страница с UI-тестами
│
└── locators.py - файл, где содержатся все импорты и переменные, необходимые для тестов

## Требования

Все необходимые пакеты приведены в файле requirements.txt. 

Установить их можно командой:
pip install -r requirements.txt

## Запуск тестов

Запустить все тесты можно командой:
python -m pytest -sv tests/

Также можно запустить тесты с учетом параметров. Например, для запуска только GET-запросов следует ввести команду: 
python -m pytest -svm get_request tests/

## Автор
Елизавета Коморникова

lizatrue5@gmail.com

