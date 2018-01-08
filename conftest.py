import pytest

global driver 

@pytest.mark.usefixtures("url")
@pytest.yield_fixture(scope="class")
def driver(request, url):
    global driver 
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--url", action="store")

@pytest.fixture(scope='session', autouse=True)
def url(request):
    return request.config.option.url

