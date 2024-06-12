import allure


@allure.id("32848")
@allure.title("Successful login")
@allure.label("suite", "manual test")
@allure.label("owner", "allure8")
def test_login_successful():
    with allure.step("Открыть страницу https://testing.github.com"):
        pass
    with allure.step("Перейти на вкладку auth"):
        pass
    with allure.step("Ввести валидные данные пользователя"):
        with allure.step("Логин: test"):
            pass
        with allure.step("Пароль: test"):
            pass
    with allure.step("Нажать кнопку submit"):
        pass
    with allure.step("Отобразилась страница с профилем пользователя"):
        pass
    with allure.step("Проверить в логах информацию об успешной регистрации"):
        pass