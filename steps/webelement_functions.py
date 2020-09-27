import logging

import yaml
from os.path import dirname, abspath

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from steps.webdriver_functions import *

# to find the full location of your project in your system use this
ROOT_DIR = dirname(dirname(abspath(__file__)))


def load_yaml(filepath):
    with open(filepath, 'r') as data:
        document = yaml.safe_load(data)
    return document


def enter_text_by_xpath(xpath, some_text):
    """
    this method finds the element by xpath and enters text in it
    :param xpath: correct unique xpath of single INPUT element
    :param some_text: text to be entered in the element
    """
    try:
        print(f"xpath provided: {xpath}")
        # element = driver.find_element_by_xpath(xpath)
        wwait = WebDriverWait(driver, 10)
        # element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        element = wwait.until(EC.presence_of_element_located((By.XPATH, xpath)))

        print(f"entering the following text :{some_text}")
        element.send_keys(some_text)
    except WebDriverException as err:
        print(f"Entering Text failed by following xpath: {xpath}")
        print(err)
        take_screenshot('ErrorEnterText_')


def click_element_by_xpath(xpath):
    """
    this method finds the element by xpath and clicks it
    :param xpath: correct unique xpath of single element
    """
    try:
        print(f"xpath provided: {xpath}")
        # element = driver.find_element_by_xpath(xpath)
        wwait = WebDriverWait(driver, 10)
        element = wwait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

        print("clicking the element")
        element.click()
    except NoSuchElementException as err:
        print(f"Check element by following xpath: {xpath}")
        print(err)
        take_screenshot('ErrorClickElement_')


def login_to_automation_practice(url, email, password):
    """
    *********** Scenario: Login to "http://automationpractice.com/index.php"
    Prerequisite: create an account:
    username: hello@email.com, have strong password: "$Password001"
    identify all locators by inspecting on browser (xpath, optional: id, css selector):
    sign_in_link = "//a[@class='login'" # this is incorrect XPATH, to see Try Except
    """
    sign_in_link = "//a[@class='login']"
    email_input = "//input[@id='email']"
    password_input = "//input[@id='passwd']"
    sign_in_button = "//button[@id='SubmitLogin']"
    sign_out_link = "//a[@class='logout']"

    # Steps:
    launch_website(url)
    click_element_by_xpath(sign_in_link)
    time.sleep(2)
    enter_text_by_xpath(email_input, email)
    enter_text_by_xpath(password_input, password)
    click_element_by_xpath(sign_in_button)
    time.sleep(10)
    print("successfully signed in ")
    print("signing out now...")
    click_element_by_xpath(sign_out_link)


def test_right_click():
    """Right click and selects the chrome option to open on new tab"""
    # TODO: find out right way to retrieve chrome right click options, which is not Element property

    sign_in_link = "//a[@class='login']"
    launch_website("http://automationpractice.com/index.php")
    sign_in_element = driver.find_element_by_xpath(sign_in_link)
    actions = ActionChains(driver)
    actions.context_click(sign_in_element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).build().perform()
    actions.send_keys(Keys.ARROW_DOWN).perform()
    actions.send_keys(Keys.ENTER).perform()


def test_drag_and_drop():
    # Step:
    # start the website
    # drag and drop item 1
    # verify item 1 is under dropped list
    # drag and drop item 2
    # verify item 2 is under dropped list

    launch_website("http://testautomationpractice.blogspot.com/")
    item1 = driver.find_element_by_xpath("//div[@id='draggable']")
    drop_zone = driver.find_element_by_xpath("//div[@id='droppable']")

    actions = ActionChains(driver)
    actions.drag_and_drop(item1, drop_zone).perform()
    # actions.move_to_element(item1, drop_zone).perform() # hover over element (mouse movement)
    print("drag and drop finished.")


def test_radio_button_is_displayed_selected():
    # Scenario: is_displayed(), is_selected(), is_enabled()

    launch_website("https://letskodeit.teachable.com/p/practice")

    xpath1 = "//div[@id='radio-btn-example']"
    radio_button_example = driver.find_element_by_xpath(xpath1)
    print(f"Radio button example is displayed: {radio_button_example.is_displayed()}")

    bmw_option = None
    if radio_button_example.is_displayed():
        bmw_option = driver.find_element_by_xpath("//input[@id='bmwradio']")
        bmw_option.click()
        time.sleep(1)
    else:
        print("Radio button example is not displayed")

    print('bwm option is clicked')
    print(f"Is bmw option selected: {bmw_option.is_selected()}")
    assert bmw_option.is_selected(), "bmw Option is not selected "
    print("Yeaah it is selected. Test Passed")


def test_get_attribute():
    """ this is dependent on other functions so it is calling function first."""

    test_radio_button_is_displayed_selected()

    print("getting the attribute of the element")
    button = driver.find_element_by_xpath("//button[@id='openwindow']")
    value1 = button.get_attribute("onclick")
    value2 = button.get_attribute("class")
    print(f"Attributes of the element: onlick: {value1} , class: {value2}")
    print(f"Text of the button : {button.text}")


def test_drop_down_list():
    launch_website("https://letskodeit.teachable.com/p/practice")

    dd_list_xpath = "//select[@id='carselect']"  # real ddown that selenium can handle
    dd_list = driver.find_element_by_xpath(dd_list_xpath)

    car_selection = Select(dd_list)  # !!!!!!!!!!

    text_options = [option.text for option in car_selection.options]
    print("Options available in the list: ", text_options)
    car_selection.select_by_index(1)

    # text_selected_ones = []
    # for option in car_selection.all_selected_options:
    #     text_selected_ones.append(option.text)
    text_selected_ones = [option.text for option in car_selection.all_selected_options]
    print("Options selected: ", text_selected_ones)

    #  selecting by value
    car_selection.select_by_value('honda')
    text_selected_ones = [option.text for option in car_selection.all_selected_options]
    print("Options selected: ", text_selected_ones)

    #  selecting by visible text
    car_selection.select_by_visible_text('BMW')
    text_selected_ones = [option.text for option in car_selection.all_selected_options]
    print("Options selected: ", text_selected_ones)


def test_alerts():
    """
    Switching to alert, get text of the alert, confirm and cancel js alerts.
    """
    name_input = "//input[@id='name']"
    confirm_button = "//input[@id='confirmbtn']"

    launch_website("https://letskodeit.teachable.com/p/practice")
    # driver.find_element_by_xpath(name_input).send_keys('John')
    enter_text_by_xpath(name_input, 'John')
    take_screenshot('enteringName')
    driver.find_element_by_xpath(confirm_button).click()
    print("alert is clicked")

    # test case 1: confirm
    alert = driver.switch_to.alert
    time.sleep(5)
    alert_text = alert.text
    print("1. Alert text captured: ", alert_text)
    assert 'John' in alert_text
    take_screenshot("alertOpened")
    # clicking OK button on alert
    alert.accept()
    print("Alert confirmed!")

    # test case 2: cancel
    driver.find_element_by_xpath(name_input).send_keys('Jane')
    driver.find_element_by_xpath(confirm_button).click()
    print("alert is clicked to cancel")
    take_screenshot("alertJane")

    alert = driver.switch_to.alert
    time.sleep(5)
    alert_text = alert.text
    print("2. Alert text captured: ", alert_text)
    assert 'Jane' in alert_text
    # clicking cancel on alert
    alert.dismiss()
    print("Alert Canceled!")
    take_screenshot('AllDone')


def test_mouse_hovering():
    # following lines were for automaitonpractice.com
    # product_name_xpath = "//ul[@id='homefeatured']//a[@class='product-name' and @title='Faded Short Sleeve T-shirts']"
    # add_to_cart_button = "//div/a[@title='Add to cart' and @data-id-product='1']"
    # product_xpath=f"{product_name_xpath}/../.." # this path goes to parent and then to grandparent of the element
    # product_add_to_cart = f"{product_xpath}{add_to_cart_button}"

    mouse_hover_xpath = "//button[@id='mousehover']"
    top_option = "//a[contains(text(),'Top')]"

    launch_website("https://letskodeit.teachable.com/p/practice")

    # mouse hovering before clicking the top option
    mouse_hover_button = driver.find_element_by_xpath(mouse_hover_xpath)
    mouse_hover_button.click()
    driver.execute_script("arguments[0].submit();", mouse_hover_button)

    actions = ActionChains(driver)
    actions.move_to_element(mouse_hover_button).perform()

    # actions.move_to_element(driver.find_element_by_xpath(mouse_hover_xpath)).perform()

    # actions.drag_and_drop_by_offset(element, 100, 0)
    # actions.drag_and_drop_by_offset(element, -100, 0)

    print("Mouse hovering is performed.")

    driver.find_element_by_xpath(top_option).click()
    print("Top option is clicked.")
    time.sleep(2)
    expected_url = "https://letskodeit.teachable.com/p/practice#top"
    assert expected_url == driver.current_url
    print("Url contains #top. Test Passed.")


def highlight_element(element):
    js_script = "arguments[0].setAttribute('style', arguments[1]);"
    original_style = element.get_attrivute('style')
    new_style = "color: green; border: 2px solid green;"
    # new_style = "background: yellow; color: green; border: 2px solid green;"
    driver.execute_script(js_script, element, new_style)
    driver.execute_script(js_script, element, original_style)


def take_screenshot(message=""):
    timestmp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
    # ROOT_DIR is "C:/deb/week7"
    file_location = f"{ROOT_DIR}/screenshots/"
    # file_location = f"C:/deb/week7/screenshots/"
    file_name = message + timestmp + ".png"
    full_file_path = file_location + file_name

    driver.save_screenshot(full_file_path)
    # driver.get_screenshot_as_png(message + timestmp)


def get_str_day():
    return time.strftime("%Y%m%d")  # 20200927


def get_str_seconds():
    return time.strftime("%Y%m%d_%H%M%S", time.localtime())


def create_logger(filename=""):
    logging.basicConfig(filename=f"{ROOT_DIR}/logs/{filename}{get_str_day()}.log",
                        level=logging.INFO,
                        format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
                        filemode='a')  # 'w' - to overwrite in each run, 'a' - append
    return logging.getLogger()
