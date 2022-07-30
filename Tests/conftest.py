import pytest
from selenium import webdriver


@pytest.fixture(params=['chrome', 'firefox'], scope='class')
def init_driver(request):
    global web_driver
    if request.param == 'chrome':
        web_driver = webdriver.Chrome()
    if request.param == 'firefox':
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()
