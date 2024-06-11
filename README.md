# Запуск автотестов с применением паттерна Page Object

## Задание
[Описание задания](https://stepik.org/lesson/238819/step/1?unit=211271)
Вам, как разработчику автотестов, нужно реализовать решение, которое позволит запускать автотесты для разных браузеров, передавая нужный браузер и язык пользователя в командной строке.  

1. Создать GitHub-репозиторий, в котором будут лежать конфигурационный файлы [conftest.py](conftest.py), библиотечный файл [requirements.txt](requirements.txt) и тесты [test_login_page.py](test_login_page.py), [test_main_page.py](test_main_page.py), [test_product_page.py](test_product_page.py).
1. Создать [base_page.py](base_page.py), [login_page.py](login_page.py), [main_page.py](main_page.py), [product_page.py](product_page.py), [basket_page.py](basket_page.py), [locators.py](locators.py), [links.py](links.py) для реализации тестирования. 
1. Добавить в файл `conftest.py` обработчик, который считывает из командной строки параметр **language**.
1. Реализовать в файле `conftest.py` логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре **browser** и передаваться в тест как параметр.
1. Маркеры описать в файле **pytest.ini**.
1. Для назначения фикстур использовать декоратор `@pytest`.
1. В тестовых файлах реализовать позитивные/негативные проверки.

## Решение проверяется по следующим критериям:
1. Браузер объявляется в фикстуре **browser** и передаётся в тест как параметр. Аналогично для языка.
1. Применение паттерна Page Object Model (POM).
1. Базовая страница для проекта - BasePage - класс-предок для страниц сайта.
1. LoginPage, BasketPage, MainPage, ProductPage - реализация для отдельных страниц сайта.
1. Создание локаторов как кортежей атрибута класса.
1. Элементы страниц в паттерне POM.
1. Создание тест-кейсов для АТ.
1. Валидация входных данных с применением CSS-селекторов.
1. Селекторы являются уникальными для проверяемых страниц и описаны в `locators.py`.
1. Вывод данных для тестов в файл list_of_links.txt.
1. Проверяется наличие/отсутствие элементов на странице. Есть **assert**.
1. Реализованы переходы между страницами.
1. Настройка явных и неявных ожиданий.
1. Обработка alerts.
1. Удобство поддержки тестов — инкапсуляция бизнес-логики в методах.
1. Стек: Python, PyTest, Selenium, WebDriver.

## Особенности реализации
1. Реализован запуск теста на разных браузерах: Chrome и Firefox. Каждому браузеру установлен вебдрайвер. Для выбора используется параметр командной строки **browser_name**. Пример запуска:  
`pytest --browser_name=firefox test_login_page.py`
1. Реализован запуск теста на разных языках. Для выбора используется параметр командной строки **language**. Пример запуска:  
`pytest --language=ru test_login_page.py`
1. По умолчанию используются:
    - язык - `en`
    - браузер - `chrome`

## Для запуска теста

### Виртуальное окружение
- Для создания виртуального окружения необходимо последовательно выполнить в командной строке:
	`$ mkdir environments`
	`$ cd environments`
	`$ python3 -m venv selenium`
- Чтобы активировать окружение, нужно запустить в командной строке из папки `enviroments` созданный приложением `venv` файл `activate.bat`. 
- После активации виртуального окружения можно устанавливать нужные пакеты и запускать скрипты для тестов.
- `deactivate` - команда для выхода из окружения.

### Параметры
Пример с параметрами:
`pytest -rx -v -m "user_login" --tb=line test_product_page.py`

- `--tb=line`		- чтобы сократить лог с результатами теста
- `-s` 				- выводить результат работы команды **print()**
- `-rx`				- report on XFAIL
- `-v`				- подробная информация о прохождении тестов
- `-m "name_mark"`	- запуск тестов с маркером "name_mark"

### Перезапуск тестов
Установка:  
`pip install pytest-rerunfailures`  
Пример с перезапуском:  
`pytest --reruns 2 test_product_page.py`

### Текущий язык браузера
curr_language = browser.execute_script('return window.navigator.language').
