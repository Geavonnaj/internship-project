from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

from webdriver_manager.chrome import ChromeDriverManager

from app.application import Application

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    ### CHROME ###
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    ### CHROME HEADLESS MODE ###
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )


    ### SAFARI ###
    # context.driver = webdriver.Safari()


    ### FIREFOX ###
    # options = webdriver.FirefoxOptions()
    # service = Service(executable_path='/Users/peggyadams/Desktop/internship-project/geckodriver')
    # context.driver = webdriver.Firefox(options=options)

    ### FIREFOX HEADLESS ###
    # options = webdriver.FirefoxOptions()
    # options.headless = True
    # options.add_argument("--window-size=1920,1080")
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    # driver.implicitly_wait(10)


    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'geavonna_HPsZqO'
    bs_key = 'MVsGzym7mATionLB7Roi'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'os': 'Windows',
        'osVersion': '10',
        'browserName': 'Firefox',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)


    ### OBJECTS ###
    context.driver.wait = WebDriverWait(context.driver, 60)
    context.driver.maximize_window()
    context.driver.maximize_window()
    # context.driver.set_window_size(1280, 720)
    context.driver.implicitly_wait(10)
    context.app = Application(context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
