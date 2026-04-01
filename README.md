# Sprint_5

UI‑тестирование сервиса [Stellar Burgers](https://stellarburgers.education-services.ru) в браузере Google Chrome.

## Стек технологий

* **Язык:** Python.
* **Фреймворк:** PyTest.
* **Автоматизация:** Selenium WebDriver.
* **Запуск тестов в один поток:** `pytest -v`.

## Структура проекта

    Sprint_5/
        ├── conftest.py
        ├── data.py
        ├── locators.py
        ├── README.md
        └── tests/
            ├── __init__.py
            ├── test_constructor_section.py
            ├── test_login_page.py
            ├── test_profile_page.py
            └── test_registration_page.py
        

### Основные модули

***1. conftest.py***

Предоставляет фикстуры для настройки окружения тестов.

***2. data.py***

 Содержит URL‑адреса всех страниц приложения в едином месте; Автоматизирует подготовку окружения; Генерирует случайных тестовых пользователей для изолированных тестов; Работает со статическими данными пользователя. 

***3. locators.py***

Содержит локаторы элементов веб‑интерфейса, сгруппированы в виде классов.

### Тесты проекта  `tests/`:

**1. Регистрация**

***test_registration_page.py:***
* `test_successful_registration` — тест успешной регистрации.
* `test_incorrect_password_error` — тестирует валидацию пароля (с параметризацией).

**Запуск:** `pytest -v tests/test_registration_page.py`

**2. Вход в систему** 

Проверка авторизации через разные точки входа - ***test_login_page.py:***
* `test_login_via_login_button_show_main_page` — через кнопку «Войти в аккаунт» на главной странице.
* `test_login_via_profile_show_main_page` — через кнопку «Личный кабинет».
* `test_login_via_registration_page_show_main_page` — вход через кнопку в форме регистрации.
* `test_login_via_recover_pass_page_show_main_page` — вход через кнопку в форме восстановления пароля.

**Запуск:** `pytest -v tests/test_login_page.py`

**3. Личный кабинет** 

Тесты навигации и функционала профиля - ***test_profile_page.py:***
* `test_click_profile_link_open_profile_page` — переход по клику на «Личный кабинет».
* `test_click_constructor_link_show_constructor` — переход по клику на «Конструктор».
* `test_click_main_logo_show_constructor` — переход на главную по клику на логотип Stellar Burgers.
* `test_click_logout_button_show_login_page` — выход по кнопке «Выйти» в личном кабинете.

**Запуск:** `pytest -v tests/test_profile_page.py`

**4. Раздел «Конструктор»**

Проверка переключения между разделами конструктора - ***test_constructor_section.py:***
* «Булки» — тест `test_click_buns_scroll_to_buns`.
* «Соусы» — тест `test_click_sauces_scroll_to_sauces`.
* «Начинки» — тест `test_click_fillings_scroll_to_fillings`.

**Запуск:** `pytest -v tests/test_constructor_section.py`
