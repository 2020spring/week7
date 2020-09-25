import datetime
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException

# *******************  Reusable steps *****************************
# Initializing a new browser
from steps.webelement_functions import take_screenshot

driver = webdriver.Chrome()
# driver.maximize_window()
driver.implicitly_wait(20)  # read more about this


# class TestAssrt(unittest2.TestCase):
#     def anythAssert(self):
#         assertEqual(25, 50-35+10)

def launch_website(url):
    driver.get(url)
    print(f"opened the browser and website : {url}")
    time.sleep(1)  # thread.sleep() in java


def find_elements_tag(tag_name):
    """1. find all buttons, working with list of elements"""
    buttons = driver.find_elements_by_xpath(f'//{tag_name}')
    # buttons.text - this is incorrect since buttons is not one element
    # buttons[1].click
    for button in buttons:
        print('text of button: ', button.text)


def open_tab_by_link_text(text):
    """2. find by link text"""
    open_tab = driver.find_element_by_link_text(text)
    # open_tab2 = driver.find_element_by_partial_link_text('en Tab')
    # open_tab.click() # this will open a new tab but does not switches to it
    time.sleep(5)
    return open_tab


def web_driver_properties():
    """using WebDriver Class properties"""
    print('Current url: ', driver.current_url)
    print('Current title: ', driver.title)
    print('Current win_handle: ', driver.current_window_handle)
    print('Current name: ', driver.name)


def web_driver_properties_switch_to_tab():
    """
    3. using WebDriver Class properties
    Works only for "https://letskodeit.teachable.com/courses" tab.
    """
    url1 = driver.current_url
    title1 = driver.title
    win_handle1 = driver.current_window_handle
    name1 = driver.name
    print('Current url1: ', url1)
    print('Current title1: ', title1)
    print('Current win_handle1: ', win_handle1)
    print('Current name1: ', name1)

    # after getting all details of the current tab, we are opening new tab
    open_tab_by_link_text('Open Tab').click()  # this will open a new tab but does not switches to it

    # switch to a new tab, WebDriver Method - switch_to.window(new_handle)
    handles = driver.window_handles
    print(handles)

    url2 = ""
    title2 = ""
    win_handle2 = ""
    # driver.switch_to.window(handles[1]) - might work but not guarantied

    for handle in handles:
        if handle != win_handle1:
            driver.switch_to.window(handle)

        url2 = driver.current_url
        title2 = driver.title
        win_handle2 = driver.current_window_handle

    print('Current url2: ', url2)
    print('Current title2: ', title2)
    print('Current win_handle2: ', win_handle2)

    # verifying new tabe url and title is by Requirement
    assert url2 == 'https://letskodeit.teachable.com/courses'

    assert title2 == "Let's Kode It"
    # assertEqual(title2, "Let's Kode It") alternative

    # """3. closing tabs vs closing a browser"""
    driver.close()  # this will close the current tab
    print("current tab is closed")
    time.sleep(5)

    # """switch back to initial window handle (initial browser tab)"""
    driver.switch_to.window(win_handle1)

    print('Title after closing a new tab: ', driver.title)
    print('current_url after closing a new tab: ', driver.current_url)
    print('current_window_handle after closing a new tab: ', driver.current_window_handle)


def close_browser():
    web_driver_properties()
    driver.quit()  # this will close the browser
    print("browser is closed")


def refresh_browser():
    print("browser is being refreshed ...")
    driver.refresh()


def go_back_to_previous_page():
    print("going back to previous page ...")
    driver.back()


def go_next_page():
    print("going to next page ...")
    driver.forward()


def click_element_by_xpath(xpath):
    """
    this method finds the element by xpath and clicks it
    :param xpath: correct unique xpath of single element
    """
    try:
        print(f"xpath provided: {xpath}")
        element = driver.find_element_by_xpath(xpath)
        print("clicking the element")
        element.click()
    except NoSuchElementException as err:
        print(f"Check element by following xpath: {xpath}")
        print(err)
        take_screenshot('ErrorClickElement_')


def enter_text_by_xpath(xpath, some_text):
    """
    this method finds the element by xpath and enters text in it
    :param xpath: correct unique xpath of single INPUT element
    :param some_text: text to be entered in the element
    """
    try:
        print(f"xpath provided: {xpath}")
        element = driver.find_element_by_xpath(xpath)
        print(f"entering the following text :{some_text}")
        element.send_keys(some_text)
    except WebDriverException as err:
        print(f"Entering Text failed by following xpath: {xpath}")
        print(err)
        take_screenshot('ErrorEnterText_')
