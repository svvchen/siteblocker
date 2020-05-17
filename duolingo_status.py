import secrets
import xvfbwrapper

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.options import Options

# pass in a goal
def check_goal_reached(goal):

    # headless = no real chrome window!
    options = webdriver.ChromeOptions()
    options.headless = True

    # to get this to work on another machine
    # you may need to just update the file path
    browser = driver = webdriver.Chrome(options = options, executable_path='/Users/svvchen/Downloads/chromedriver')

    # open duolingo page
    browser.get("https://www.duolingo.com/")
    wait = WebDriverWait(browser, 20)

    # Credit to DustinAlandzes for coming up
    # with this login button mechanism. He
    # waits for the page to load until he sees
    # the login trigger.

    login_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'I ALREADY HAVE AN ACCOUNT')]"))
    )

    # once it's ready, click.
    login_button.click()

    # type in user + pass
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email or username']")))
    username_field.send_keys(secrets.username)

    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
    password_field.send_keys(secrets.password)

    # more logic to properly wait for page
    # loads properly, first by storing the
    # current login page url
    current_url = driver.current_url

    # initiate the new load
    password_field.submit()

    # then, comparing new url to old, and
    # only proceeding once they're different
    WebDriverWait(driver, 15).until(EC.url_changes(current_url))

    # VERY weirdly, I can't find the element
    # until I've refreshed after page load
    browser.refresh()

    # _3entt is the class name of the xp cmpnt
    xp_element = browser.find_element_by_class_name('_3entt').text

    # change 14/30 XP => "14" => 14
    xp_string = xp_element.split("/")[0]
    xp_int = int(xp_string)

    print("Current xp: " + xp_string)

    if xp_int > goal:
        print("Goal reached!")
        return True
    else:
        print("Goal not reached.")
        return False

    browser.quit()

# test
# check_goal_reached(50)
