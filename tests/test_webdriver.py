from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import yaml
from steps.webdriver_functions import *
from steps.webelement_functions import *

data = load_yaml(f"{ROOT_DIR}/data/config.yml")

# # ********* Scenario with correct steps
# launch_website("https://letskodeit.teachable.com/p/practice")
# find_elements_tag('button')
# web_driver_properties_switch_to_tab()
# close_browser()

# # ********* Scenario for go back, forward, refresh
# launch_website("http://automationpractice.com/index.php")
# women_tab = "//a[@class='sf-with-ul'][contains(text(),'Women')]"
# click_element_by_xpath(women_tab)
# go_back_to_previous_page()
# refresh_browser()
# go_next_page()
# close_browser()

# # *********** Scenario: Login to "http://automationpractice.com/index.php"
# web_url = "http://automationpractice.com/index.php"
# username = "hello@email.com"
# pswd = "$Password001"

# 'data' is the same information as data1 below:
# data1 = {
#     'scenario1': {'web_url': 'http..', 'username': 'hello', 'password': 'yourpass'},
#     'scenario2': {'web_url': 'http..', 'username': 'hello', 'password': 'yourpass'}
#     }

web_url = data['scenario1']['web_url']
username = data['scenario1']['username']
pswd = data['scenario1']['password']

# url = data['url']
# email = data['email']
# passcode = data['passcode']


# login_to_automation_practice(web_url, username, pswd)
# login_to_automation_practice(email=username, password=pswd, url=web_url)


# test_right_click()
# test_drag_and_drop()
# test_get_attribute()
# test_radio_button_is_displayed_selected()

# agenda for next class:

# 09/19/2020 - week 8
# Instructions to Class Project1 and Class project 2
# organize the tests
# CheckBox is the same as Radio button - try it yourself
# drop down list
# test_drop_down_list()
# hw/ try on automationpractice.com on Women tab, sort by

# Agenda for 09/20/2020 ****************************
# yaml file and information hiding using data files
# alert (confirm, cancel) - java script
test_alerts()

# hover over element
# test_mouse_hovering()
# close_browser()


# Agenda: next class
# take a screenshot with selenium
# included in test_alerts()

#  explicit waits , and difference between implicit_wait()
# used in enter_text_by_xpath
