import os
import pytest
from selenium import webdriver


driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser name")


@pytest.fixture(scope="function")
def browser_instance(request):
    global driver
    browser = request.config.getoption("browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    if report.when in ["setup", "call"]:
        xfail = hasattr(report, "wasxfail")

        if (xfail and report.skipped) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), "reports")
            os.makedirs(reports_dir, exist_ok=True)

            file_name = report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_") + ".png"
            full_path = os.path.join(reports_dir, file_name)

            print("Screenshot saved at:", full_path)

            _capture_screenshot(item, full_path)

            if os.path.exists(full_path):
                pytest_html = item.config.pluginmanager.getplugin("html")

                html = f'''
                    <div>
                        <img src="{file_name}" alt="screenshot"
                             style="width:304px;height:228px;"
                             onclick="window.open(this.src)"
                             align="right"/>
                    </div>
                '''
                extras.append(pytest_html.extras.html(html))

    report.extras = extras


def _capture_screenshot(item, file_path):
    driver = item.funcargs.get("browser_instance", None)

    if driver is not None:
        driver.save_screenshot(file_path)
    else:
        print("No browser_instance fixture found for this test, screenshot skipped.")